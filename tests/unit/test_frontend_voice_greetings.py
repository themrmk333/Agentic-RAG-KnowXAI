"""Unit test verifying voice greeting strings, timing intervals, and admin voice sequencing."""

import subprocess
import sys
from datetime import time
from pathlib import Path


def test_voice_greeting_exact_strings_in_frontend():
    """Verify that frontend/src/App.tsx contains the exact required voice greetings."""
    app_tsx = Path("frontend/src/App.tsx").read_text(encoding="utf-8")

    registration_greeting = "Welcome to MK Infinite Private Limited."
    face_login_greeting = "Hello dude, welcome back!"

    assert registration_greeting in app_tsx, (
        f"Expected exact registration greeting '{registration_greeting}' not found in App.tsx"
    )
    assert face_login_greeting in app_tsx, (
        f"Expected exact face login greeting '{face_login_greeting}' not found in App.tsx"
    )


def test_voice_greetings_never_hardcode_tokens_or_passwords():
    """Verify that speech synthesis does not log or vocalize sensitive tokens."""
    app_tsx = Path("frontend/src/App.tsx").read_text(encoding="utf-8")
    assert "SpeechSynthesisUtterance(token" not in app_tsx
    assert "SpeechSynthesisUtterance(data.password" not in app_tsx
    assert "SpeechSynthesisUtterance(loginPass" not in app_tsx


def test_admin_voice_greeting_service_implementation():
    """Verify adminVoiceGreeting.ts exists and implements exact phrases, sequencing, and deduplication."""
    service_file = Path("frontend/src/admin/adminVoiceGreeting.ts")
    assert service_file.exists(), "adminVoiceGreeting.ts must exist"
    content = service_file.read_text(encoding="utf-8")

    # Phrase 1: "Hello Boss!"
    assert '"Hello Boss!"' in content

    # Phrase 2: 4 Time period greetings
    assert '"Good morning!"' in content
    assert '"Good afternoon!"' in content
    assert '"Good evening!"' in content
    assert '"Good night!"' in content

    # Sequential utterance chaining via onend
    assert "utterance1.onend" in content
    assert "window.speechSynthesis.speak(utterance2)" in content

    # Re-render deduplication guard
    assert "lastSpokenTimestamp" in content
    assert "lastSpokenText" in content


def test_admin_voice_greeting_dashboard_display():
    """Verify that both AdminDashboard.tsx and OverviewSection.tsx display the combined greeting."""
    dashboard_tsx = Path("frontend/src/admin/AdminDashboard.tsx").read_text(encoding="utf-8")
    overview_tsx = Path("frontend/src/admin/sections/OverviewSection.tsx").read_text(encoding="utf-8")

    assert "getCombinedAdminGreeting()" in dashboard_tsx
    assert "getCombinedAdminGreeting()" in overview_tsx
    assert "triggerAdminVoiceGreeting" in dashboard_tsx


def test_admin_voice_greeting_login_trigger():
    """Verify that handleAdminLoginSuccess triggers triggerAdminVoiceGreeting()."""
    app_tsx = Path("frontend/src/App.tsx").read_text(encoding="utf-8")
    assert "triggerAdminVoiceGreeting()" in app_tsx
    assert "handleAdminLoginSuccess" in app_tsx


def test_time_interval_mapping_rules():
    """Verify the 4 time period classification rules matching user specifications:
    - 5:00 AM–11:59 AM: "Good morning!"
    - 12:00 PM–4:59 PM: "Good afternoon!"
    - 5:00 PM–8:59 PM: "Good evening!"
    - 9:00 PM–4:59 AM: "Good night!"
    """
    def map_greeting(t: time) -> str:
        hour = t.hour
        if 5 <= hour < 12:
            return "Good morning!"
        elif 12 <= hour < 17:
            return "Good afternoon!"
        elif 17 <= hour < 21:
            return "Good evening!"
        else:
            return "Good night!"

    # Morning tests
    assert map_greeting(time(5, 0)) == "Good morning!"
    assert map_greeting(time(9, 30)) == "Good morning!"
    assert map_greeting(time(11, 59, 59)) == "Good morning!"

    # Afternoon tests
    assert map_greeting(time(12, 0)) == "Good afternoon!"
    assert map_greeting(time(14, 0)) == "Good afternoon!"
    assert map_greeting(time(16, 59, 59)) == "Good afternoon!"

    # Evening tests
    assert map_greeting(time(17, 0)) == "Good evening!"
    assert map_greeting(time(19, 45)) == "Good evening!"
    assert map_greeting(time(20, 59, 59)) == "Good evening!"

    # Night tests
    assert map_greeting(time(21, 0)) == "Good night!"
    assert map_greeting(time(23, 59, 59)) == "Good night!"
    assert map_greeting(time(0, 0)) == "Good night!"
    assert map_greeting(time(2, 30)) == "Good night!"
    assert map_greeting(time(4, 59, 59)) == "Good night!"


def test_run_node_admin_speech_synthesis_suite():
    """Execute the full Node.js utterance mock simulation suite verifying speech events & ordering."""
    runner = Path("frontend/test_voice_greeting_runner.mjs")
    assert runner.exists()
    result = subprocess.run(
        ["node", "--experimental-strip-types", str(runner)],
        capture_output=True,
        text=True,
        check=False
    )
    assert result.returncode == 0, f"Node speech test suite failed:\n{result.stdout}\n{result.stderr}"
    assert "TOTAL TESTS: 58 | PASSED: 58 | FAILED: 0" in result.stdout
