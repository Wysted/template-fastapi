from enum import Enum

class UserStates(Enum):
    DISABLED = 'deactivate'
    ACTIVE = 'active'

class UserTypes(Enum):
    ADMIN = 'd'
    CLIENT = 'a'
