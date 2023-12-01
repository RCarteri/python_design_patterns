class MetaSingleton(type):
	_instances = {}

	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

class Singleton(metaclass=MetaSingleton):
	pass

s1 = Singleton()
print(f'Object created: {id(s1)}')

s2 = Singleton()
print(f'Object created: {id(s2)}')