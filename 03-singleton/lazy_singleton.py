class Singleton(object):

    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('__init__ was called...')
        else:
            print('Instance already created:', self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s1 = Singleton()  # Class is initialized, but object is not created
print(f'Creating instance: {Singleton.get_instance()}')

s2 = Singleton()  # Instance already created