# FastAPI
from app.dependencies import fastapi

status = fastapi.status
# FastAPI
from starlette.background import BackgroundTasks
# Services
from app.services.files import files_service
# Settings
from app.core.config import configuration

router = fastapi.APIRouter(
    prefix=f'{configuration.default_api}/profiles',
)
