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

    def __init__(self, name, price):
        super(Aspirin, self).__init__(name=name, price=price)

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

    def get_description(self):
        return "Абстрактаная фабрика. Она плод вообржаения."


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


class AspirinFactory(PillFactory):

    def create_aspirin(self, name, price):
        return Aspirin(name, price)

    def create_paracetamol(self, name, price):
        return Paracetamol(name, price)

    def get_description(self):
        return "Фабрика производит аспирин и парацетамол"


if __name__ == '__main__':
    aspirin_factory = AspirinFactory()
    print(aspirin_factory.get_description())
    aspirin = aspirin_factory.create_aspirin("Aspirin", 2.5)
    print(aspirin.get_info())
    print(aspirin.get_dosage_info())
    print(aspirin.get_dosage(), end="\n\n")

    paracetamol = aspirin_factory.create_paracetamol("Paracetamol", 1.5)
    print(paracetamol.get_info())
    print(paracetamol.get_dosage_info())
    print(paracetamol.get_dosage())
