"""Entrypoint for the Photoprism REST API."""

import aiohttp

from .api import API
from .exceptions import PhotoprismBadRequestError, PhotoprismTimeoutError


class Photoprism:
    """Entrypoint class."""

    def __init__(self, *args, **kwargs):
        """Initialize the client."""
        self._api = API(*args, **kwargs)

    async def photos(self, **kwargs):
        """Get photos."""
        return await self._api.request("/api/v1/photos", params=kwargs)

    async def config(self):
        """Get config."""
        return await self._api.request("/api/v1/config")

    async def index(self):
        """Start indexing."""
        try:
            await self._api.request(
                "/api/v1/index",
                method="POST",
                data={"rescan": False},
                timeout=aiohttp.ClientTimeout(total=1),
            )
        # The request always times out, but the indexing starts, so ignoring timeout error.
        except PhotoprismTimeoutError:
            pass
        # The index is already in progress
        except PhotoprismBadRequestError:
            pass

    async def close(self):
        """Close open client session."""
        await self._api.close()

    async def __aenter__(self):
        """Async enter."""
        return self

    async def __aexit__(self, *exc_info):
        """Async exit."""
        await self.close()
