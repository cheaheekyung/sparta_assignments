import random                                                              # 랜덤모듈 불러오기                                                                

while True :                                                               # 반복문
    Q_num = random.randint(1,10)                                           # 랜덤숫자 1~10 고르기
    print('랜덤 숫자 1~10이 생성됩니다 맞춰보세요')

    while True:                                                            # 반복문
        try :                                                              # try ~ except 구문으로 숫자 아닌 값에 예외처리
            A_num = int(input('예상숫자 >> '))                              # 사용자에게 숫자 input 받기
            
            if not (1 <= A_num <= 10):                                     # 1<= A_num <=10 가 아니면 continue로 다시 숫자 input으로 돌아가기             
                print("1과 10 사이의 숫자를 입력해주세요!")
                continue

            if Q_num < A_num :                                             # Q_num < A_num면 너무 커요 문구 출력
                print('떙! 너무 커요')  

            elif Q_num > A_num :                                           # Q_num > A_num면 너무 작아요 문구 출력
                print('땡! 너무 작아요')

            else :
                print('딩동댕 정답입니다.')                                 # 그 외(정답일 경우) 정답 문구 출력
                break

        except ValueError :
            print('잘못된 입력입니다. 숫자를 입력하세요')                    # try ~ except ValueError구문으로 숫자 아닌 값에 예외처리

    
    while True :                                                          # 한 판 더 ? 반복문 
        re_game = input('한 판 더 ? (y/n) >> ').lower()                   # y/n로 input 받고 .lower로 대소문자 모두 받음
        
        if re_game == 'y' :                                              # y일 경우 break
            break
        elif re_game == 'n' :                                            # n일 경우 끝! 출력 후 break
            print('끝!')
            break
        else :                                                           # y나 n 말고 다른걸로 입력할 경우 잘 못 입력했다는 구문 출력
            print('잘 못 입력하셨습니다. y나 n을 입력해주세요')
            continue
    
    if re_game == 'n' :                                                  # n일 경우 while 탈출
        break
