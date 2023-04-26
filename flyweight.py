from factory_method import Pill, PillFactory


class Aspirin(Pill):
    def change_price(self, price):
        self.price = price

    def get_dosage(self):
        return "Принимайте таблетку раз в 4 часа."


class AspirinFactoryFlyweight(PillFactory):
    _flyweights = {}

    def create_pill(self, name, price):
        if name not in self._flyweights:
            self._flyweights[name] = Aspirin(name, price)
        else:
            self._flyweights[name].change_price(price)
        return self._flyweights[name]


if __name__ == '__main__':
    factory = AspirinFactoryFlyweight()
    aspirin1 = factory.create_pill("Aspirin1", 0.5)
    print(aspirin1.get_info())
    aspirin2 = factory.create_pill("Aspirin2", 1.0)
    aspirin3 = factory.create_pill("Aspirin1", 3)
    print(aspirin2.get_info())
    print(aspirin1.get_info())
    print(aspirin3.get_info())
    print(aspirin1 is aspirin2)
    print(aspirin1 is aspirin3)
