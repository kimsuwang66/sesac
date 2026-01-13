import math
import random
from pprint import pprint

names_1 = ['강성신', '김수왕', '김진우', '남건우',
        '박세형', '박지훈', '서현석',  '이상준', 
        '이상호', '이종혁', '이채훈', '한다솔' ]
names_2 = ['김아네스', '배은하', '사비카', '이지선', 
         '주현지', '최유리', '하재연', '황희연']


names = names_1 + names_2

# 결석 로직
absent_people = []
while True:
    absent_person = input('결석자 입력 \n')
    

    if absent_people not in names:
        break


    if absent_person in names_1:
        names_1.remove(absent_person)
        absent_people.append(absent_person)

    if absent_people in names_2:
        names_2.remove(absent_person)
        absent_people.append(absent_person)


print(f'결석자 : {absent_people}')


# 섞음.
random.shuffle(names_1)
random.shuffle(names_2)

names_lengh_1 = len(names_1)
names_lengh_2 = len(names_2)



n = int(input('몇명 한 조 할까요?'))



group_count = math.ceil((names_lengh_1 + names_lengh_2) / n)
print(group_count)


teams = []
for _ in range(group_count):
    teams.append([]) 

i = 0
while i < names_lengh_1:
    name = names_1[i]

    team_index = i % group_count
    team = teams[team_index]

    team.append(name)
    i += 1

while i < names_lengh_2 + names_lengh_1:
    index = i - names_lengh_1
    name = names_2[index]

    team_index = i % group_count
    team = teams[team_index]

    team.append(name)
    i += 1


for i in range(group_count):
    team = teams[i]

    print(f"{i+1}번 팀 :", *team)