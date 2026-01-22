# 1. 고차 함수이자 데코레이터 역할을 할 함수 정의
def activity_logger(original_func):
    # 내부에서 실제 동작을 감싸는 'wrapper' 함수를 만듭니다.
    def wrapper(person):
        print("--- 활동 기록을 시작합니다 ---")
        result = original_func(person)  # 원래 함수 실행
        print(f"결과: {result}")
        print("--- 활동 기록이 종료되었습니다 ---")
        return result
    
    return wrapper  # 함수 자체를 반환함 (고차 함수의 특징)

# 2. @ 기호를 이용해 함수를 '장식'합니다.
@activity_logger
def run(person):
    return f"{person.name}이(가) 신나게 달립니다."

@activity_logger
def sleep(person):
    return f"{person.name}이(가) 깊은 잠을 잡니다."

# 3. 호출할 때는 고차 함수를 부를 필요 없이 함수명만 부르면 됩니다.
class Person:
    def __init__(self, name):
        self.name = name

p = Person(test,"성춘향")

run(p)   # 실행하면 자동으로 로그가 찍힙니다!
sleep(p) # 실행하면 자동으로 로그가 찍힙니다!