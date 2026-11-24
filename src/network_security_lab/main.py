"""Entry point for the Network Security Lab application."""

import sys
import logging
from network_security_lab.cli.main import cli


def setup_logging(level: str = "INFO") -> None:
    """Configure application-wide logging."""
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def main() -> None:
    """Main entry point."""
    setup_logging()
    cli()


if __name__ == "__main__":
    main()
