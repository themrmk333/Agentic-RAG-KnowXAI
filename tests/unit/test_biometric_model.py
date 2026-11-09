"""Unit tests for BiometricCredential SQLAlchemy model and settings configuration."""

import pytest
from datetime import datetime, timezone
from sqlalchemy import select
from database.connection import SessionLocal
from database.models import User, BiometricCredential
from config.settings import get_settings


def test_biometric_settings_configuration():
    """Verify biometric settings defaults and types."""
    settings = get_settings()
    assert settings.biometric_encryption_key is not None
    assert len(settings.biometric_encryption_key.get_secret_value()) >= 16
    assert isinstance(settings.face_similarity_threshold, float)
    assert 0.0 < settings.face_similarity_threshold < 1.0


def test_biometric_credential_model_lifecycle():
    """Test creation, relationship, and cascade deletion of BiometricCredential."""
    test_email = f"bio_test_{int(datetime.now().timestamp())}@mk-infinite.ai"
    test_emp_id = f"EMP_BIO_{int(datetime.now().timestamp()) % 100000}"

    with SessionLocal() as session:
        # Create user
        user = User(
            email=test_email,
            username=test_email.split("@")[0],
            full_name="Biometric Test Subject",
            employee_id=test_emp_id,
            department="IT Support",
            role="Employee",
            auth_provider="local",
        )
        session.add(user)
        session.commit()
        session.refresh(user)

        user_id = user.id
        assert user_id is not None
        assert user.auth_provider == "local"

        # Create BiometricCredential linked to user
        mock_encrypted_payload = "ENC_AES256GCM_MOCK_PAYLOAD_V1"
        bio = BiometricCredential(
            user_id=user.id,
            encrypted_template=mock_encrypted_payload,
            template_version="v1_mobilenet_512d",
            is_enabled=True,
            failed_attempts=0,
        )
        session.add(bio)
        session.commit()
        session.refresh(bio)

        assert bio.id is not None
        assert bio.user_id == user_id
        assert bio.encrypted_template == mock_encrypted_payload
        assert bio.is_enabled is True
        assert bio.failed_attempts == 0

        # Verify relationship from User to BiometricCredential
        session.refresh(user)
        assert user.biometric_credential is not None
        assert user.biometric_credential.id == bio.id

        # Verify query by user_id
        fetched_bio = session.execute(
            select(BiometricCredential).where(BiometricCredential.user_id == user_id)
        ).scalar_one_or_none()
        assert fetched_bio is not None
        assert fetched_bio.encrypted_template == mock_encrypted_payload

        # Test CASCADE deletion when user is deleted
        session.delete(user)
        session.commit()

        # BiometricCredential should be deleted via ON DELETE CASCADE
        orphaned_bio = session.execute(
            select(BiometricCredential).where(BiometricCredential.user_id == user_id)
        ).scalar_one_or_none()
        assert orphaned_bio is None
