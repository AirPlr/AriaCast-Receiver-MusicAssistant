"""Metadata handler for AriaCast protocol."""

from __future__ import annotations

from typing import Any


class MetadataHandler:
    """Handle metadata updates for AriaCast streams."""

    def __init__(self) -> None:
        """Initialize metadata handler."""
        self.current_metadata: dict[str, Any] = {
            "title": None,
            "artist": None,
            "album": None,
            "artwork_url": None,
            "duration_ms": None,
            "position_ms": None,
            "is_playing": False,
        }

    def update(self, metadata: dict[str, Any]) -> None:
        """Update current metadata with new values.
        
        Args:
            metadata: Dictionary containing metadata updates
        """
        for key in ["title", "artist", "album", "artwork_url", "duration_ms", "position_ms", "is_playing"]:
            if key in metadata and metadata[key] is not None:
                self.current_metadata[key] = metadata[key]

    def clear(self) -> None:
        """Clear all metadata."""
        self.current_metadata = {
            "title": None,
            "artist": None,
            "album": None,
            "artwork_url": None,
            "duration_ms": None,
            "position_ms": None,
            "is_playing": False,
        }

    def get(self) -> dict[str, Any]:
        """Get current metadata.
        
        Returns:
            Dictionary containing current metadata
        """
        return self.current_metadata.copy()
