print("Python", "Java") # , 로 구분 시 띄어쓰기가 자동
print("Python","Java", sep=" , ", end="?") # sep로 제어 가능 , end=""는 문장의 끝부분을 바꿔줌. 자동 줄바꿈 X
print("무엇이 더 재밌을까요? ")

import sys
print("Python", "Java", file=sys.stdout) # 표준 출력
print("Python", "Java", file=sys.stderr) # 표준에러를 따로 로깅 처리 가능

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): # key, value 출력 가능
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4)) #과목은 8칸의 공간을 확보하고 왼쪽정렬, 점수는 4개의 칸을 확보하고 오른쪽 정렬


# 은행 대기 순번표
# 001, 002, 003, ...
for num in range(1,21):
    print('대기번호: '+str(num).zfill(3)) # 3자리를 만들고 빈공간은 0으로 채움


answer = input("아무 값이나 입려하세요: ")
print("입력하신 값은 "+answer) # 숫자나 문자나 다 잘 출력 -> 사용자 입력을 받으면 무조건 문자로 
print(type(answer))