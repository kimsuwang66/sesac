class Person:
    def speak(self):
        print("사람이 말을 합니다.")

class Job:
    def speak(self):
        print("업무를 수행합니다.")

class Professional(Job, Person):
    # Person과 Job 클래스 모두를 상속받음
    pass

prof = Professional()
# 두 부모 클래스의 모든 메서드 사용 가능
prof.speak()

