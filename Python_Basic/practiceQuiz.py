# 자료형 퀴즈

from random import *
users = range(1,21) # users = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(type(users)) # range Type
users = list(users)
# print(type(users))
print(users)
shuffle(users)
print(users)

winners = sample(users, 4)
print(winners)

# print('''
# --- 당첨자 발표 ---
# 치킨 당첨자 : %s)      

# ''', "하이")
print("--- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피당첨자 : {0}".format(winners[1:]))
print(" -- 축하드립니다 --")


