class Actor:
    def __init__(self):
        self.isBusy = False

    def occupied(self):
        self.isBusy = True
        print(type(self).__name__, "is occupied with current movie")

    def available(self):
        self.isBusy = False
        print(type(self).__name__, "is free for the movie")

    def getStatus(self):
        return self.isBusy

class Agent:
    def work(self):
        actor = Actor()
        if actor.getStatus():
            actor.occupied()
        else:
            actor.available()

Agent().work()