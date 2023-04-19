from abc import ABC, abstractmethod


class Pill(ABC):
    dosage_info = "Проконсультруйтесь с доктором"

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_dosage(self):
        pass

    def get_dosage_info(self):
        return self.dosage_info

    def get_info(self):
        return f"Цена {self.price}, наименование - {self.name}"


class Aspirin(Pill):
    dosage_info = "Используйте при головном боле."

    def get_dosage(self):
        return "Принимайте таблетку раз в 4 часа."


class Paracetamol(Pill):
    dosage_info = "Используйте при головном боле."

    def get_dosage(self):
        return "Принимайте таблетку раз в 6 часов."


class PillFactory(ABC):

    @abstractmethod
    def create_pill(self, name, price):
        pass


class AspirinFactory(PillFactory):

    def create_pill(self, name, price):
        return Aspirin(name, price)


class ParacetamolFactory(PillFactory):

    def create_pill(self, name, price):
        return Paracetamol(name, price)


if __name__ == '__main__':
    aspirin_factory = AspirinFactory()
    aspirin = aspirin_factory.create_pill("Aspirin", 2.5)
    print(aspirin.get_info())
    print(aspirin.get_dosage_info())
    print(aspirin.get_dosage(), end="\n\n")

    paracetamol_factory = ParacetamolFactory()
    paracetamol = paracetamol_factory.create_pill("Paracetamol", 1.5)
    print(paracetamol.get_info())
    print(paracetamol.get_dosage_info())
    print(paracetamol.get_dosage())