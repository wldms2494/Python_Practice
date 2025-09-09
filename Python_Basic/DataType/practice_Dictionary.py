cabinet = {3:"유재석", 100:"김태호"}
print(cabinet)
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) -> 없는 키는 오류 발생
print(cabinet.get(5)) # 값이 없으면 None 출력
print(cabinet.get(5, "사용가능")) # 값이 없으면 지정해놓은 값을 출력
print("하이")

# 사전안에 값이 있는지 확인
print(3 in cabinet)
print(5 in cabinet)


cabinet2 = {"A-3" : "송지은", "B-20" : "이지우"}
print(cabinet2["A-3"])
cabinet2["C-20"] = "박지원" # 만약에 존재하는 키라면 값이 업데이트가 됨
print(cabinet2)

# 가버린 손님
del cabinet2["A-3"]

print(cabinet2)

# 키들만 출력
print(cabinet2.keys())

# value만 출력
print(cabinet2.values())

# key, value 쌍으로 출력
print(cabinet2.items())

# 목욕탕 폐점.  cabinet 값 없애기
cabinet2.clear()

print(cabinet2)