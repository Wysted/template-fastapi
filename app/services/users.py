# Responses
import fastapi
from fastapi.exceptions import HTTPException
import bcrypt

status = fastapi.status
# Models
from app.models.user import User
# Interfaces
from app.interfaces.user import UserUpdate,User as UserBody

class Users():
    def get_by_email(self, email: str) -> User | None:
        return User.objects(email=email).first()
    
    def get_by_id(self, id: str) -> User | None:
        return User.objects(id=id).first()

    def register(self, user: UserBody) -> User:
        valid_users = ['a', 'b', 'c']
        if user.role not in valid_users:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not valid role',
            )
        return User(**user.to_model()).save()
    

    def update(self, id: str, userUpdate: UserUpdate):
        valid_methods = ['email', 'password']
        if userUpdate.method not in valid_methods:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Not a valid method',
            )
        user = self.get_by_id(id)
        if userUpdate.method == 'email':
            user.update(**{userUpdate.method: userUpdate.data})
        else:
            is_pass = bcrypt.checkpw(
                bytes(userUpdate.data, 'utf-8'),
                bytes(user.password, 'utf-8'),
            )
            if is_pass is True:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='The password must not be the same as the previous one',
                )
            password = bcrypt.hashpw(
                password=bytes(userUpdate.data, 'utf-8'),
                salt=bcrypt.gensalt(),
            ).decode('utf-8')
            user.update(**{userUpdate.method: password})
            return user.reload()
            
users_service = Users()
