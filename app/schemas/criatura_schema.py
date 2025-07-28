from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

class RegiaoEnum(str, Enum):
    norte = "Norte"
    nordeste = "Nordeste"
    centro_oeste = "Centro-Oeste"
    sudeste = "Sudeste"
    sul = "Sul"

class CriaturaCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=50, description="Nome da criatura")
    regiao: RegiaoEnum
    periculosidade: int = Field(..., ge=1, le=5, description="Nível de periculosidade da criatura(1 a 5)")
    lenda: str = Field(..., min_length=20, max_length=5000, description="História ou lenda associada à criatura")

class CriaturaUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=2, max_length=50)
    regiao: Optional[RegiaoEnum] = None
    periculosidade: Optional[int] = Field(None, ge=1, le=5)
    lenda: Optional[str] = Field(None, min_length=20)

class CriaturaResponse(CriaturaCreate):
    id: int
    
    model_config = {
        "from_attributes": True
    }