from abc import ABC, abstractmethod


class DBAbstract(ABC):
    @abstractmethod
    def get_data(self, query: str) -> str:
        pass


class DBReal(DBAbstract):
    def get_data(self, query: str) -> str:
        print(f"Запрос: {query}")
        return "Таблица "+query.split(' ')[-1]


class DBProxy(DBAbstract):
    def __init__(self):
        self._cache = {}
        self._service = DBReal()

    def get_data(self, query):
        if query in self._cache:
            print(f"Взято с кеша {query}")
            return self._cache[query]
        else:
            result = self._service.get_data(query)
            self._cache[query] = result
            return result


if __name__ == "__main__":
    service = DBProxy()
    for query in ["SELECT * FROM users", "SELECT * FROM orders", "SELECT * FROM products"]:
        print(service.get_data(query))
    print(service.get_data("SELECT * FROM users"))