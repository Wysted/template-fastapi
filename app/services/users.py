# Responses
import fastapi
from fastapi.exceptions import HTTPException
import bcrypt

status = fastapi.status
# Models
from app.models.user import User
# Interfaces
from app.interfaces.user import User as UserBody
#User types
from app.interfaces.user_types import UserTypes

from app.dependencies import TokenData
#Services

class Users():
    def get_by_email(self, email: str) -> User | None:
        return User.objects(email=email).first()
    
    def get_by_id(self, id: str) -> User | None:
        return User.objects(id=id).first()

    def register(self, user: UserBody) -> User:
        valid_users = [
            UserTypes.SUBUSER.value,
            UserTypes.ADMIN.value,
        ]
        if user.role not in valid_users:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not valid role',
            )
        # Exists user
        exists_user = User.objects(email=user.email).only('id').first()
        if exists_user is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='El usuario ya está registrado',
            )

        inserted_user = User(**user.to_model()).save()

        return inserted_user.id
users_service = Users()
