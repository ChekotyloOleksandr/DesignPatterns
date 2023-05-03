from abc import abstractmethod, ABC


class Fan:
    def __init__(self):
        self.state = OffState(self)

    def set_state(self, state):
        self.state = state

    def increase_speed(self):
        self.state.increase_speed()

    def turn_off(self):
        self.state.turn_off()

    def decrease_speed(self):
        self.state.decrease_speed()


class State(ABC):
    def __init__(self, fan):
        self.fan = fan

    @abstractmethod
    def increase_speed(self):
        pass

    def turn_off(self):
        print("Выключен")
        self.fan.set_state(OffState(self.fan))

    @abstractmethod
    def decrease_speed(self):
        pass


class OffState(State):
    def increase_speed(self):
        print("Включен на низкую скорость")
        self.fan.set_state(LowSpeedState(self.fan))

    def turn_off(self):
        print("Уже не работает ")

    def decrease_speed(self):
        print("Уже выключен")


class LowSpeedState(State):
    def increase_speed(self):
        print("Включен на среднюю скорость")
        self.fan.set_state(MediumSpeedState(self.fan))

    def decrease_speed(self):
        print("Выключен")
        self.fan.set_state(OffState(self.fan))


class MediumSpeedState(State):
    def increase_speed(self):
        print("Включен на высокую скорость")
        self.fan.set_state(HighSpeedState(self.fan))

    def decrease_speed(self):
        print("Включен на низкую скорость")
        self.fan.set_state(LowSpeedState(self.fan))


class HighSpeedState(State):
    def increase_speed(self):
        print('Это максимум')

    def decrease_speed(self):
        print("Включен на среднюю скорость")
        self.fan.set_state(MediumSpeedState(self.fan))


if __name__ == '__main__':
    fan = Fan()
    print(type(fan.state))
    fan.increase_speed()
    print(type(fan.state))
    fan.increase_speed()
    print(type(fan.state))
    fan.increase_speed()
    print(type(fan.state))
    fan.increase_speed()
    fan.turn_off()
    print(type(fan.state))
