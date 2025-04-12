from dataclasses import dataclass
from datetime import date
from enum import Enum

class MovementType(Enum):
    INCOME = "income"
    EXPENSE = "expense"

@dataclass
class Movement:
    """Here will be the financial movements"""
    idMovement: int
    value: float
    description: str
    idCategory: int
    movDate: date
    movType: MovementType

    def __post_init__(self):
        if not isinstance(self.movType, MovementType):
            raise ValueError("The movType is not a instance of MovementType Enum")
        
    def insert(self):
        print("inserting on the dataBase")

    def find(self, *arg):
        pass
        #maybe find by some key, I think id is bether
    
    def update(self):
        print(f"updating id {self.idMovement}")

    @staticmethod
    def delete(idMovement):
        print(f"deleting id {idMovement}")


Movement(500, "Salário", 1, date.today(), MovementType.INCOME).insert()
Movement.update(500)
Movement.delete(500)


"""
def __init__(self, value, description, idCategory, movDate, movType):
        self.value = value
        self.description = description
        self.idCategory = idCategory
        self.movDate = movDate
        self.movType = movType
"""

    

