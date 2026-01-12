# if문 뒤에는 condition

if True:
    print('True')

if 1 < 3:
    print('1 < 3')

# 값이 존재한다 -> True

if 5:
    print(5)

if -3:
    print(-3)

if 'abc':
    print('abc')

if ' ':
    print('공백')

if [1, 2, 3]:
    print('[1, 2, 3]')

# 값이 존재하지 않는다 -> False


if 0:
    pass
else:
    print('false', 0)

if '':
    pass
else:
    print('false', '빈문자열')

if []:
    pass
else:
    print('false', '빈 리스트')
