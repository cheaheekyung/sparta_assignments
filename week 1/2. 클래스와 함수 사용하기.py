class person :                                                                     # person 이라는 클래스 정의
    def __init__(self, name, gender, age) :                                        # __init__ 으로 name, gender, age 정의 
        self.name = name
        self.gender = gender
        self.age = age
    
    def display(self) :                                                            # display 함수 정의
        print(f"이름: {self.name}, 성별: {self.gender} \n나이: {self.age} ")        # F-string 사용이름, 성별 나오고 줄바꿈 후 나이 출력
    
   
    def greet(self) :                                                              # greet 함수 정의
        if self.age >19 :                                                          # 조건문 활용하여 연령에 따라 두가지 메세지(성인, 미성년자) 출력
            print(f"안녕하세요, {self.name}! 성인이시군요!")                         # F-string 사용
        else :
            print(f"안녕하세요, {self.name}! 미성년자시군요!")


print("정보를 입력해주세요. \n(성별은 'male' 또는 'female'로 표기)")                   # 정보를 입력알림 출력    

while True :                                                                        # 반복문을 사용하여 나이 입력받고, 유효성검사 실시
    try :
        user_age = int(input("나이: "))                                              # 숫자를 입력하면 반복문 탈출
        break
    except ValueError :
        print('숫자를 입력해주세요')                                                  # 숫자가 아니라면 valueerror로 다시 입력

user_name = input("이름: ")                                                          # 유저이름 입력 받음
   
while True:                                                                          # 반복문 사용하여 성별 입력받고, 유효성검사 실시
    user_gender = input("성별: ").lower()                                            # .lower 사용하여 대소문자 모두 인식하도록 함
    if user_gender not in ['male', 'female'] :                                       # male, female이 아닌경우 다시 입력하도록 함.
        print('잘 못 입력하셨습니다. male 또는 female을 입력하세요')
    else :                                                                           # 제대로 입력하면 반복문 탈출
        break


user= person(user_name, user_gender, user_age)                                       # 유저들의 입력값을 person 클래스에 저장
user.display()                                                                        # display 실행
user.greet()                                                                          # greet 실행  
