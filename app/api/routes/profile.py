# FastAPI
from app.dependencies import fastapi
from app.dependencies import responses

status = fastapi.status
# Interfaces
from app.dependencies import Res
# JWT
from app.dependencies import TokenData
# Services
from app.dependencies import auth_service
from app.services.users import users_service
# Settings
from app.core.config import configuration

router = fastapi.APIRouter(
    prefix=f'{configuration.default_api}/profiles',
)

@router.patch(
    '/update',
    response_model=Res[None],
    dependencies=[fastapi.Depends(auth_service.is_auth)],

)
async def update(tokenData: TokenData = fastapi.Depends(auth_service.decode_token)) -> Res:

    return responses.JSONResponse(
        status_code=200,
        content = {
            'success': True,
            'body': '',
        }
    )