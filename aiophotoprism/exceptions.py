"""Exceptions for the Photoprism REST API."""


class PhotoprismError(Exception):
    """Base Photoprism Exception class."""


class PhotoprismUnauthorizedError(PhotoprismError):
    """When the server does not accept the API token."""


class PhotoprismNotFoundError(PhotoprismError):
    """When the server responds with 404."""


class PhotoprismTimeoutError(PhotoprismError):
    """When request times out."""


class PhotoprismBadRequestError(PhotoprismError):
    """When the server responds with 400."""
