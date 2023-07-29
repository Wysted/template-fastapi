# FastAPI
from app.dependencies import fastapi
from app.dependencies import responses
# Interfaces
from app.dependencies import Res
# JWT
from app.dependencies import TokenData, UserTypes
# Services
from app.dependencies import auth_service
from app.services.users import users_service
# Settings
from app.core.config import configuration

router = fastapi.APIRouter(
    prefix=configuration.default_api,
    dependencies=[fastapi.Depends(auth_service.is_auth)],
)

@router.get(
    '/x',
    response_model=Res[None],
    dependencies=[fastapi.Depends(auth_service.roles([UserTypes.STUDIO_OWNER]))],
)
async def get(tokenData: TokenData = fastapi.Depends(auth_service.decode_token)) -> Res:
    users = users_service.get_users()
    return responses.JSONResponse(
        status_code=200,
        content = {
            'success': True,
            'body': users,
        }
    )
