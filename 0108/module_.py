# 내장함수 - python이 만들어놓은 함수.
print(1) # 프린트라는 함수를 안만들어도 사용이 가능합니다.
# sum()
# max()
# min()
# 자주 쓰일 것 같은 함수들은 미리 만들어놨습니다.

import math # math라는 모듈을 불러올꺼야.

print(math.ceil(3.12))
# ceil(3.12) # 올림이라는 기능은 우리가 자주 사용 안합니다.

import random

print(random.sample([1, 2, 3, 4], 2))


# 불러오는 방식
# 1. 바로 import하고, 사용할때 `.`을 사용해서 명시하기

import math

math.ceil(2.14)

# 2. 불러올 때 어떤 것을 사용할지 명시합니다.

from math import ceil
from math import * # math안의 모든 함수를 불러온다.

ceil(3.14)

import my_module

my_module.my_func()

# 1. python 내부의 module
# 2. 내가 만든 파일을 module
# 3. 누군가가 만든 파일을 다운받아서 사용