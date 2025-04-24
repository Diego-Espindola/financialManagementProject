import sqlite3
from dataclasses import dataclass
from datetime import date
from enum import Enum


class MovementType(Enum):
    INCOME = "income"
    EXPENSE = "expense"


@dataclass
class Movement:
    idMovement: int
    value: float
    description: str
    idCategory: int
    movDate: date
    movType: MovementType

    def __post_init__(self):
        if not isinstance(self.movType, MovementType):
            raise ValueError("movType must be an instance of MovementType")

    @staticmethod
    def connect():
        conn = sqlite3.connect("movements.db")
        conn.execute('''
            CREATE TABLE IF NOT EXISTS movements (
                idMovement INTEGER PRIMARY KEY,
                value REAL,
                description TEXT,
                idCategory INTEGER,
                movDate TEXT,
                movType TEXT
            )
        ''')
        return conn

    def insert(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO movements (idMovement, value, description, idCategory, movDate, movType)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.idMovement, self.value, self.description, self.idCategory, self.movDate.isoformat(), self.movType.value))
        conn.commit()
        conn.close()
        print(f"Inserted movement {self.idMovement}")

    @staticmethod
    def find(idMovement):
        conn = Movement.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM movements WHERE idMovement = ?', (idMovement,))
        result = cursor.fetchone()
        conn.close()
        return result

    def update(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE movements SET
                value = ?,
                description = ?,
                idCategory = ?,
                movDate = ?,
                movType = ?
            WHERE idMovement = ?
        ''', (self.value, self.description, self.idCategory, self.movDate.isoformat(), self.movType.value, self.idMovement))
        conn.commit()
        conn.close()
        print(f"Updated movement {self.idMovement}")

    @staticmethod
    def delete(idMovement):
        conn = Movement.connect()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM movements WHERE idMovement = ?', (idMovement,))
        conn.commit()
        conn.close()
        print(f"Deleted movement {idMovement}")
