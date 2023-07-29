from enum import Enum

class UserTypes(Enum):
    DIRECTOR = 'f'
    DIRECTIVE = 'e'
    TEACHER = 'd'
    ATTORNEY = 'c'
    STUDENT_DIRECTIVE = 'b'
    STUDENT = 'a'
