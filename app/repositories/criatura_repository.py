from app.models.criatura import Criatura
from app.exceptions.repository_exceptions import RepositoryError, EntityNotFoundError
from app.exceptions.logger import logger
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy import select
from app.schemas.criatura_schema import CriaturaCreate, CriaturaUpdate

class CriaturaRepository:
    def __init__(self, db_connection_handler) -> None:
        self.__conn = db_connection_handler

    async def insert(self, criatura_data: CriaturaCreate) -> Criatura:
        async with self.__conn as db:
            try:
                criatura = Criatura(
                    nome=criatura_data.nome,
                    regiao=criatura_data.regiao.value,
                    periculosidade=criatura_data.periculosidade,
                    lenda=criatura_data.lenda
                )
                db.session.add(criatura)
                await db.session.commit()
                await db.session.refresh(criatura)
                return criatura
            except IntegrityError:
                await db.session.rollback()
                raise RepositoryError("Erro ao inserir criatura. Já existe uma criatura com esse nome.")
            except SQLAlchemyError as e:
                await db.session.rollback()
                logger.error(f"Erro ao inserir criatura: {e}")
                raise RepositoryError("Erro ao salvar criatura no banco de dados.")

    async def select_all(self) -> list[Criatura]:
        async with self.__conn as db:
            try:
                query = select(Criatura)
                response = await db.session.execute(query)
                criaturas = response.scalars().all()
                if not criaturas:
                    return []
                return criaturas
            except SQLAlchemyError as e:
                logger.error(f"Erro ao buscar criaturas.")
                raise RepositoryError("Erro ao acessar banco de dados.")

    async def select_by_id(self, id: int) -> Criatura:
        async with self.__conn as db:
            try:
                query = select(Criatura).where(Criatura.id == id)
                response = await db.session.execute(query)
                criatura = response.scalar_one_or_none()
                if not criatura:
                    raise EntityNotFoundError(f"Criatura com ID '{id}' não encontrada.")
                return criatura
            except SQLAlchemyError as e:
                logger.error(f"Erro ao buscar criatura por ID: {e}")
                raise RepositoryError("Erro ao acessar banco de dados")
            
    async def select_by_name(self, nome: str) -> Criatura:
        async with self.__conn as db:
            try:
                query = select(Criatura).where(Criatura.nome == nome)
                response = await db.session.execute(query)
                criatura = response.scalar_one_or_none()
                if not criatura:
                    raise EntityNotFoundError(f"Criatura com nome '{nome}' não encontrada.")
                return criatura
            except SQLAlchemyError as e:
                logger.error(f"Erro ao buscar criatura por nome: {e}")
                raise RepositoryError("Erro ao acessar banco de dados")

    async def update_by_id(self, id: int, update_data: CriaturaUpdate) -> Criatura:
        async with self.__conn as db:
            try:
                query = select(Criatura).where(Criatura.id == id)
                response = await db.session.execute(query)
                criatura = response.scalar_one_or_none()
                if not criatura:
                    raise EntityNotFoundError(f"Criatura com ID '{id}' não encontrada.")
                for field, value in update_data.model_dump(exclude_unset=True).items():
                    setattr(criatura, field, value)
                await db.session.commit()
                await db.session.refresh(criatura)
                return criatura
            except IntegrityError:
                await db.session.rollback()
                raise RepositoryError("Já existe uma criatura com esse nome.")
            except SQLAlchemyError as e:
                await db.session.rollback()
                raise RepositoryError(f"Erro ao acessar banco de dados e atualizar criatura: {e}")
            
    async def update_by_name(self, nome: str, update_data: CriaturaUpdate) -> Criatura:
        async with self.__conn as db:
            try:
                query = select(Criatura).where(Criatura.nome == nome)
                response = await db.session.execute(query)
                criatura = response.scalar_one_or_none()
                if not criatura:
                    raise EntityNotFoundError(f"Criatura com nome '{nome}' não encontrada.")
                for field, value in update_data.model_dump(exclude_unset=True).items():
                    setattr(criatura, field, value)
                await db.session.commit()
                await db.session.refresh(criatura)
                return criatura
            except IntegrityError:
                await db.session.rollback()
                raise RepositoryError("Já existe uma criatura com esse nome.")
            except SQLAlchemyError as e:
                await db.session.rollback()
                raise RepositoryError(f"Erro ao acessar banco de dados e atualizar criatura: {e}")

    async def delete_by_id(self, id: int) -> None:
        async with self.__conn as db:
            try:
                query = select(Criatura).where(Criatura.id == id)
                response = await db.session.execute(query)
                criatura = response.scalar_one_or_none()
                if not criatura:
                    raise EntityNotFoundError(f"Criatura com ID '{id}' não encontrada.")
                await db.session.delete(criatura)
                await db.session.commit()
            except SQLAlchemyError as e:
                await db.session.rollback()
                raise RepositoryError(f"Erro ao acessar banco de dados e deletar criatura: {e}")
            
    async def delete_by_name(self, nome: str) -> None:
        async with self.__conn as db:
            try:
                query = select(Criatura).where(Criatura.nome == nome)
                response = await db.session.execute(query)
                criatura = response.scalar_one_or_none()
                if not criatura:
                    raise EntityNotFoundError(f"Criatura com nome '{nome}' não encontrada.")
                await db.session.delete(criatura)
                await db.session.commit()
            except SQLAlchemyError as e:
                await db.session.rollback()
                raise RepositoryError(f"Erro ao acessar banco de dados e deletar criatura: {e}")

    
