from abc import ABC, abstractmethod


class Product:
    def __init__(self, name: str, price: int, delivery: int, rating: float):
        self.name = name
        self.price = price
        self.delivery = delivery
        self.rating = rating


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, product_list, reverse):
        pass


class PriceSort(SortStrategy):
    def sort(self, product_list, reverse):
        return sorted(product_list, key=lambda x: x.price, reverse=reverse)


class DeliverySort(SortStrategy):
    def sort(self, product_list, reverse):
        return sorted(product_list, key=lambda x: x.delivery, reverse=reverse)


class RatingSort(SortStrategy):
    def sort(self, product_list, reverse):
        return sorted(product_list, key=lambda x: x.rating, reverse=reverse)


class NameSort(SortStrategy):
    def sort(self, product_list, reverse):
        return sorted(product_list, key=lambda x: ascii(x.name), reverse=reverse)


class ProductSorter:
    def __init__(self, sort_strategy: SortStrategy):
        self.sort_strategy = sort_strategy

    def set_sort_strategy(self, sort_strategy: SortStrategy):
        self.sort_strategy = sort_strategy

    def sort(self, product_list, reverse=True):
        return self.sort_strategy.sort(product_list, reverse)


if __name__ == '__main__':
    products = [
        Product("Acer 232", 30000, 5, 4.7),
        Product("Asus Tuf", 45000, 7, 4.9),
        Product("Acer Nitro", 17000, 8, 3.7),
        Product("Lenovo Idea Pad", 23000, 10, 4),
        Product("Fujtutsu", 8000, 9, 4.5)
    ]
    product_sorter = ProductSorter(PriceSort())
    print('sort price')
    print([(product.name, product.price) for product in product_sorter.sort(products)])

    print('sort delivery')
    product_sorter.set_sort_strategy(DeliverySort())
    print([(product.name, product.delivery) for product in product_sorter.sort(products,False)])

    print('sort rating')
    product_sorter.set_sort_strategy(RatingSort())
    print([(product.name,product.rating) for product in product_sorter.sort(products)])

    print('sort name')
    product_sorter.set_sort_strategy(NameSort())
    print([product.name for product in product_sorter.sort(products, False)])
