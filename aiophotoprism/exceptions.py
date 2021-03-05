"""Exceptions for the Photoprism REST API."""


class PhotoprismError(Exception):
    """Base Photoprism Exception class."""


class UnauthorizedError(PhotoprismError):
    """When the server does not accept the API token."""


class NotFoundError(PhotoprismError):
    """When the server responds with 404."""
