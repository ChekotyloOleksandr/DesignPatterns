from abc import ABC, abstractmethod


class MessageSender(ABC):

    @abstractmethod
    def send(self):
        pass


class EmailSender(MessageSender):
    def __init__(self, email, massage):
        self.email = email
        self.massage = massage

    def send(self):
        print(f'Отправка на e-mail {self.email}')
        print(f'Сообщение: {self.massage.get_message()}')


class SMSSender(MessageSender):
    def __init__(self, phone, message):
        self.phone = phone
        self.message = message

    def send(self):
        print(f'Отправка на номер {self.phone}')
        print(f'Сообщение: {self.message.get_message()}')


class Message(ABC):
    def __init__(self, message):
        self.message = message

    @abstractmethod
    def get_message(self):
        pass


class TextMessage(Message):

    def get_message(self):
        return f'Текст: {self.message}'


class PngMessage(Message):
    def get_message(self):
        return f'Картинка: {self.message}.png'


png_email = PngMessage('Picture')
text_email = TextMessage('Text')
email_sender = EmailSender('example@example.com', png_email)
sms_sender = SMSSender('8-800-555-35-35', png_email)
email_sender.send()
sms_sender.send()
print()
email_sender = EmailSender('example@example.com', text_email)
sms_sender = SMSSender('8-800-555-35-35', text_email)
email_sender.send()
sms_sender.send()
