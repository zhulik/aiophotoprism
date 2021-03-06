"""Low level client for the Photoprism REST API."""

import asyncio

import aiohttp
from yarl import URL

from .dictobject import dictobject
from .exceptions import (
    PhotoprismBadRequestError,
    PhotoprismError,
    PhotoprismNotFoundError,
    PhotoprismTimeoutError,
    PhotoprismUnauthorizedError,
)


class API:
    """Low level client."""

    DEFAULT_TIMEOUT = 10

    def __init__(
        self,
        username,
        password,
        url="http://127.0.0.1:2342",
        timeout=DEFAULT_TIMEOUT,
        verify_ssl=True,
        loop=None,
        session=None,
    ):
        """Initialize the client."""
        self._username = username
        self._password = password
        self._url = URL(url)
        self._timeout = aiohttp.ClientTimeout(total=timeout)
        self._verify_ssl = verify_ssl
        self._session_id = None

        self._loop = loop or asyncio.get_event_loop()
        self._session = session
        self._close_session = False

        if self._session is None:
            self._session = aiohttp.ClientSession(loop=self._loop)
            self._close_session = True

    async def request(self, *args, **kwargs):
        """Perform request with error wrapping and authentication."""
        try:
            if "headers" in kwargs:
                kwargs["headers"] = {
                    **{"X-Session-ID": await self.session_id()},
                    **kwargs["headers"],
                }
            else:
                kwargs["headers"] = {"X-Session-ID": await self.session_id()}
            return dictobject(await self.raw_request(*args, **kwargs))
        except aiohttp.client_exceptions.ClientResponseError as error:
            if error.status in [401, 403]:
                raise PhotoprismUnauthorizedError from error
            if error.status == 404:
                raise PhotoprismNotFoundError from error
            if error.status == 400:
                raise PhotoprismBadRequestError from error
            raise PhotoprismError from error
        except asyncio.exceptions.TimeoutError as error:
            raise PhotoprismTimeoutError from error
        except Exception as error:
            raise PhotoprismError from error

    async def raw_request(
        self, uri, params=None, data=None, headers=None, method="GET", timeout=None
    ):
        """Perform request."""
        timeout = timeout or self._timeout
        headers = headers or {}
        async with self._session.request(
            method,
            self._url.join(URL(uri)).update_query(params),
            json=data,
            headers={**{"Accept": "application/json"}, **headers},
            timeout=timeout,
            verify_ssl=self._verify_ssl,
        ) as response:
            response.raise_for_status()
            if (
                "Content-Type" in response.headers
                and "application/json" in response.headers["Content-Type"]
            ):
                return await response.json()
            return await response.read()

    async def close(self):
        """Close the session."""
        if self._session and self._close_session:
            await self._session.close()

    async def session_id(self):
        """Authenticate and return a session id."""
        if self._session_id is None:
            self._session_id = (
                await self.raw_request(
                    "api/v1/session",
                    data={"username": self._username, "password": self._password},
                    method="POST",
                )
            )["id"]
        return self._session_id
