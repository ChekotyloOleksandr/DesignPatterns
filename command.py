from abc import ABC, abstractmethod


class Player:
    def __init__(self, name):
        self.name = name

    def move_forward(self):
        print(f"{self.name} moving forward...")

    def jump(self):
        print(f"{self.name} jumping...")

    def attack(self):
        print(f"{self.name} attacking...")


class Command(ABC):
    def __init__(self, player):
        self.player = player

    @abstractmethod
    def execute(self):
        pass


class MoveForwardCommand(Command):
    def execute(self):
        self.player.move_forward()


class JumpCommand(Command):

    def execute(self):
        self.player.jump()


class ShootCommand(Command):

    def execute(self):
        self.player.attack()


class MultipleCommand(Command):
    def __init__(self, player, *commands):
        super().__init__(player)
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()


class Invoker:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def clear_commands(self):
        self.commands.clear()

    def run_commands(self):
        for command in self.commands:
            command.execute()


player = Player("Isaac")
invoker = Invoker()

invoker.add_command(MoveForwardCommand(player))
invoker.add_command(JumpCommand(player))
invoker.add_command(ShootCommand(player))
invoker.run_commands()
print()
invoker.clear_commands()
macro_command = MultipleCommand(player, JumpCommand(player), ShootCommand(player))
invoker.add_command(macro_command)
invoker.run_commands()