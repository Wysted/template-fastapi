from app.dependencies import settings
from app.core.config import configuration
from app.dependencies import typing
from app.dependencies import jwt, JWTError
from app.dependencies import security
from app.dependencies import exceptions
from app.dependencies import status
from app.dependencies import TokenData, UserTypes
from app.dependencies import fastapi
from app.dependencies import context

schema = security.OAuth2PasswordBearer(
    tokenUrl="token",
)

class Auth():
    TOKEN_DATA_KEY = 'token_data'
    _exception = exceptions.HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
    )

    async def is_auth(self, token: str = fastapi.Depends(schema)) -> None:
        try:
            payload = jwt.decode(
                token.replace('Bearer ', ''),
                settings.JWT_SECRET_KEY,
                algorithms=[configuration.jwt_algotithm],
            )

            context.setdefault(
                self.TOKEN_DATA_KEY,
                TokenData(
                    user_type=UserTypes(payload.get('user_type')),
                    id=payload.get('_id'),
                    sub=payload.get('sub')
                ),
            )
        except JWTError:
            raise self._exception
    
    def roles(self, roles: typing.List[str]):
        def manageRoles():
            tokenData: TokenData = context.data.get(self.TOKEN_DATA_KEY)

            if all(role != tokenData.user_type for role in roles):
                raise self._exception
        return manageRoles

    def decode_token(self, token: str = fastapi.Depends(schema)) -> TokenData:
        return context.data.get(self.TOKEN_DATA_KEY)

auth_service = Auth()
