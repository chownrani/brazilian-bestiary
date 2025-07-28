from app.models.criatura import Criatura
from app.exceptions.repository_exceptions import RepositoryError, EntityNotFoundError
from app.schemas.criatura_schema import CriaturaCreate, CriaturaUpdate
import pytest

@pytest.mark.asyncio
async def test_create_criatura_success(service, mock_repository):
    criatura = Criatura(id=1, nome="Curupira", regiao="Norte", periculosidade=4, lenda="Protetor das florestas")
    mock_repository.insert.return_value = criatura

    data = CriaturaCreate(nome="Curupira", regiao="Norte", periculosidade=4, lenda="Protetor das florestas")
    response = await service.create_criatura(data)

    assert response.nome == "Curupira"
    mock_repository.insert.assert_awaited_once_with(data)

@pytest.mark.asyncio
async def test_create_criatura_failure(service, mock_repository):
    mock_repository.insert.side_effect = RepositoryError("Erro no banco")

    data = CriaturaCreate(
        nome="Falha",
        regiao="Norte",
        periculosidade=3,
        lenda="Essa é uma lenda qualquer que é longa o suficiente."
    )

    with pytest.raises(RepositoryError):
        await service.create_criatura(data)

    mock_repository.insert.assert_awaited_once_with(data)

@pytest.mark.asyncio
async def test_get_all_criaturas_success(service, mock_repository):
    criaturas = [Criatura(id=1, nome="Curupira", regiao="Norte", periculosidade=4, lenda="Protetor das florestas")]
    mock_repository.select_all.return_value = criaturas

    result = await service.get_all_criaturas()

    assert len(result) == 1
    assert result[0].nome == "Curupira"
    mock_repository.select_all.assert_awaited_once()

@pytest.mark.asyncio
async def test_get_all_criaturas_empty(service, mock_repository):
    mock_repository.select_all.return_value = []
    with pytest.raises(EntityNotFoundError):
        await service.get_all_criaturas()

@pytest.mark.asyncio
async def test_get_criatura_by_id_success(service, mock_repository):
    criatura = Criatura(id=1, nome="Curupira", regiao="Norte", periculosidade=4, lenda="Protetor das florestas")
    mock_repository.select_by_id.return_value = criatura

    result = await service.get_criatura_by_id(1)

    assert result.nome == "Curupira"
    mock_repository.select_by_id.assert_awaited_once_with(1)

@pytest.mark.asyncio
async def test_get_criatura_by_id_not_found(service, mock_repository):
    mock_repository.select_by_id.side_effect = EntityNotFoundError("Não encontrada")
    with pytest.raises(EntityNotFoundError):
        await service.get_criatura_by_id(999)

@pytest.mark.asyncio
async def test_update_criatura_by_id_success(service, mock_repository):
    criatura = Criatura(id=1, nome="Curupira Atualizado", regiao="Norte", periculosidade=5, lenda="Protetor das florestas, atualizado.")
    mock_repository.update_by_id.return_value = criatura
    data = CriaturaUpdate(periculosidade=5)

    result = await service.update_criatura_by_id(1, data)

    assert result.periculosidade == 5
    mock_repository.update_by_id.assert_awaited_once_with(1, data)

@pytest.mark.asyncio
async def test_update_criatura_by_id_not_found(service, mock_repository):
    mock_repository.update_by_id.side_effect = EntityNotFoundError("Não encontrada")
    data = CriaturaUpdate(periculosidade=5)
    with pytest.raises(EntityNotFoundError):
        await service.update_criatura_by_id(999, data)

@pytest.mark.asyncio
async def test_delete_criatura_by_id_success(service, mock_repository):
    await service.delete_criatura_by_id(1)
    mock_repository.delete_by_id.assert_awaited_once_with(1)