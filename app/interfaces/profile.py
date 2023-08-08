from pydantic import BaseModel
from typing import Optional
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
    nickname: Optional[str]
    description : Optional[str]
    avatar : Optional[str]
    # categories : Optional[str] 

   