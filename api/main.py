"""FastAPI application entry point."""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import DBAPIError, OperationalError

from config.settings import Settings, get_settings
from database.connection import init_db

from .logging import configure_logging
import logging
from .routes.system import router as system_router
from .routes.auth import router as auth_router
from .routes.biometrics import router as biometrics_router
from .routes.oauth import router as oauth_router
from .routes.chat import router as chat_router
from .routes.documents import router as documents_router
from .routes.admin import router as admin_router
from .routes.rag import router as rag_router



API_VERSION = "0.1.0"

def create_app(settings: Settings | None = None) -> FastAPI:
    """Create the application using the shared project settings."""
    resolved_settings = settings or get_settings()
    configure_logging(resolved_settings.debug)

    # Initialize database extensions, schemas, and default data
    init_db()

    application = FastAPI(
        title=resolved_settings.app_name,
        version=API_VERSION,
        description="Agentic RAG API",
    )
    application.state.environment = resolved_settings.app_env
    application.add_middleware(
        CORSMiddleware,
        allow_origins=resolved_settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    @application.exception_handler(OperationalError)
    @application.exception_handler(DBAPIError)
    async def database_exception_handler(request: Request, exc: Exception):
        logger = logging.getLogger("uvicorn.error")
        logger.error(f"Database unavailable: {exc}", exc_info=True)
        return JSONResponse(
            status_code=503,
            content={"detail": "Database service is currently unavailable. Please try again shortly."}
        )

    @application.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger = logging.getLogger("uvicorn.error")
        logger.error(f"Unhandled exception: {exc}", exc_info=True)
        if application.state.environment == "production":
            return JSONResponse(
                status_code=500,
                content={"detail": "Internal server error"}
            )
        # In non-production, we can return the exception details for easier debugging
        return JSONResponse(
            status_code=500,
            content={"detail": str(exc)}
        )
    application.include_router(system_router)
    application.include_router(auth_router)
    application.include_router(auth_router, prefix="/api")
    application.include_router(biometrics_router)
    application.include_router(oauth_router)
    application.include_router(chat_router)
    application.include_router(documents_router)
    application.include_router(admin_router)
    application.include_router(admin_router, prefix="/api")
    application.include_router(rag_router)
    return application


app = create_app()
