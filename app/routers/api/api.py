from fastapi import FastAPI
from app.routers.routes.criatura_routes import router as criaturas_routes

def create_app() -> FastAPI:
    app = FastAPI(title="Bestiário Brasileiro")
    app.include_router(criaturas_routes)
    return app

