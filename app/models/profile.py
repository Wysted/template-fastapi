from mongoengine import *
from app.db.db import uri

PROFILE_COLLECTION = 'profiles'

connect(host=uri)

class Profile(Document):
    user = ReferenceField('User', required=True)
    description = StringField(required=False, max_length=500)
    avatar = StringField(required=False)
    likes = IntField(min_value=0, default=0)
    categories = ReferenceField('Category', required=True)
    nickname = StringField(required=True, max_length=25)
    date = DateField(required=True)
    