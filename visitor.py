from abc import ABC, abstractmethod


class Place(ABC):
    def __init__(self, ticket_price):
        self.ticket_price = ticket_price

    @abstractmethod
    def accept(self, visitor):
        pass


class Museum(Place):
    def accept(self, visitor):
        visitor.visit_museum(self)


class Park(Place):
    def accept(self, visitor):
        visitor.visit_park(self)


class Zoo(Place):
    def accept(self, visitor):
        visitor.visit_zoo(self)


class Visitor(ABC):
    @abstractmethod
    def visit_museum(self, museum):
        pass

    @abstractmethod
    def visit_park(self, park):
        pass

    @abstractmethod
    def visit_zoo(self, zoo):
        pass


class ChildVisitor(Visitor):
    def visit_museum(self, museum):
        print(f"Максим посетил музей и заплатит {museum.ticket_price / 2} грн")

    def visit_park(self, park):
        print(f"Максим посетил парк и заплатит {museum.ticket_price / 2} грн")

    def visit_zoo(self, zoo):
        print(f"Максим посетил зоопарк и заплатит {museum.ticket_price / 2} грн")


class AdultVisitor(Visitor):
    def visit_museum(self, museum):
        print(f"Никита посетил музей и заплатит {museum.ticket_price} грн")

    def visit_park(self, park):
        print(f"Никита посетил парк и заплатит {museum.ticket_price} грн")

    def visit_zoo(self, zoo):
        print(f"Никита посетил зоопарк и заплатит {museum.ticket_price} грн")

if __name__ == '__main__':

    museum = Museum(50)
    park = Park(70)
    zoo = Zoo(0)

    child_visitor = ChildVisitor()
    adult_visitor = AdultVisitor()
    print("Никите 30, Максиму 10")
    museum.accept(child_visitor)
    museum.accept(adult_visitor)
    park.accept(child_visitor)
    park.accept(adult_visitor)
    zoo.accept(child_visitor)
    zoo.accept(adult_visitor)