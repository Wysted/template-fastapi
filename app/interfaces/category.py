from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import bcrypt

class Category(BaseModel):
    name: str # Solo debería aceptar Tatuador, Cliente y Dueño de estudio
    description : Optional[str]
    def to_model(self):
        return {
            'name': self.name,
            'description': self.description,
            'date': datetime.utcnow(),
        }