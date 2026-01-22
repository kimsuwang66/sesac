from abc import ABC, abstractmethod

class Product: #상품 정보는 여기에 담는 게 아님
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    
    # def __str__(self): # 여기서 정의하면 나중에 재고확인때 이대로 예쁘게 출력, 안하면 <__main__.Product object at 0x1017d4b90>
    #     return f"상품명: {self.name}   상품가격 : {self.price}   재고 : {self.stock}"
    

class Payment(ABC):
    @abstractmethod
    def process_payment(self,amount):
        pass

class Cash(Payment):
    def __init__(self,inserted_money):
        self.inserted_money=inserted_money

    def process_payment(self,amount):
        if self.inserted_money >= amount:
            print(f"{amount} 결제완료. 잔액 {self.inserted_money-amount} 원을 반환합니다.")
            return True
        else:
            print("투입금액이 부족합니다")
            return False

class Card(Payment):
    def __init__(self,card_limit):
        self.card_limit=card_limit

    def process_payment(self,amount):
        if self.card_limit >= amount:
            print(f"{amount}원을 결제했습니다. 카드 잔액은 {self.card_limit-amount}원 입니다.")
            return True
        else:
            print('카드 한도 초과')
            return False


class VendingMachine:
    def __init__(self):
        self.inventory=[]
    # def add_product(self,product):
    #     self.inventory.append(product)
    def add_products(self, *products):
        for product in products:
            self.inventory.append(product)
            print(f"{product.name} 등록 완료")    
    def stock_check(self):
        for p in self.inventory:
            print(p)

    def buy_product(self,product_name,payment_method):
        product=None
        for p in self.inventory:
            if product_name == p.name:
                product = p
                break
        if product is None:
            print(f"{product_name.name} 상품이 자판기에 없습니다")
            return
        if product.stock <= 0:
            print(f"{product.name}의 재고가 부족합니다")
            return

        if payment_method.process_payment(product.price):
            product.stock -= 1
            print(f"{product_name} 배출")
        else:
            print(f"{product_name} 결제에 실패했습니다.")        

vm1=VendingMachine()
coke = Product("콜라", 1500, 2)
sprite = Product("사이다",1200,15)
beer = Product("맥주",2000,5)
water = Product("생수",800,1)
vm1.add_products(coke,sprite,beer,water)

vm1.stock_check()
vm1.buy_product("콜라",Cash(1000))
vm1.buy_product("콜라",Cash(2000))
vm1.stock_check()
vm1.buy_product("생수",Card(500))
vm1.buy_product("생수",Card(10000))
vm1.buy_product("생수",Card(10000))