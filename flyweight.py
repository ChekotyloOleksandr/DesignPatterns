import hashlib
from factory_method import Pill, PillFactory

class Aspirin(Pill):
    def __init__(self, name, price):
        super().__init__(name, price)

    def change_price(self, price):
        self.price = price

    def get_dosage(self):
        return "Принимайте таблетку раз в 4 часа."


    def __repr__(self):
        return f"Aspirin(name={self.name}, price={self.price})"


class AspirinFactoryFlyweight(PillFactory):
    _flyweights = {}

    def create_pill(self, name, price):
        identifier = hashlib.md5(name.encode()).hexdigest()
        if identifier not in self._flyweights:
            self._flyweights[identifier] = Aspirin(name, price)
        return self._flyweights[identifier]


if __name__ == '__main__':
    factory = AspirinFactoryFlyweight()
    aspirin1 = factory.create_pill("Aspirin1", 0.5)
    print(aspirin1.get_info())
    aspirin2 = factory.create_pill("Aspirin2", 1.0)
    print(aspirin1.get_info())
    aspirin3 = factory.create_pill("Aspirin1", 0.5)
    print(aspirin1.get_info())
    print(aspirin1 is aspirin2)
    print(aspirin1 is aspirin3)