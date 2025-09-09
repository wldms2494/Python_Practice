# 자료구조 퀴즈
# Quiz 당신은 Cocoa 서비스 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오
# 조건 1 : 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야합니다. 

# 나의 답변 
# from random import *
# customers = list(range(1,51))

# matched =""
# totalCnt = 0


# for customer in customers :
#     elapsedTime = randint(1,10) * 5 
#     if elapsedTime >= 5 and elapsedTime <= 15 :
#         matched = "O"
#         totalCnt +=1
        
#     else :
#          matched = " "
         
#     print("[" + matched + "]"+str(customer)+"번째 손님 (소요시간 : "+str(elapsedTime)+"분)")

# print(f"""
# 총 탑승 승겍 : {totalCnt}분
# """)


# 선생님 답변
from random import *
cnt = 0
for i in range(1,51): # 1~50 d이라는 수 (승객)
    time = randrange(5, 51) #5분 ~ 50분 소요시간
    if 5 <= time <= 15: # 5분~ 15분 이내의 손님, 
        print("[O] {0}번째 손님 (소요시간 : {1}분)" .format(i, time)  )
        cnt += 1
    else : # 매칭이 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)" .format(i, time)  )

print("총 탑승 승객 : {0}".format(cnt))