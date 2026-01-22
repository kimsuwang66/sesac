lst1 = [8, 2, 5, 1, 9, 3, 23]

result_lst1 = lst1.sort()
print('lst1', lst1)
print('result_lst1', result_lst1)
###########################
lst2 = [8, 2, 5, 1, 9, 3, 23]

result_lst2 = sorted(lst2)
print('lst2', lst2)
print('result_lst2', result_lst2)

data = [
    [1, 10], 
    [10, 5], 
    [5, 20]
    ]

def func(el):
    return el[1]

print(sorted(data, key=func))
print(sorted(data, key=lambda el : el[1]))

def func2(el):
    return sum(el)
print(sorted(data, key=func2))
print(sorted(data, key=lambda el : sum(el)))

data = [
    {
        'name' : 'jun',
        'math' : 100,
        'korean' : 50
    },
    {
        'name' : 'ken',
        'math' : 20,
        'korean' : 80
    },
    {
        'name' : 'alex',
        'math' : 80,
        'korean' : 40
    },
]
print(sorted(data, key=lambda el : el['math']))
print(sorted(data, key=lambda el : el['math'], reverse=True))