# Responses
import fastapi
from fastapi.exceptions import HTTPException
import bcrypt

status = fastapi.status
# Models
from app.models.profile import Profile
# Interfaces
from app.interfaces.profile import Profile as ProfileBody
from app.interfaces.profile import ProfileUpdate
# Token
from app.dependencies import TokenData

class Profiles():
    #Buscar perfil por el user
    def get_by_id(self, id: str) -> Profile | None:
        return Profile.objects(user=id).first()
    #Crea un perfil al crear el usuario de tipo Tatuador b
    def createProfile(self,id : str, name : str) -> Profile:
        user_profile = ProfileBody(user = str(id),nickname = name)
        return Profile(**user_profile.to_model()).save()
    #Actualizar datos
    def updateProfile(self,profileUpdate: ProfileUpdate,tokenData : TokenData):
        profile = self.get_by_id(tokenData.id)
        if profileUpdate.nickname is not None:
            profile.update(**{"nickname": profileUpdate.nickname})
        if profileUpdate.description is not None:
            profile.update(**{"description": profileUpdate.description})
        if profileUpdate.avatar is not None:
            profile.update(**{"avatar": profileUpdate.avatar})
        return

    


profiles_service = Profiles()
