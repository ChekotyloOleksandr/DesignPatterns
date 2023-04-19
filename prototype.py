import copy


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        return f"{self.name} {self.age} {self.city}"

    def clone(self):
        return copy.deepcopy(self)


if __name__ == '__main__':
    maxim = Person("Maxim", 30, 'Kharkiv')
    nikita = maxim.clone()
    nikita.name = "Nikita"
    nikita.city = "Kiev"
    print(maxim)
    print(nikita)
