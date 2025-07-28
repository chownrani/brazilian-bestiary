from app.repositories.criatura_repository import CriaturaRepository
from app.models.criatura import Criatura
from app.schemas.criatura_schema import CriaturaCreate, CriaturaUpdate
from app.exceptions.repository_exceptions import EntityNotFoundError
from tests.repositories.conftest import mock_db_connection
import pytest

@pytest.mark.asyncio
async def test_insert(mock_db_connection):
    """
    1. Mockando a conexão e a sessão do banco de dados para passar como
    argumento na instância do repositório

    2. Criando uma criatura fake para simular o retorno do session.refresh
    no insert do repositório
    
    3. Chamando o método insert do repositório e verificando se o retorno é 
    Criatura e se todos os métodos foram chamados
    """
    mock_conn, mock_session, _, _ = mock_db_connection
    repo = CriaturaRepository(mock_conn)

    criatura = Criatura(id=1, nome="Curupira", regiao="Norte", periculosidade=4, lenda="Protetor das florestas.")

    data = CriaturaCreate(nome="Curupira", regiao="Norte", periculosidade=4, lenda="Protetor das florestas.")
    mock_session.refresh.return_value = criatura

    response = await repo.insert(data)

    assert isinstance(response, Criatura)
    assert response.nome == "Curupira"
    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once()

@pytest.mark.asyncio
async def test_select_all(mock_db_connection):
    """
    1. Mockando o mock_scalars para simular seu retorno no método select
    2. Verificando o retorno
    """
    mock_conn, mock_session, _, mock_scalars = mock_db_connection
    repo = CriaturaRepository(mock_conn)

    mock_scalars.all.return_value = [Criatura(id=1, nome="Curupira", regiao="Norte", periculosidade=4, lenda="Lenda")]
    
    response = await repo.select_all()

    assert isinstance(response, list)
    assert len(response) == 1
    assert response[0].nome == "Curupira"
    mock_session.execute.assert_called_once()

@pytest.mark.asyncio
async def test_select_by_id_and_name(mock_db_connection):
    """
    Testando a chamada de 'select' pelo ID e pelo nome, além da busca sem resultados
    """
    mock_conn, mock_session, mock_result, _ = mock_db_connection
    repo = CriaturaRepository(mock_conn)

    criatura = Criatura(id=1, nome="Curupira", regiao="Norte", periculosidade=4, lenda="Lenda")
    mock_result.scalar_one_or_none.return_value = criatura

    response = await repo.select_by_id(1)
    assert isinstance(response, Criatura)
    assert response.id == 1
    mock_session.execute.assert_called()

    response = await repo.select_by_name("Curupira")
    assert response.nome == "Curupira"

    mock_result.scalar_one_or_none.return_value = None
    with pytest.raises(EntityNotFoundError):
        await repo.select_by_id(999)


@pytest.mark.asyncio
async def test_update_by_id_and_name(mock_db_connection):
    mock_conn, mock_session, mock_result, _ = mock_db_connection
    repo = CriaturaRepository(mock_conn)

    criatura = Criatura(id=1, nome="Curupira", regiao="Norte", periculosidade=4, lenda="Lenda")
    mock_result.scalar_one_or_none.return_value = criatura

    update_data = CriaturaUpdate(periculosidade=5)

    updated = await repo.update_by_id(1, update_data)
    assert updated.periculosidade == 5
    mock_session.commit.assert_called()
    mock_session.refresh.assert_called()

    updated = await repo.update_by_name("Curupira", update_data)
    assert updated.periculosidade == 5

    # Caso: criatura não encontrada
    mock_result.scalar_one_or_none.return_value = None
    with pytest.raises(EntityNotFoundError):
        await repo.update_by_id(999, update_data)


@pytest.mark.asyncio
async def test_delete_by_id_and_name(mock_db_connection):
    mock_conn, mock_session, mock_result, _ = mock_db_connection
    repo = CriaturaRepository(mock_conn)

    criatura = Criatura(id=1, nome="Curupira", regiao="Norte", periculosidade=4, lenda="Lenda")
    mock_result.scalar_one_or_none.return_value = criatura

    await repo.delete_by_id(1)
    mock_session.delete.assert_called_with(criatura)
    mock_session.commit.assert_called()

    await repo.delete_by_name("Curupira")
    mock_session.delete.assert_called()

    mock_result.scalar_one_or_none.return_value = None
    with pytest.raises(EntityNotFoundError):
        await repo.delete_by_id(999)
