from abc import ABC, abstractmethod

class ComputerState(ABC):
    name = "computerState"
    allowed = []

    def change(self, state):
        if state.name in self.allowed:
            print(f"Current: {self} => switched to new state {state.name}")
            self.__class__ = state
        else:
            print(f"Current: {self} => switching to {state.name} not possible")

    def __str__(self):
        return self.name

class On(ComputerState):
    name = "on"
    allowed = ["off", "suspend", "hibernate"]

class Off(ComputerState):
    name = "off"
    allowed = ["on"]

class Suspend(ComputerState):
    name = "suspend"
    allowed = ["on"]

class Hibernate(ComputerState):
    name = "hibernate"
    allowed = ["on"]

class Computer:
    def __init__(self, model="HP"):
        self.model = model
        self.state = Off()

    def change(self, state):
        self.state.change(state)

if __name__ == "__main__":
    comp = Computer()
    comp.change(On)
    comp.change(Off)
    comp.change(On)
    comp.change(Suspend)
    comp.change(Hibernate)
    comp.change(On)
    comp.change(Off)