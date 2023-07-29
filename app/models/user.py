from mongoengine import *
from app.db.db import uri

USER_COLLECTION = 'users'

connect(host=uri)

class User(Document):
    email = StringField(required=True, max_length=255)
