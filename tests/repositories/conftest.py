from unittest.mock import AsyncMock, Mock
import pytest_asyncio

@pytest_asyncio.fixture
async def mock_db_connection() -> AsyncMock:
    """
    1. Mockando o DBConnectionHandler e sua sessão
    2. Definindo os métodos do SQLAlchemy como síncronos ou assíncronos conforme
    necessário para evitar inconsistências com os métodos reais
    """
    mock_conn = AsyncMock()
    mock_session = AsyncMock()
    mock_conn.__aenter__.return_value = mock_conn
    mock_conn.session = mock_session

    # Métodos síncronos
    mock_session.add = Mock()
    mock_session.add.return_value = None
    mock_session.delete = AsyncMock()
    mock_session.refresh = AsyncMock()

    # Métodos assíncronos
    mock_session.commit = AsyncMock()
    mock_session.execute = AsyncMock()

    # Resultado padrão para execute()
    mock_result = Mock()
    mock_scalars = Mock()
    mock_scalars.all.return_value = []  # lista vazia por padrão
    mock_result.scalars.return_value = mock_scalars
    mock_session.execute.return_value = mock_result

    return mock_conn, mock_session, mock_result, mock_scalars


