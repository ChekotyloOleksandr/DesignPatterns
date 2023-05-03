from abc import abstractmethod, ABC


class Character(ABC):
    def __init__(self):
        self.character = None

    def create_character(self, name, skills):
        self.character = Character()
        self.add_name(name)
        self.add_role()
        self.add_speed()
        self.add_armor()
        self.add_weapon()
        self.add_skills(skills)
        return self

    def add_name(self, name):
        self.character.name = name
    @abstractmethod
    def add_armor(self):
        pass
    @abstractmethod
    def perform_action(self):
        pass

    @abstractmethod
    def add_weapon(self):
        pass

    @abstractmethod
    def add_speed(self):
        pass

    @abstractmethod
    def add_role(self):
        pass

    def add_skills(self, skills):
        self.character.skills = skills


class Warrior(Character):

    def add_weapon(self):
        self.character.weapon = 'Sword'

    def perform_action(self):
        print(f"{self.character.name} бьет спец. удар мечом под названием {self.character.skills[0]}!")

    def add_armor(self):
        self.character.armor = 20

    def add_speed(self):
        self.character.speed = 310

    def add_role(self):
        self.character.role = 'Warrior'


class Archer(Character):
    def perform_action(self):
        print(f"{self.character.name} использует способонсть лука под названием {self.character.skills[0]}!")

    def add_weapon(self):
        self.character.weapon = "Bow"

    def add_armor(self):
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


if __name__ == "__main__":
    warrior = Warrior()
    archer = Archer()
    warrior = warrior.create_character("Maestro", ['Chrono', "Eclipse"])
    print(warrior.character)
    archer = archer.create_character("Windranger", ["ult", "arrow"])
    print(archer.character)
    archer.perform_action()
    warrior.perform_action()
