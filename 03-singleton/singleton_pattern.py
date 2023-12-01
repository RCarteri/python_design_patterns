class Singleton(object):

    __instance = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            print(f'Creating: {cls.instance}')
            return cls.instance

s1 = Singleton()
print(f'Instance 1: {id(s1)}')

s2 = Singleton()
print(f'Instance 2: {id(s2)}')