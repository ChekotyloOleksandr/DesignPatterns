import decorator


class Customer:
    def __init__(self, name, address, city):
        self.name = name
        self.address = address
        self.city = city

    def get_info(self):
        return f"имя - {self.name}, адрес - {self.address}, город - {self.city}"


class Order:
    def __init__(self, name, address, city):
        self.items = []
        self.customer = Customer(name, address, city)

    def add_item_in_order(self, product: decorator.Pizza):
        self.items.append(product)

    def get_total_price(self):
        return sum(item.get_cost() for item in self.items)

    def deliver(self):
        print(f"Данные:{self.customer.get_info()}")
        print(f"Заказ: {[f'{item.get_info()} - {item.get_cost()}' for item in self.items]}")
        print(f"Общая стоимость: {self.get_total_price()}")


class OrderFacade:
    @staticmethod
    def create_order(name, address, city, *pizzas):
        customer = Customer(name, address, city)
        order = Order(name, address, city)

        for pizza in pizzas:
            order.add_item_in_order(pizza)

        order.deliver()


if __name__ == '__main__':
    OrderFacade.create_order(
        "Олекса",
        "Пушкінська 82",
        "Харків",
        decorator.AddMeat(decorator.Margarita()),
        decorator.Buffalo()
    )
