# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요? :")
# print("{0}은 아주 좋은 언어입니다.".format(language))

#dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 랜덤은 외장 함수
# print(dir()) # --> random이 추가된걸 볼 수 있음
# import pickle
# print(dir()) # --> pickle이 추가된걸 볼 수 있음


# import random # 랜덤은 외장 함수
# print(dir(random)) # random.까지 쳤을 때 쓸 수 있는 모든걸 보여줌 . 안에 뭐들었는지 보여줌


# lst = [1,2,3]
# print(dir(lst)) # list가 어떤 변수와 함수를 사용할 수 있는 지 알려줌

name= 'Jim'
print(dir(name))
