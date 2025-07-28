class RepositoryError(Exception):
    pass

class EntityNotFoundError(RepositoryError):
    def __init__(self, message: str = "Entidade não encontrada") -> None:
        super().__init__(message)