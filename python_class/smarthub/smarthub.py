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
