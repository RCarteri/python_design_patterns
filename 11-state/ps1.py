from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        print("ConcreteStateA.handle()")

class ConcreteStateB(State):
    def handle(self):
        print("ConcreteStateB.handle()")

class Context(State):
    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def handle(self):
        self.state.handle()

if __name__ == "__main__":
    context = Context()
    stateA = ConcreteStateA()
    stateB = ConcreteStateB()
    context.setState(stateA)
    context.handle()
    context.setState(stateB)
    context.handle()