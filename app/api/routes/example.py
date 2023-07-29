# FastAPI
from app.dependencies import fastapi
from app.dependencies import responses
# Interfaces
from app.dependencies import Res
# JWT
from app.dependencies import TokenData, UserTypes
# Services
from app.dependencies import auth_service
# Settings
from app.core.config import configuration

router = fastapi.APIRouter(
    prefix=configuration.default_api,
    dependencies=[fastapi.Depends(auth_service.is_auth)],
)

@router.get(
    '/x',
    response_model=Res[None],
    dependencies=[fastapi.Depends(auth_service.roles([UserTypes.DIRECTOR]))],
)
async def get(tokenData: TokenData = fastapi.Depends(auth_service.decode_token)) -> Res:
    return responses.JSONResponse(
        status_code=200,
        content = {
            'success': True,
            'body': 'hola!',
        }
    )
