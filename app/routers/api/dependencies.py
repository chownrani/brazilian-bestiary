from app.database.connection import DBConnectionHandler
from app.repositories.criatura_repository import CriaturaRepository
from app.services.criatura_service import CriaturaService

def get_criatura_service() -> CriaturaService:
    conn = DBConnectionHandler()
    repo = CriaturaRepository(conn)
    return CriaturaService(repo)