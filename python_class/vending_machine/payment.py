from abc import ABC, abstractmethod

class Payment(ABC):
    
    def __init__(self, money: int, name: str):
        # 결제 한도 금액
        self.name = name
        self.money = money

    def pay(self, price):
        if self.money >= price:
            self.money -= price
            return True
        
        elif self.money < price:
            return False


    def __str__(self):
        return f"{self.name}"

class CardPayment(Payment):
    
    def __init__(self, money, name, total_money):
        super().__init__(money, name)
        # 지금까지 얼마 썼는지
        self.total_money = total_money

    def pay(self, price):
        self.total_money += price
        print('카드결제 완료')
        return super().pay(price)

class CashPayment(Payment):
    
    def pay(self, price):
        print('현금결제 완료')
        # 거스름돈 계산
        return super().pay(price)
    