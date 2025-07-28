from unittest.mock import AsyncMock
from httpx import AsyncClient, ASGITransport
from app.routers.routes.criatura_routes import router
from app.routers.api.api import create_app
from app.routers.api.dependencies import get_criatura_service
import pytest_asyncio

@pytest_asyncio.fixture
def criatura():
    return {
        "id": 1,
        "nome": "Curupira",
        "regiao": "Norte",
        "periculosidade": 4,
        "lenda": "Protetor das florestas"
    }

@pytest_asyncio.fixture
def criatura_update():
    return {
        "id": 1,
        "nome": "Curupira",
        "regiao": "Norte",
        "periculosidade": 4,
        "lenda": "Protetor das florestas, atualizado"
    }

@pytest_asyncio.fixture
def mock_service(criatura, criatura_update):
    service = AsyncMock()
    service.create_criatura.return_value = criatura
    service.get_all_criaturas.return_value = [criatura]
    service.get_criatura_by_id.return_value = criatura
    service.get_criatura_by_name.return_value = criatura
    service.update_criatura_by_id.return_value = criatura_update
    service.update_criatura_by_name.return_value = criatura_update
    service.delete_criatura_by_id.return_value = None
    service.delete_criatura_by_name.return_value = None
    return service

@pytest_asyncio.fixture
async def client(mock_service):
    app = create_app()
    app.include_router(router)
    app.dependency_overrides[get_criatura_service] = lambda: mock_service
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac