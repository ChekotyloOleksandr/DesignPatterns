from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Margarita(Pizza):
    def get_cost(self):
        return 130

    def get_info(self):
        return "Margarita"


class Hawaiian(Pizza):
    def get_cost(self):
        return 150

    def get_info(self):
        return "Hawaiian"


class Buffalo(Pizza):
    def get_cost(self):
        return 200

    def get_info(self):
        return "Buffalo"


class AddPizzaTopping(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza

    def get_cost(self):
        return self._pizza.get_cost()

    def get_info(self):
        return self._pizza.get_info()


class AddCheese(AddPizzaTopping):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_cost(self):
        return self._pizza.get_cost() + 30

    def get_info(self):
        return self._pizza.get_info() + " with cheese topping"


class AddMeat(AddPizzaTopping):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_cost(self):
        return self._pizza.get_cost() + 50

    def get_info(self):
        return self._pizza.get_info() + " with meat topping"

if __name__ == '__main__':
    margarita = Margarita()
    margarita_with_meat = AddMeat(margarita)
    print(f"{margarita_with_meat.get_cost()} - {margarita_with_meat.get_info()}")
    buffalo = Buffalo()
    buffalo_with_cheese = AddCheese(buffalo)
    print(f"{buffalo_with_cheese.get_cost()} - {buffalo_with_cheese.get_info()}")
    hawaiian = Hawaiian()
    hawaiian_with_cheese = AddCheese(hawaiian)
    hawaiian_with_cheese_and_meat=AddMeat(hawaiian_with_cheese)
    print(f"{hawaiian_with_cheese_and_meat.get_cost()} - {hawaiian_with_cheese_and_meat.get_info()}")