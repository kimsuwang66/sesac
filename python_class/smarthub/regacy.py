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



class SmartHub:

    def __init__(self):
        self.device_list = []

    def register_device(self, device):
        # 디바이스를 입력받아서
        # 나의 디바이스 목록에 넣자.
        # 입력받은 device가 진짜 Device 맞니?
        self.device_list.append(device)

    def turn_on_all(self):
        for device in self.device_list:
            # device가 turn_on 가진게 맞니?
            device.turn_on()

ac = AirConditioner()
# ac.show_status()
# ac.turn_on()
# ac.show_status()

light = Light()
# light.turn_on()
# light.show_status()

myhub = SmartHub()
myhub.register_device(ac)
myhub.register_device(light)
myhub.register_device('헤헤 로봇')
# myhub.turn_on_all()