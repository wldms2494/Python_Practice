# 지역변수와 전역변수

# gun =10 #총이 총 10자루

# def checkPoint(soldiers):
#     gun = gun-soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총: {0}".format(gun))
# checkPoint(2) #2명이 경계 근무로 나감
# print("남은 총 : {0}".format(gun))


# L 이대로 호출하면 checkpoint에서 gun을 찾지 못해 오류가 남

gun =10 #총이 총 10자루

def checkPoint(soldiers):
    global gun # 전역 공간에 있는 gun을 사용
    gun = gun-soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총: {0}".format(gun))
checkPoint(2) #2명이 경계 근무로 나감
print("남은 총 : {0}".format(gun))

# 전역변수를 너무 많이 사용하면 코드 관리가 어려워 질 수 있어서 가급적 함수의 파라미터로 계산을 하고 반환값을 사용함 

def checkpoint_return(gun, soldiers):
    gun = gun-soldiers
    print("함수 내 남은 총 : {0}", format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_return(gun, 2)
print("남은 총 : {0}".format(gun))