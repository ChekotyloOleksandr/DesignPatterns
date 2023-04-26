from abc import ABC, abstractmethod


class MessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailSender(MessageSender):
    def __init__(self, email):
        self.email = email

    def send(self, message):
        print(f'Отправка на e-mail {self.email}')
        print(f'Сообщение: {message}')


class SMSSender(MessageSender):
    def __init__(self, phone):
        self.phone = phone

    def send(self, message):
        print(f'Отправка на номер {self.phone}')
        print(f'Сообщение: {message}')


class Message(ABC):
    def __init__(self, sender):
        self.sender = sender

    def send(self, message):
        self.sender.send(message)


class TextMessage(Message):

    def send(self, message):
        message = f'Текст: {message}'
        super().send(message)


class PngMessage(Message):
    def send(self, message):
        message = f'Картинка: {message}.png'
        super().send(message)


email_sender = EmailSender('example@example.com')
sms_sender = SMSSender('8-800-555-35-35')
png_email=PngMessage(email_sender)
text_email = TextMessage(email_sender)
text_email.send('Отправка по емейлу')
png_email.send('Picture')
print()
png_sms=PngMessage(sms_sender)
text_sms = TextMessage(sms_sender)
png_sms.send('Picture')
text_sms.send('Отправка по смс')
