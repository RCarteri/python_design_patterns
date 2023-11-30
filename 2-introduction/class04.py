from abc import ABC, abstractmethod
from uuid import uuid4

class Pessoa(ABC):
    def __init__(self, name):
        self.__name = name

    @classmethod
    @abstractmethod
    def earn_money(self):
        pass

class Student(Pessoa):
    def __init__(self, name):
        super().__init__(name)
        self.__matricula = str(uuid4()).split('-')[0].upper()

    def earn_money(self):
        print(f'{self.__name} is earning money as a student')

student1 = Student('Felicity')
print(student1.__dict__)