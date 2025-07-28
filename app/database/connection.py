from app.database.base import Base
from app.config.settings import DATABASE_URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    """
        Classe que gerencia a conexão assíncrona do SQLAlchemy.

        Implementa a criação de uma AsyncEngine, além dos métodos contextuais
        '__aenter__' e '__aexit__' para possibilitar o uso assíncrono de 'with'
        nos repositories.

        O '__aenter__' inicia uma sessão assíncrona do SQLAlchemy e o '__aexit__'
        a fecha.
    """
    def __init__(self) -> None:
        self.__connection_string = DATABASE_URL
        self.__engine = self.__create_engine()
        self.session = None

    def __create_engine(self) -> AsyncEngine:
        engine = create_async_engine(self.__connection_string)
        return engine
    
    def get_engine(self) -> AsyncEngine:
        return self.__engine
    
    async def __aenter__(self) -> "DBConnectionHandler":
        async_session = sessionmaker(
            bind=self.__engine,
            class_=AsyncSession,
            expire_on_commit=False
        )
        self.session = async_session()
        async with self.__engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        return self
    
    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.session.close()
    