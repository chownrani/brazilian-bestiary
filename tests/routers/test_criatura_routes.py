from app.schemas.criatura_schema import CriaturaUpdate
import pytest

@pytest.mark.asyncio
async def test_create_criatura(client, mock_service, criatura):
    payload = criatura
    response = await client.post("/criaturas/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Curupira"
    mock_service.create_criatura.assert_awaited_once()

@pytest.mark.asyncio
async def test_get_all_criaturas(client, mock_service):
    response = await client.get("/criaturas/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["nome"] == "Curupira"
    mock_service.get_all_criaturas.assert_awaited_once()

@pytest.mark.asyncio
async def test_get_criatura_by_id_and_name(client, mock_service, criatura):
    response = await client.get(f"/criaturas/id/{criatura['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == criatura["id"]
    mock_service.get_criatura_by_id.assert_awaited_once_with(criatura["id"])

    # By NAME
    response = await client.get(f"/criaturas/nome/{criatura['nome']}")
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == criatura["nome"]
    mock_service.get_criatura_by_name.assert_awaited_once_with(criatura["nome"])

@pytest.mark.asyncio
async def test_update_criatura_by_id_and_name(client, mock_service, criatura_update):
    update_data = criatura_update

    response = await client.put(f"/criaturas/id/{criatura_update['id']}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["lenda"] == "Protetor das florestas, atualizado"
    mock_service.update_criatura_by_id.assert_awaited_once()
    args, kwargs = mock_service.update_criatura_by_id.await_args
    assert args[0] == criatura_update["id"]
    assert isinstance(args[1], CriaturaUpdate)
    assert args[1].lenda == "Protetor das florestas, atualizado"

    response = await client.put(f"/criaturas/nome/{criatura_update['nome']}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["lenda"] == "Protetor das florestas, atualizado"
    mock_service.update_criatura_by_name.assert_awaited_once()
    args, kwargs = mock_service.update_criatura_by_name.await_args
    assert args[0] == criatura_update["nome"]
    assert isinstance(args[1], CriaturaUpdate)
    assert args[1].lenda == "Protetor das florestas, atualizado"

@pytest.mark.asyncio
async def test_delete_criatura_by_id_and_name(client, mock_service, criatura):
    response = await client.delete(f"/criaturas/id/{criatura['id']}")
    assert response.status_code == 204
    mock_service.delete_criatura_by_id.assert_awaited_once_with(criatura["id"])

    response = await client.delete(f"/criaturas/nome/{criatura['nome']}")
    assert response.status_code == 204
    mock_service.delete_criatura_by_name.assert_awaited_once_with(criatura["nome"])
