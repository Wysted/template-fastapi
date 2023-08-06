from pydantic import BaseModel
from datetime import datetime
import bcrypt

class Profile(BaseModel):
    user: str 
    nickname: str
    def to_model(self):
        return {
            'user': self.user,
            'nickname': self.nickname,
            'likes' : 0,   
            'date': datetime.utcnow(),
        }


class ProfileUpdate(BaseModel):
    method : str
    data : str
   