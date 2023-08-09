# FastAPI
from app.dependencies import fastapi
from app.dependencies import responses

status = fastapi.status
# Interfaces
from app.dependencies import Res
from app.interfaces.category import Category
# FastAPI
# Services
from app.services.categories import categories_service
# Settings
from app.core.config import configuration

router = fastapi.APIRouter(
    prefix=f'{configuration.default_api}/categories',
)

@router.post(
    '',
    response_model=Res[str],
    response_description='El ID del dato insertado',
)
async def create_category(category: Category):
    inserted_category = categories_service.create_category(category)

    return responses.JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            'success': True,
            'body': str(inserted_category),
        },
    )
