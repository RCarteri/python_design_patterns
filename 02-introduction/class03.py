from typing import List, Tuple


class Course:
    def __init__(self, name: str = "Course default", hours: int = 45) -> None:
        self.__name = name
        self.__hours = hours


course1 = Course()
course2 = Course("Python", 40)
course3 = Course("Java", 60)

# print(course1.__dict__)
# print(course2.__dict__)
# print(course3.__dict__)

name: str = 'geek university'
tuple: Tuple = (1, 2, 3, 4, 5)
list: List = [1, 2, 3, 4, 5]


# print(name[:4], tuple[:4], list[:4])

class Person:
    def __init__(self, name: str) -> None:
        self.__name = name

    def walk(self) -> None:
        print(f'{self.__name} is walking')


class Student(Person):
    def __init__(self, name: str, registration: str) -> None:
        super().__init__(name)
        self.__registration = registration


felicity = Student('Felicity', '123456')


# felicity.walk()

def fibbonacci_sequence(n: int) -> List[int]:
    sequence: List[int] = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


# print(fibbonacci_sequence(10))

class Engine:
    def start(self) -> None:
        print('Starting engine')


class Tire:
    def roll(self) -> None:
        print('Rolling tire')


class Car:
    def __init__(self, model: str) -> None:
        self.__model = model
        self.__engine = Engine()
        self.__tires = [Tire(), Tire(), Tire(), Tire()]


fusca = Car('Fusca')
fusca._Car__engine.start()
