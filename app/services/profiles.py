# Responses
import fastapi
from fastapi.exceptions import HTTPException
from fastapi import UploadFile

status = fastapi.status

# Models
from app.models.profile import Profile
# Interfaces
from app.interfaces.profile import Profile as ProfileBody
from app.interfaces.profile import ProfileUpdate
from app.services.categories import categories_service
from app.services.files import files_service
# Token
from app.dependencies import TokenData

class Profiles():
    #Buscar perfil por el user
    def get_by_id(self, id: str) -> Profile | None:
        return Profile.objects(user=id).first()
    #Crea un perfil al crear el usuario de tipo Tatuador b
    def create_profile(self,id : str, name : str) -> Profile:
        user_profile = ProfileBody(user = str(id),nickname = name)
        return Profile(**user_profile.to_model()).save()
    #Actualizar datos nickname, description o categories
    def update_profile(self,profileUpdate: ProfileUpdate,tokenData : TokenData) -> Profile:
        profile = self.get_by_id(tokenData.id)
        if profileUpdate.nickname is not None:
            profile.update(**{"nickname": profileUpdate.nickname})
        if profileUpdate.description is not None:
            profile.update(**{"description": profileUpdate.description})
        if profileUpdate.categories is not None:
            profile.update(**{"unset__categories": 1})
            for category in profileUpdate.categories:
                inserte_category = categories_service.get_by_name(category)
                if inserte_category is  None:  
                    raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Not a valid category',
                    )
                profile.update(**{"push__categories" : inserte_category.id})
        return
    #Cambia el avatar del perfil hay que cambiar el api a lo correcto B), o no?
    def update_avatar (self,file : UploadFile,tokenData : TokenData) -> Profile:
        profile = self.get_by_id(tokenData.id)
        photo = files_service.upload_file(f"{profile.user.id}_avatar.png",file)
        if profile is not None:
            profile.update(**{"avatar": f"api/{photo}"})
        return



profiles_service = Profiles()
