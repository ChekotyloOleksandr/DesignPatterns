from abc import abstractmethod, ABC


class CharacterBuilder(ABC):
    def __init__(self):
        self.character = None

    def add_name(self, name):
        self.character.name = name

    @abstractmethod
    def add_weapon(self):
        pass

    @abstractmethod
    def add_speed(self):
        pass

    @abstractmethod
    def add_role(self):
        pass

    def create_character(self):
        self.character = Character()

    def get_character(self):
        return self.character

    def add_skills(self, skills):
        self.character.skills = skills


class WarriorBuilder(CharacterBuilder):

    def add_weapon(self):
        self.character.weapon = 'Sword'

    def add_armor(self):
        self.character.armor = 20

    def add_speed(self):
        self.character.speed = 310

    def add_role(self):
        self.character.role = 'Warrior'


class ArcherBuilder(CharacterBuilder):

    def add_weapon(self):
        self.character.weapon = "Bow"

    def add_armor(self, armor):
        self.character.armor = 0

    def add_speed(self):
        self.character.speed = 280

    def add_role(self):
        self.character.role = 'Archer'


class Character:
    def __init__(self):
        self.name = None
        self.role = None
        self.weapon = None
        self.armor = None
        self.speed = None
        self.skills = None

    def __str__(self):
        return f"Character is {self.role}. Name - {self.name}. His weapon - {self.weapon}, armor - {self.armor}," \
               f"speed- {self.speed}, skills - {self.skills} "


class Director:
    def __init__(self, builder):
        self.builder = builder

    def create_character(self, name, skills):
        self.builder.create_character()
        self.builder.add_name(name)
        self.builder.add_role()
        self.builder.add_speed()
        self.builder.add_weapon()
        self.builder.add_skills(skills)
        return self.builder.get_character()


if __name__ == "__main__":
    warrior_builder = WarriorBuilder()
    archer_builder = ArcherBuilder()
    director = Director(warrior_builder)
    warrior = director.create_character("Maestro", ['Chrono', "Eclipse"])
    print(warrior)
    director.builder = archer_builder
    archer = director.create_character("Windranger", ["ult", "arrow"])
    print(archer)
