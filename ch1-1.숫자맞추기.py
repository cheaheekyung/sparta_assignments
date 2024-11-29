#random모듈 불러오기
import random

#random 모듈 속 랜덤정수를 생성하는 randint 함수사용(1이상, 10이하)
Q_num = random.randint(1,10)

#사용자 입력값을 int로 받기
A_num = int(input('숫자를 맞춰보세요 (1~10 중 랜덤) >> '))

#반복을 위한 while문 사용
while True:
   
    #입력값이 문제보다 클 때, 크다는 문구 출력 후 다시 입력 받기
    if Q_num < A_num :
        print('떙! 너무 커요')  
        A_num = int(input('다시 입력하세요 >> '))
    
    #입력값이 문제보다 작을 때, 작다는 문구 출력 후 다시 입력 받기
    elif Q_num > A_num :
        print('땡! 너무 작아요')
        A_num = int(input('다시 입력하세요 >> '))

    #입력값과 문제가 같을 떄 정답입니다 출력
    else :
        print('딩동댕 정답입니다.')
        #while문 중단
        break