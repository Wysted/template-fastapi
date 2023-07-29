from app.dependencies import db

USER_COLLECTION = 'users'

user = db.get_collection(USER_COLLECTION)
