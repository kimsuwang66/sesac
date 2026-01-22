from device import AirConditioner, Light
from smarthub import SmartHub

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
myhub.turn_on_all()

myhub.device_list[0].turn_off()
# [0]로 접근하기 힘드니, 
# 사실 device_list는 딕셔너리가 어울릴지도?

from .something.aaa import text
print(text)