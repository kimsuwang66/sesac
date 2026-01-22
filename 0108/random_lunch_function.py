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
def remove_absent_person(names):
    absent_people = []
    while True:
        absent_person = input('결석자 입력 \n')

        if absent_person not in names:
            break
        if absent_person in names:
            names.remove(absent_person)
            absent_people.append(absent_person)

    print(f'결석자 : {absent_people}')

    return names

def get_group_count():
    n = int(input('몇명 한 조 할까요?'))
    group_count = math.ceil(names_lengh / n)
    return group_count

def get_random_team():
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
    return teams

def print_teams(teams):
    for i in range(group_count):
        team = teams[i]

        print(f"{i+1}번 팀 :", *team)

# 결석자 제외
names = remove_absent_person(names)

names_lengh = len(names)
# 랜덤으로 섞어
random.shuffle(names)

# 조 개수 찾아
group_count = get_group_count()

# 조 만들어
teams = get_random_team()

print_teams(teams)
