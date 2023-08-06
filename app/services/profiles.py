# Responses
import fastapi
from fastapi.exceptions import HTTPException
import bcrypt

status = fastapi.status
# Models
from app.models.profile import Profile
# Interfaces
from app.interfaces.user import User as UserBody
from app.interfaces.profile import Profile as ProfileBody
#State
from app.interfaces.user_types import UserTypes

class Profiles():

    def createProfile(self,id : str, name : str) -> Profile:
        user_profile = ProfileBody(user = str(id),nickname = name)
        return Profile(**user_profile.to_model()).save()

    


profiles_service = Profiles()
