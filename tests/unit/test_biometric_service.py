"""Unit tests for BiometricService, AES-256-GCM encryption, anti-spoofing heuristics, and 1:1 matching."""

import pytest
from PIL import Image, ImageDraw
from services.biometric_service import (
    BiometricEncryptionService,
    BiometricSecurityError,
    BiometricService,
    FaceAntiSpoofingHeuristic,
    MockFaceEngine,
    compute_cosine_similarity,
    decode_base64_image,
)


def _create_test_image(pattern: str = "face_a", width: int = 160, height: int = 160, brightness: int = 128) -> Image.Image:
    """Helper to generate PIL images with deterministic distinct patterns."""
    img = Image.new("RGB", (width, height), color=(brightness, brightness, brightness))
    draw = ImageDraw.Draw(img)
    if pattern == "face_a":
        # Draw distinctive geometric shapes resembling face elements
        draw.ellipse([40, 40, 70, 70], fill=(20, 20, 20))
        draw.ellipse([90, 40, 120, 70], fill=(20, 20, 20))
        draw.rectangle([70, 75, 90, 105], fill=(40, 40, 40))
        draw.arc([50, 110, 110, 135], start=0, end=180, fill=(10, 10, 10), width=4)
    elif pattern == "face_b":
        # Completely different pattern
        draw.rectangle([20, 20, 60, 60], fill=(200, 50, 50))
        draw.rectangle([100, 20, 140, 60], fill=(50, 200, 50))
        draw.ellipse([50, 80, 110, 140], fill=(50, 50, 200))
    elif pattern == "blank":
        pass  # Flat color
    return img


def test_encryption_roundtrip():
    """Verify AES-256-GCM encryption and decryption round-trip."""
    enc = BiometricEncryptionService()
    test_vector = [0.123456, -0.654321, 0.999999] + [0.0] * 509
    user_id = 42

    encrypted = enc.encrypt_vector(test_vector, user_id=user_id)
    assert isinstance(encrypted, str)
    assert len(encrypted) > 100

    decrypted = enc.decrypt_vector(encrypted, user_id=user_id, expected_dim=512)
    assert len(decrypted) == 512
    for orig, dec in zip(test_vector, decrypted):
        assert pytest.approx(orig, abs=1e-5) == dec


def test_encryption_tamper_detection():
    """Verify that tampering with ciphertext fails authentication."""
    enc = BiometricEncryptionService()
    test_vector = [0.5] * 512
    user_id = 99

    encrypted = enc.encrypt_vector(test_vector, user_id=user_id)
    # Alter one character in base64 payload
    tampered = encrypted[:-2] + ("A" if encrypted[-2] != "A" else "B") + encrypted[-1]

    with pytest.raises(BiometricSecurityError, match="corrupted or tampered"):
        enc.decrypt_vector(tampered, user_id=user_id, expected_dim=512)


def test_encryption_cross_account_substitution_prevented():
    """Verify that User A's template cannot be decrypted as User B's template."""
    enc = BiometricEncryptionService()
    test_vector = [0.25] * 512

    # Encrypted for user 101
    encrypted_for_101 = enc.encrypt_vector(test_vector, user_id=101)

    # Attempting to decrypt as user 102 MUST fail due to Associated Data mismatch
    with pytest.raises(BiometricSecurityError, match="corrupted or tampered"):
        enc.decrypt_vector(encrypted_for_101, user_id=102, expected_dim=512)


def test_anti_spoofing_heuristics():
    """Test image focus and illumination checks."""
    # 1. Dark image should fail
    dark_img = Image.new("RGB", (160, 160), color=(10, 10, 10))
    ok, msg, stats = FaceAntiSpoofingHeuristic.evaluate_quality(dark_img)
    assert not ok
    assert "dark" in msg.lower()

    # 2. Overexposed image should fail
    bright_img = Image.new("RGB", (160, 160), color=(245, 245, 245))
    ok, msg, stats = FaceAntiSpoofingHeuristic.evaluate_quality(bright_img)
    assert not ok
    assert "washed out" in msg.lower() or "overexposed" in msg.lower()

    # 3. Acceptable structured image should pass
    good_img = _create_test_image("face_a", brightness=120)
    ok, msg, stats = FaceAntiSpoofingHeuristic.evaluate_quality(good_img)
    assert ok


def test_burst_motion_liveness():
    """Test static image replay detection via frame delta."""
    img_a = _create_test_image("face_a", brightness=120)
    img_identical = _create_test_image("face_a", brightness=120)

    # Identical frames (delta == 0) -> static attack
    ok, msg, delta = FaceAntiSpoofingHeuristic.evaluate_burst_motion([img_a, img_identical])
    assert not ok
    assert "static image" in msg.lower() or "replay" in msg.lower()

    # Slight variation simulating natural micro-movement
    img_shifted = _create_test_image("face_a", brightness=124)
    ok, msg, delta = FaceAntiSpoofingHeuristic.evaluate_burst_motion([img_a, img_shifted])
    assert ok
    assert delta >= FaceAntiSpoofingHeuristic.MIN_FRAME_DELTA


def test_mock_face_engine_determinism():
    """Test deterministic mock engine."""
    engine = MockFaceEngine()
    img1 = _create_test_image("face_a")
    img2 = _create_test_image("face_a")
    img_diff = _create_test_image("face_b")

    emb1 = engine.extract_embedding(img1)
    emb2 = engine.extract_embedding(img2)
    emb_diff = engine.extract_embedding(img_diff)

    assert len(emb1) == 512
    assert len(emb2) == 512
    assert len(emb_diff) == 512

    # Same image yields similarity == 1.0
    sim_same = compute_cosine_similarity(emb1, emb2)
    assert pytest.approx(sim_same, abs=1e-4) == 1.0

    # Distinct pattern yields significantly lower similarity
    sim_diff = compute_cosine_similarity(emb1, emb_diff)
    assert sim_diff < 0.6


def test_biometric_service_verification_flow():
    """Test full enrollment, encryption, and 1:1 verification flow."""
    mock_engine = MockFaceEngine()
    service = BiometricService(engine=mock_engine)

    img_enrolled = _create_test_image("face_a")
    img_probe_matching = _create_test_image("face_a")
    img_probe_imposter = _create_test_image("face_b")

    # Enroll User 50
    enrolled_vec = mock_engine.extract_embedding(img_enrolled)
    encrypted_template = service.encryption.encrypt_vector(enrolled_vec, user_id=50)

    # 1. Matching probe
    probe_vec = mock_engine.extract_embedding(img_probe_matching)
    is_matched, score, threshold = service.verify_probe(probe_vec, encrypted_template, user_id=50)
    assert is_matched is True
    assert score >= threshold

    # 2. Imposter probe
    imposter_vec = mock_engine.extract_embedding(img_probe_imposter)
    is_matched, score, threshold = service.verify_probe(imposter_vec, encrypted_template, user_id=50)
    assert is_matched is False
    assert score < threshold


def test_inception_resnet_v1_engine_real_weights():
    """Verify production InceptionResnetV1FaceEngine with official VGGFace2 weights."""
    import math
    from services.biometric_service import InceptionResnetV1FaceEngine

    engine = InceptionResnetV1FaceEngine()
    assert engine.is_available() is True
    assert engine.version_tag == "facenet_vggface2_512d"

    img_a = _create_test_image("face_a")
    img_b = _create_test_image("face_b")

    emb_a = engine.extract_embedding(img_a)
    emb_b = engine.extract_embedding(img_b)

    # 1. Dimension and finite values
    assert len(emb_a) == 512
    assert len(emb_b) == 512
    assert all(math.isfinite(x) for x in emb_a)
    assert all(math.isfinite(x) for x in emb_b)

    # 2. L2 Normalization (unit vector)
    norm_a = math.sqrt(sum(x * x for x in emb_a))
    assert pytest.approx(norm_a, abs=1e-3) == 1.0

    # 3. Determinism for identical image
    emb_a_repeat = engine.extract_embedding(img_a)
    sim_same = compute_cosine_similarity(emb_a, emb_a_repeat)
    assert pytest.approx(sim_same, abs=1e-4) == 1.0

    # 4. Discrimination for distinct image
    sim_diff = compute_cosine_similarity(emb_a, emb_b)
    assert sim_diff < 0.95


def test_inception_resnet_v1_engine_cpu_fallback():
    """Verify InceptionResnetV1FaceEngine CPU fallback operates correctly."""
    import math
    from services.biometric_service import InceptionResnetV1FaceEngine

    engine_cpu = InceptionResnetV1FaceEngine(device="cpu")
    assert engine_cpu.device == "cpu"
    assert engine_cpu.is_available() is True

    img = _create_test_image("face_a")
    emb = engine_cpu.extract_embedding(img)
    assert len(emb) == 512
    assert all(math.isfinite(x) for x in emb)


def test_inception_resnet_v1_unavailable_raises_security_error():
    """Verify unavailable engine raises actionable BiometricSecurityError and never generates mock data."""
    from services.biometric_service import InceptionResnetV1FaceEngine

    engine = InceptionResnetV1FaceEngine()
    engine._model = None
    engine._init_error = "Test simulated missing weights file"

    assert engine.is_available() is False
    img = _create_test_image("face_a")
    with pytest.raises(BiometricSecurityError, match="Face recognition model is not loaded or weights are unavailable"):
        engine.extract_embedding(img)

