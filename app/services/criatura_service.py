from app.schemas.criatura_schema import CriaturaCreate, CriaturaUpdate, CriaturaResponse
from app.exceptions.repository_exceptions import RepositoryError, EntityNotFoundError

class CriaturaService:
    def __init__(self, repository) -> None:
        self.__repo = repository

    async def create_criatura(self, criatura_data: CriaturaCreate) -> CriaturaResponse:
        try:
            criatura = await self.__repo.insert(criatura_data)
            return CriaturaResponse.model_validate(criatura)
        except RepositoryError as e:
            raise e
    
    async def get_all_criaturas(self) -> list[CriaturaResponse]:
        criaturas = await self.__repo.select_all()
        if not criaturas:
            raise EntityNotFoundError("Nenhuma criatura encontrada.")
        return [CriaturaResponse.model_validate(c) for c in criaturas]

    async def get_criatura_by_id(self, id: int) -> CriaturaResponse:
        criatura = await self.__repo.select_by_id(id)
        if not criatura:
            raise EntityNotFoundError(f"Criatura com ID '{id}' não encontrada.")
        return CriaturaResponse.model_validate(criatura)
    
    async def get_criatura_by_name(self, nome: str) -> CriaturaResponse:
        criatura = await self.__repo.select_by_name(nome)
        if not criatura:
            raise EntityNotFoundError(f"Criatura com nome '{nome}' não encontrada.")
        return CriaturaResponse.model_validate(criatura)
    
    async def update_criatura_by_id(self, id: int, update_data: CriaturaUpdate) -> CriaturaResponse:
        criatura = await self.__repo.update_by_id(id, update_data)
        if not criatura:
            raise EntityNotFoundError(f"Criatura com ID '{id}' não encontrada")
        return CriaturaResponse.model_validate(criatura)

    async def update_criatura_by_name(self, nome: str, update_data: CriaturaUpdate) -> CriaturaResponse:
        criatura = await self.__repo.update_by_name(nome, update_data)
        if not criatura:
            raise EntityNotFoundError(f"Criatura com nome '{nome}' não encontrada")
        return CriaturaResponse.model_validate(criatura)

    async def delete_criatura_by_id(self, id: int) -> None:
        await self.__repo.delete_by_id(id)

    async def delete_criatura_by_name(self, nome: str) -> None:
        await self.__repo.delete_by_name(nome)