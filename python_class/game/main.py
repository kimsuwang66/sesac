from charater import Charater
from job import  Warrier, Mage
from weapon import Sword, Wand

me = Charater('아서', Warrier())
you = Charater('멀린', Mage())

sword = Sword('쌍고검')
wand = Wand('딱총나무 지팡이')

me.attack()
you.attack()

me.use_skill()

me.equip_weapon(sword)
me.use_skill()

me.equip_weapon(wand)
you.equip_weapon(wand)

me.job = Mage()