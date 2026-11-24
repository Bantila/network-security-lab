"""CLI interface for Network Security Lab.

Uses Click for argument parsing.
All commands delegate to core modules — no business logic here.
"""

import logging
import click

from network_security_lab import __version__
from network_security_lab.infrastructure.configuration.settings import settings

logger = logging.getLogger(__name__)


@click.group()
@click.version_option(__version__, prog_name="nsl")
@click.option(
    "--log-level",
    default="INFO",
    type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR"], case_sensitive=False),
    help="Logging verbosity level.",
    show_default=True,
)
def cli(log_level: str) -> None:
    """Network Security Lab — research tool for network security analysis.

    Study VPN, Proxy protocols and analyze network traffic in a controlled environment.
    """
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


@cli.command("info")
def cmd_info() -> None:
    """Show application information and configuration."""
    click.echo(f"Network Security Lab v{__version__}")
    click.echo(f"Data directory: {settings.data_dir}")
    click.echo(f"Log level: {settings.log_level}")
    click.echo()
    click.echo("Available command groups:")
    click.echo("  nsl network   — network diagnostics")
    click.echo("  nsl proxy     — proxy connections")
    click.echo("  nsl vpn       — VPN management")
    click.echo("  nsl capture   — traffic capture")
    click.echo("  nsl bench     — benchmarks and experiments")


@cli.group("network")
def network_group() -> None:
    """Network diagnostics and information."""


@network_group.command("status")
def network_status() -> None:
    """Show current network status (stub — implemented in Stage 2)."""
    click.echo("[Stage 2] Network status: not yet implemented.")
    click.echo("This command will show interfaces, IPs, and connectivity.")
