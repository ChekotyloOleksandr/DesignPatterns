class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SomeClass(metaclass=SingletonMeta):
    def __init__(self, x: str):
        self.x = x


a = SomeClass("First")
b = SomeClass('Secondd')
print(id(a), id(b))  # Output: 1 1
