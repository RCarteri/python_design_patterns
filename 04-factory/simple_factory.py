from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")

class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")

# Factory
class Factory:
    def get_animal(self, animal_type):
        return eval(animal_type)().do_say()

# Client
if __name__ == '__main__':
    factory = Factory()
    factory.get_animal('Dog')

    factory.get_animal('Cat')