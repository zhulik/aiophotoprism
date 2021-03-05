"""Entrypoint for the Photoprism REST API."""

from .api import API


class Photoprism:
    """Entrypoint class."""

    def __init__(self, *args, **kwargs):
        """Initialize the client."""
        self._api = API(*args, **kwargs)

    def photos(self, **kwargs):
        """Get photos."""
        return self._api.request("/api/v1/photos", params=kwargs)

    async def close(self):
        """Close open client session."""
        await self._api.close()

    async def __aenter__(self):
        """Async enter."""
        return self

    async def __aexit__(self, *exc_info):
        """Async exit."""
        await self.close()
