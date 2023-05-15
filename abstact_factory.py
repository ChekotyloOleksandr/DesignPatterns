from abc import ABC, abstractmethod
from factory_method import Pill


class Aspirin(Pill):
    dosage_info = "Используйте при головном боле."

    def get_dosage(self):
        return "Принимайте таблетку раз в 4 часа."


class Paracetamol(Pill):
    dosage_info = "Используйте при головном боле."

    def get_dosage(self):
        return "Принимайте таблетку раз в 6 часов."


class FakeAspirin(Pill):
    dosage_info = "Используйте при головном боле. Повышает температуру"

    def get_dosage(self):
        return "Принимайте таблетку раз в 2 часа."


class FakeParacetamol(Pill):
    dosage_info = "Используйте при головном боле. Понижает температуру."

    def get_dosage(self):
        return "Принимайте таблетку раз в 5 часов."


class PillFactory(ABC):

    @abstractmethod
    def create_aspirin(self, name, price):
        pass

    @abstractmethod
    def create_paracetamol(self, name, price):
        pass

    @abstractmethod
    def get_description(self):
        pass


class LegalFactory(PillFactory):

    def create_aspirin(self, name, price):
        return Aspirin(name, price)

    def create_paracetamol(self, name, price):
        return Paracetamol(name, price)

    def get_description(self):
        return "Фабрика производит аспирин и парацетамол"


class IllegalFactory(PillFactory):

    def create_aspirin(self, name, price):
        return FakeAspirin(name, price)

    def create_paracetamol(self, name, price):
        return FakeParacetamol(name, price)

    def get_description(self):
        return "Фабрика производит аспирин и парацетамол нелегально"


if __name__ == '__main__':
    legal_factory = LegalFactory()
    print(legal_factory.get_description())
    aspirin = legal_factory.create_aspirin("Aspirin", 2.5)
    print(aspirin.get_info())
    print(aspirin.get_dosage_info())
    print(aspirin.get_dosage())

    paracetamol = legal_factory.create_paracetamol("Paracetamol", 1.5)
    print(paracetamol.get_info())
    print(paracetamol.get_dosage_info())
    print(paracetamol.get_dosage())
    print()

    ilegal_factory = IllegalFactory()
    print(ilegal_factory.get_description())
    fake_aspirin = ilegal_factory.create_aspirin("Fake Aspirin", 0.5)
    print(fake_aspirin.get_info())
    print(fake_aspirin.get_dosage_info())
    print(fake_aspirin.get_dosage())

    fake_paracetamol = ilegal_factory.create_paracetamol("Fake Paracetamol", 1.5)
    print(fake_paracetamol.get_info())
    print(fake_paracetamol.get_dosage_info())
    print(fake_paracetamol.get_dosage())