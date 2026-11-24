"""Application configuration management."""

import os
import logging
from dataclasses import dataclass, field
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class AppSettings:
    """Central application configuration.
    
    Uses environment variables with sensible defaults.
    No secrets are stored here — only paths and runtime options.
    """

    # Directories
    data_dir: Path = field(
        default_factory=lambda: Path(
            os.environ.get("NSL_DATA_DIR", Path.home() / ".network-security-lab")
        )
    )
    log_level: str = field(
        default_factory=lambda: os.environ.get("NSL_LOG_LEVEL", "INFO")
    )

    def __post_init__(self) -> None:
        """Create required directories on startup."""
        self.data_dir.mkdir(parents=True, exist_ok=True)
        (self.data_dir / "captures").mkdir(exist_ok=True)
        (self.data_dir / "exports").mkdir(exist_ok=True)
        logger.debug("Data directory: %s", self.data_dir)


# Singleton — импортируй отсюда, не создавай новый экземпляр
settings = AppSettings()
