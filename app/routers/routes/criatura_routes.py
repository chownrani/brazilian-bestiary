from fastapi import APIRouter, Depends
from app.routers.api.dependencies import get_criatura_service
from app.schemas.criatura_schema import CriaturaCreate, CriaturaResponse, CriaturaUpdate
from app.services.criatura_service import CriaturaService

router = APIRouter(prefix="/criaturas", tags=["Criaturas"])

@router.post("/", response_model=CriaturaResponse)
async def create_criatura(criatura_data: CriaturaCreate, service: CriaturaService = Depends(get_criatura_service)):
    return await service.create_criatura(criatura_data)

@router.get("/", response_model=list[CriaturaResponse])
async def list_criaturas(service: CriaturaService = Depends(get_criatura_service)):
    return await service.get_all_criaturas()

@router.get("/id/{id}", response_model=CriaturaResponse)
async def get_criatura_by_id(id: int, service: CriaturaService = Depends(get_criatura_service)):
    return await service.get_criatura_by_id(id)

@router.get("/nome/{nome}", response_model=CriaturaResponse)
async def get_criatura_by_name(nome: str, service: CriaturaService = Depends(get_criatura_service)):
    return await service.get_criatura_by_name(nome)

@router.put("/id/{id}", response_model=CriaturaResponse)
async def update_criatura_by_id(id: int, update_data: CriaturaUpdate, service: CriaturaService = Depends(get_criatura_service)):
    return await service.update_criatura_by_id(id, update_data)

@router.put("/nome/{nome}", response_model=CriaturaResponse)
async def update_criatura_by_name(nome: str, update_data: CriaturaUpdate, service: CriaturaService = Depends(get_criatura_service)):
    return await service.update_criatura_by_name(nome, update_data)

@router.delete("/id/{id}", status_code=204)
async def delete_criatura_by_id(id: int, service: CriaturaService = Depends(get_criatura_service)):
    await service.delete_criatura_by_id(id)

@router.delete("/nome/{nome}", status_code=204)
async def delete_criatura_by_name(nome: str, service: CriaturaService = Depends(get_criatura_service)):
    await service.delete_criatura_by_name(nome)