class Hero:
    def __init__(self, name: str, weapon: str, health: int):
        self.name = name
        self.weapon = weapon
        self.health = health


class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Save:
    def __init__(self):
        self._mementos = []

    def add_save(self, memento):
        self._mementos.append(memento)

    def get_save(self, index):
        return self._mementos[index]

    def get_all_saves(self):
        return self._mementos

    def load(self, index):
        if 0 <= index < len(self._mementos):
            return self.get_save(index).get_state()


if __name__ == '__main__':
    hero = Hero("Isaac", 'Bow', 40)
    print(f"New hero - {hero.name} has {hero.health} hp, equipment - {hero.weapon}")
    saves = Save()
    saves.add_save(Memento([hero.name, hero.weapon, hero.health]))
    print('Hero defeat ogre')
    hero.health, hero.weapon = 30, "Sword"
    print(f"{hero.name} has {hero.health} hp, equipment - {hero.weapon}")
    saves.add_save(Memento([hero.name, hero.weapon, hero.health]))
    print('Choose save')
    for i,memento in enumerate(saves.get_all_saves()):
        name, weapon, health = memento.get_state()
        print(f"{i} - {name} has {health} hp, equipment - {weapon}")
    print()
    print('Loading save.....')
    hero.name, hero.weapon, hero.health = saves.load(0)
    print(f"{hero.name} has {hero.health} hp, equipment - {hero.weapon}")
