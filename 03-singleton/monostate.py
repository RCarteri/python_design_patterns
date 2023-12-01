class Monostate:
    __state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__state
        return obj

m1 = Monostate()
print(f'M1 ID: {id(m1)}')
print(m1.__dict__)

m2 = Monostate()
print(f'M2 ID: {id(m2)}')
print(m2.__dict__)

m1.name = 'Felicity'

print(f'M1 name: {m1.name}')
print(f'M2 name: {m2.name}')