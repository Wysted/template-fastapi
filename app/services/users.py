from app.models.user import User

class Users():
    def get_users():
        return User.objects()

users_service = Users()
