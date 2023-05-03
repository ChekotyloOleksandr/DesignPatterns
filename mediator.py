class User:
    def __init__(self, name):
        self._name = name
        self._mediator = None

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator

    def send(self, message):
        print(f"{self._name} sends message: {message}")
        self.mediator.send(self, message)

    def receive(self, message):
        print(f"{self._name} receives message: {message}")


class Chat:
    def __init__(self, user1: User, user2: User):
        self.user1 = user1
        self.user2 = user2
        self.user1.mediator = self
        self.user2.mediator = self

    def send(self, sender, message):
        self.user1.receive(message) if sender == self.user2 else self.user2.receive(message)


if __name__ == "__main__":
    user1 = User("Isaac")
    user2 = User("Eden")
    chatroom = Chat(user1, user2)
    user1.send('Hello')
    user2.send("Hi")
