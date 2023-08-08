# FastAPI
from app.dependencies import fastapi
from app.dependencies import responses

status = fastapi.status
# Interfaces
from app.dependencies import Res
from app.interfaces.profile import ProfileUpdate


# JWT
from app.dependencies import TokenData, UserTypes
# Services

from app.dependencies import auth_service
from app.services.profiles import profiles_service
# Settings

from app.core.config import configuration

router = fastapi.APIRouter(
    prefix=f'{configuration.default_api}/profiles',
)

@router.patch(
    '/update',
    response_model=Res[None],
    dependencies=[fastapi.Depends(auth_service.is_auth),fastapi.Depends(auth_service.roles([UserTypes.TATTO_ARTIST]))],

)
async def update(profileUpdate: ProfileUpdate,tokenData: TokenData = fastapi.Depends(auth_service.decode_token)) -> Res:
    profiles_service.updateProfile(profileUpdate,tokenData)
    return responses.JSONResponse(
        status_code=200,
        content = {
            'success': True,
            'body': '',
        }
    )