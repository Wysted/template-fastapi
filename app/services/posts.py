# Responses
import fastapi
from fastapi.exceptions import HTTPException
from fastapi import UploadFile
status = fastapi.status

# Models

from app.models.post import Post
# Interfaces
from app.interfaces.post import Post as PostBody


from app.services.tattoos import tattoos_service
from app.services.profiles import profiles_service


# Token
from app.dependencies import TokenData

class Posts():
    def create_post(self,files : list[UploadFile],categories: list,content:str , tokenData : TokenData) -> Post:
        profile = profiles_service.get_by_id_user(tokenData.id)
        if profile is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Not valid profile',
            )
        #Subir post con imagenes del post, todas las categorias se aplican a todas las imagenes del post
        inserted_tattoos = tattoos_service.create_tatto(files,categories,tokenData)
        post = PostBody(profile = str(profile.id), tatto = inserted_tattoos, content =content)
        Post(**post.to_model()).save()

        

posts_service = Posts()