import math
import random
from pprint import pprint

names = [
    '강성신', '김수왕', '김아네스', '김진우', '남건우', 
    '박세형', '박지훈', '배은하', '사비카', '서현석', 
    '이상준', '이상호', '이종혁', '이지선', '이채훈', 
    '주현지', '최유리', '하재연', '한다솔', '황희연'
    ]

# 결석 로직
absent_people = []
while True:
    absent_person = input('결석자 입력 \n')

    if absent_person not in names:
        break
    if absent_person in names:
        names.remove(absent_person)
        absent_people.append(absent_person)

print(f'결석자 : {absent_people}')

    




# 섞음.
random.shuffle(names)
names_lengh = len(names)


# n명의 인원으로 조를 짜고 싶다.
# n = 4
n = int(input('몇명 한 조 할까요?'))

# n으로 나눠 떨어지면 그대로 쓴다.
# n으로 나누어 떨이지지 않으면 1을 더한다.
# 나누고 올림한다.

group_count = math.ceil(names_lengh / n)
print(group_count)

# 내가 바라는 data의 형태이다.
# team1 = [a, b, c, d, ]
# team2 = [e, f, g, h]

# teams = [team1, team2, ..., teamn]

# teams = [[] for _ in range(group_count)]
teams = []
for _ in range(group_count):
    teams.append([]) # team에 대한 그릇.

# print(names)
# print(teams)

for i in range(names_lengh):
    name = names[i]

    team_index = i % group_count
    team = teams[team_index]

    team.append(name)

for i in range(group_count):
    team = teams[i]

    print(f"{i+1}번 팀 :", *team)