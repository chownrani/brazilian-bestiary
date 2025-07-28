from app.database.base import Base
from sqlalchemy import Column, Integer, String, Text

class Criatura(Base):
    __tablename__ = "criaturas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), unique=True, nullable=False, index=True)
    regiao = Column(String(20), nullable=False, index=True)
    periculosidade = Column(Integer, nullable=False)
    lenda = Column(Text, nullable=False)

    def __repr__(self) -> str:
        return f"<Criatura(nome='{self.nome}', regiao='{self.regiao}', periculosidade={self.periculosidade})>"
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "regiao": self.regiao,
            "periculosidade": self.periculosidade,
            "lenda": self.lenda
        }