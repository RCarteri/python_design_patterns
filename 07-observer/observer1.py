class Object:
    def __init__(self):
        self.__observers = []

    def __repr__(self):
        return 'Object'
    def register(self, observer):
        self.__observers.append(observer)
    def notify_all(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)

class ObserverA:
    def __init__(self, object):
        object.register(self)
    def __repr__(self):
        return self.name
    def notify(self, object, *args):
        print(f'{type(self).__name__} has been notified by {object}: {args}!')

class ObserverB:
    def __init__(self, object):
        object.register(self)
    def __repr__(self):
        return self.name
    def notify(self, object, *args):
        print(f'{type(self).__name__} has been notified by {object}: {args}!')

obj = Object()

obs1 = ObserverA(obj)
obs2 = ObserverB(obj)

obj.notify_all('notification', 'message')