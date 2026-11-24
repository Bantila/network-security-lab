"""Tests for application configuration."""

import pytest
from pathlib import Path
from network_security_lab.infrastructure.configuration.settings import AppSettings


def test_settings_creates_data_dir(tmp_path: Path) -> None:
    """AppSettings must create data_dir on initialisation."""
    target = tmp_path / "nsl_test"
    s = AppSettings(data_dir=target)
    assert target.exists()


def test_settings_creates_subdirs(tmp_path: Path) -> None:
    """AppSettings must create captures and exports subdirectories."""
    s = AppSettings(data_dir=tmp_path / "nsl_test")
    assert (s.data_dir / "captures").exists()
    assert (s.data_dir / "exports").exists()


def test_settings_default_log_level(tmp_path: Path) -> None:
    """Default log level is INFO."""
    s = AppSettings(data_dir=tmp_path / "nsl_test")
    assert s.log_level == "INFO"
