"""Tests for CLI commands."""

import pytest
from click.testing import CliRunner
from network_security_lab.cli.main import cli
from network_security_lab import __version__


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


def test_version(runner: CliRunner) -> None:
    """nsl --version must print correct version."""
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.output


def test_info_command(runner: CliRunner) -> None:
    """nsl info must list available command groups."""
    result = runner.invoke(cli, ["info"])
    assert result.exit_code == 0
    assert "Network Security Lab" in result.output
    assert "nsl network" in result.output


def test_network_status_stub(runner: CliRunner) -> None:
    """nsl network status is a stub in Stage 1."""
    result = runner.invoke(cli, ["network", "status"])
    assert result.exit_code == 0
    assert "Stage 2" in result.output
