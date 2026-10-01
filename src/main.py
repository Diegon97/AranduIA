"""
Punto de Entrada Principal de AranduIA (FastAPI Server).
Monta las APIs del Tutor, Docente, Gateway WhatsApp, Sincronización y la interfaz PWA.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from src.config import settings
from src.api.tutor_routes import router as tutor_router
from src.api.docente_routes import router as docente_router
from src.api.whatsapp_routes import router as whatsapp_router
from src.api.sync_routes import router as sync_router

app = FastAPI(
    title=settings.APP_NAME,
    description="Ecosistema Abierto, Soberano y Offline-First de IA Educativa para Paraguay.",
    version="0.1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# CORS para permitir integración con PWA y clientes locales
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar routers de API
app.include_router(tutor_router)
app.include_router(docente_router)
app.include_router(whatsapp_router)
app.include_router(sync_router)

# Montar frontend estático PWA si existe el directorio
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")
