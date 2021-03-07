"""Tests for Photoprism."""

import pytest
from aiophotoprism import Photoprism
from expects import be_a, expect


@pytest.mark.asyncio
async def test_initialization():
    """Test initialization."""
    expect(Photoprism("username", "password")).to(be_a(Photoprism))
