# Responses
import fastapi
from fastapi.exceptions import HTTPException

status = fastapi.status
# Models
from app.models.user import User
# Interfaces
from app.interfaces.user import User as UserBody

class Users():
    def get_by_email(self, email: str) -> User | None:
        return User.objects(email=email).first()

    def register(self, user: UserBody) -> User:
        valid_users = ['a', 'b', 'c']
        if user.role not in valid_users:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not valid role',
            )

        return User(**user.to_model()).save()

users_service = Users()
