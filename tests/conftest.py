"""Test helper functions."""

import pytest
from aioresponses import aioresponses as responses

from aiophotoprism import Photoprism


@pytest.fixture
async def photoprism_client():
    """Yield a Photoprism client."""
    async with Photoprism("token") as client:
        yield client


@pytest.fixture
def aioresponses():
    """Yield aioresponses."""
    with responses() as m:
        yield m
