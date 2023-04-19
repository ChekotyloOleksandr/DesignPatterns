class SomeClass:
    _instance = None

    def __init__(self, x: str):
        if not self._instance:
            self.x = x
            self.__class__._instance = self
        else:
            self.x = self.__class__._instance.x

    def __str__(self):
        return self.x


a = SomeClass("First")
b = SomeClass('Second')
print(a,b)  # Output: 1 1
