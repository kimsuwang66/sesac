# ## 게임의 캐릭터 운영 규칙

# ### 1. 캐릭터는 이름과 역할을 가지고 태어납니다.

# 우리 게임의 모든 캐릭터는 이름표를 달고, 자기가 무엇을 하는 사람인지 역할을 정해서 태어납니다. 이름이 없거나 역할이 정해지지 않은 상태로는 게임 세상에 발을 들일 수 없습니다.

# ### 2. 어떻게 싸우는지는 역할에 따라 결정됩니다.

# 모든 캐릭터에게 똑같이 공격하라고 명령을 내려도, 그 사람이 맡은 역할에 따라 행동이 달라집니다.

# - 전사 역할을 맡은 사람에게 명령하면 본능적으로 검을 휘두르며 나갑니다.
# - 마법사 역할을 맡은 사람에게 명령하면 자연스럽게 마법을 주문처럼 외우며 나갑니다.
# 캐릭터가 손에 무엇을 들었느냐와 상관없이, 그 사람이 평생 배워온 싸움의 방식이 나오는 것입니다.

# ### 3. 도구(무기)는 아무나 들 수 없습니다.

# 이 세상에는 검이나 지팡이 같은 다양한 도구들이 있습니다. 각 도구에는 그 도구만이 가진 필살기가 하나씩 숨겨져 있죠. 하지만 아무나 이 도구를 집어 들 수 있는 건 아닙니다.

# - 각 역할마다 이런 종류의 도구만 써도 좋다는 허가 리스트가 있습니다.
# - 만약 전사에게 지팡이를 쥐여주려고 하면, 전사는 나는 이런 건 배운 적이 없어서 못 써요라며 거절합니다. 오직 허락된 도구인 검을 줄 때만 기쁘게 받아들여 손에 쥡니다.

# ### 4. 무기를 들어야만 필살기를 씁니다.

# 캐릭터에게 무기에 숨겨진 기술을 써보라고 시켰을 때의 상황입니다.

# - 손에 무기가 있다면: 그 무기에 적혀 있는 화려한 필살기를 사용합니다. 예를 들어 검이라면 강력한 베기 같은 기술이 나갑니다.
# - 맨손이라면: 지금 내 손에 든 게 없는데 무엇을 쓰나요라고 당황해합니다. 즉, 무기를 제대로 장착했을 때만 가능한 행동입니다.

# 공통 기능은 Character에서

from abc import ABC, abstractmethod

# class GameServer: #여기에 캐릭터 이름, 직업, 장착무기정보 보관
#     def __init__(self):
#         self.characters={}

class Character(ABC):
    def __init__(self,name,role):
        self.name=name
        self.role=role
        self.current_weapon=None

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def equip(self,weapon):
        pass

    def use_skill(self):
        if self.current_weapon:
            print(self.name,"skill")
        else:
            print("맨손")
        

class Warrior(Character):
    def attack(self):
        if self.current_weapon:
            print(f"{self.name} 전사공격")
        else:
            print(f"{self.name} 무기없음")

    def equip(self,weapon):
        if weapon.weapon_type == 'sword':
            self.current_weapon = weapon
            print(f"{self.name}이 {weapon.name}을 장착")
        else:
            print(f"{self.name}은 {weapon.name}은 못써")
class Mage(Character):
    def attack(self):
        if self.current_weapon:
            print(f"{self.name} 법사공격")
        else:
            print(f"{self.name} 무기없음")

    def equip(self,weapon):
        if weapon.weapon_type == 'wand':
            self.current_weapon = weapon
            print(f"{self.name}이 {weapon.name}을 장착")
        else:
            print(f"{self.name}은 {weapon.name}은 못써")
        
class Weapon:
    def __init__(self,name,weapon_type):
        self.name=name
        self.weapon_type=weapon_type
    
    
# 1. 무기들 준비
sword = Weapon("강철 검",'sword')
staff = Weapon("생명의 지팡이",'wand')

# 2. 캐릭터 생성
p1 = Warrior("아라곤", "전사")
p2 = Mage("간달프", "마법사")

# 3. 장착 및 액션
p1.equip(staff)
p1.equip(sword)
p1.attack()
p1.use_skill()

p2.attack()
p2.equip(sword)
p2.equip(staff)
p2.use_skill()
p2.attack()

# 4. 무기 없는 상태 테스트
p3 = Warrior("초보자", "전사")
p3.attack()



