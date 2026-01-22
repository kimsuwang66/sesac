from abc import ABC, abstractmethod
class Device(ABC):
    def __init__(self):
        self.is_activated = False

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def show_status(self):
        pass

# device1 = Device()
# device1.turn_on()


class AirConditioner(Device):

    def turn_on(self):
        print("에어컨 켜짐")
        self.is_activated = True

    def turn_off(self):
        print('에어컨 꺼짐')
        self.is_activated = False
        

    def show_status(self):
        print('현재온도 22도')
        print(f'에어컨 상태 : {self.is_activated}')


class Light(Device):

    def turn_on(self):
        print("라이트 켜짐")
        self.is_activated = True

    def turn_off(self):
        print('라이트 꺼짐')
        self.is_activated = False
        

    def show_status(self):
        print(f'조명 상태 : {self.is_activated}')

