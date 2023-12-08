from datetime import datetime

class Person:
    def __init__(self: object, name: str):
        self.__name = name
        self.__birth = datetime.now()

    def __str__(self):
        return self.__name

    def __repr__(self):
        return self.__name

class Car:
    def __init__(self: object, is_sedan: bool = False) -> None:
        self.__is_sedan = is_sedan
        self.__speed = 0
        self.__driver = None

    def __str__(self):
        if self.__driver:
            return f"{self.__driver} {self.__driver.__name}'s car"
        return 'Car without driver'

    def drive(self, driver: Person) -> None:
        self.__driver = driver
        self.speed_up(1)

    def speed_up(self, speed: int) -> None:
        self.__speed += speed

    def stop(self):
        self.__speed = 0
