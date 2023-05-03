class ChatRoom:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def send_message(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive(message)


class User:
    def __init__(self, name):
        self.chat_room = None
        self.name = name

    def send(self, message):
        if self.chat_room:
            self.chat_room.send_message(message, self)
        else:
            print(self.name + " say " + message + " in the void")

    def receive(self, message):
        print(f"{self.name} receives message: {message}")

    def connect(self, chat_room):
        self.chat_room = chat_room
        chat_room.add_user(self)

    def disconnect(self):
        if self.chat_room:
            self.chat_room.remove_user(self)
            self.chat_room = None
            print(self.name + " disconnected.")


if __name__ == '__main__':
    chat_room = ChatRoom()
    user1 = User("Isaac")
    user2 = User("Azazel")
    user3 = User("Eden")
    user1.connect(chat_room)
    user2.connect(chat_room)
    user3.connect(chat_room)

    user1.send("QQ")
    user3.disconnect()
    user2.send("Hello Isaac")
    user3.send("Hello Isaac")
    user2.send("How are you?")
