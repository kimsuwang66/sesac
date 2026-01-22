from vending_machine import VendingMachine
class Person:
    
    def __init__(self):
        # 내가 지불 가능한 결제 방식들.
        self.wallet = {
            # 이름 : Payment()
            # 의 형태
        }

    def run(self, vm: VendingMachine):
        # self : person instance.
        # vm.run(self)
        vm.run(self.wallet)

    def add_payment(self, payment):
        self.wallet[payment.name] = payment

    def show_budget(self):
        for key, value in self.wallet.items():
            print(key, value.money)


