from unittest.mock import AsyncMock
from app.services.criatura_service import CriaturaService
import pytest_asyncio

@pytest_asyncio.fixture
def mock_repository():
    return AsyncMock()

@pytest_asyncio.fixture
def service(mock_repository):
    return CriaturaService(mock_repository)