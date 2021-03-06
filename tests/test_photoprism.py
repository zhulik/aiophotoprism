"""Tests for Photoprism."""

import pytest
from expects import be_a, expect

from aiophotoprism import Photoprism

@pytest.mark.asyncio
async def test_initialization():
    expect(Photoprism("username", "password")).to(be_a(Photoprism))
