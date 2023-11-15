from mongoengine import *
from app.db.db import uri
# Interfaces
from app.interfaces.user_types import UserTypes

USER_COLLECTION = 'users'

connect(host=uri)

class User(Document):
    role = EnumField(UserTypes, default=UserTypes.ADMIN)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    name = StringField(required=True, max_length=100)
    date = DateField(required=True)
