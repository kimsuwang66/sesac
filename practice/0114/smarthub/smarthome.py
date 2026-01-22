# 여러기기 중앙관리
# ex)전부 키기/전부 끄기
# 기기(Device) - 일반클래스 / 추상클래스
#     -켜기()
#     -끄기()
#     -상태 확인하기() -  오버라이딩
# 에어컨(기기)
#     - 온도조절
# 조명(기기)
#     - 밝기조절
# Tv(기기)
#     - 채널변경
# 스마트 허브
#   -연결된 기기 : list
#   -연결하기()
#   상태확인 기능
#   전체 키기
#   전체 끄기
### [스마트 허브(SmartHub) 설계]

# - 허브는 `이름`과 `지원하는 연결 방식(Protocol)`을 속성으로 가집니다.
# - 허브는 여러 개의 `기기(Device)`를 저장할 수 있는 리스트를 가집니다.
# - 기능: `기기_등록()`, `전체_가동()`, `전체_중지()`.

# ### [기기(Device) 설계 - 추상 클래스]

# - 모든 기기는 `이름`, `제조사`, `연결 방식` 속성을 가집니다.
# - 기기 생성 시 이름과 연결 방식이 지정되어야 합니다.
# - 기능: `작동()`, `상태확인()` (추상 메서드).
# - **구현 클래스:** `스마트전등(SmartLight)`, `에어컨(AirConditioner)`을 생성하세요.

# ### [연결 방식(Protocol) 설계 - 추상 클래스]

# - 연결 방식은 `통신_시작()` 기능을 가집니다.
# - **구현 클래스:** `WiFiProtocol`, `ZigbeeProtocol`, `BluetoothProtocol`을 생성하세요.
# - 각 프로토콜은 `통신_시작()` 호출 시 "WiFi로 연결을 시도합니다", "Zigbee망을 구성합니다" 등 고유의 메시지를 출력합니다.

from abc import ABC, abstractmethod

class Smarthub:
    def __init__(self,name):
        self.devices=[]
        self.name=name
        
    def register_device(self,device):
        for new_device in self.devices:
            if new_device.name == device.name:
                print(f"{new_device.name} : 이미 등록되어 있습니다")#device.name 쓰던 new_device.name 쓰던 동일하게 출력됨
                return
        
        self.devices.append(device)
        print(f"{device.name}등록 완료")

    def turn_on_all(self):
        print(f"{self.name}, 전체 가동")
        for dev in self.devices:
            dev.power_on()
            

    def turn_off_all(self):
        print(f"{self.name}, 전체 종료")
        for dev in self.devices:
            dev.power_off()

   
    
class Device(ABC):
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
        self.is_activated = False #작동상태 기본 꺼짐
    
    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass

    @abstractmethod
    def status(self):
        pass


class SmartLight(Device):
    def power_on(self):
        print(f"{self.name} 전등을 켭니다")
        self.is_activated=True


    def power_off(self):
        print(f"{self.name} 전등을 끕니다")
        self.is_activated=False

    def status(self):
        print(f"{self.name}의 현재 상태는 {self.is_activated}")


class Airconditioner(Device):
    def power_on(self):
        print(f"{self.name} 에어컨을 켭니다")
        self.is_activated=True

    def power_off(self):
        print(f"{self.name} 에어컨을 끕니다")
        self.is_activated=False

    def status(self):
        print(f"{self.name}의 현재 상태는 {self.is_activated}")

myhub1=Smarthub('첫번째 허브')
print(myhub1.name)
for dev in myhub1.devices:
    print(dev.name)

myhub2=Smarthub('두번째 허브')
print(myhub2.name)
for dev in myhub2.devices:
    print(dev.name)

light1=SmartLight('거실등','중국산')
aircon1=Airconditioner('거실 에어컨','LG')

myhub1.register_device(light1)
myhub1.register_device(aircon1)
myhub2.register_device(aircon1)

light1.status()

for dev in myhub1.devices:
    print(f"{myhub1.name}에는 {dev.brand} {dev.name}이 있음")

for dev in myhub2.devices:
    print(f"{myhub2.name}에는 {dev.brand} {dev.name}이 있음")

myhub1.turn_on_all()
myhub2.turn_on_all()

light1.status()


# myhub1.register_device()
# for dev in myhub1.devices:
#     print(dev.name)

# myhub1.turn_on_all()