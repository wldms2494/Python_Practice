# List 
subway = ["유재석","조세호","박명수"]
print(subway)
# 조세호는 몇번째칸 ? 
print(subway.index("조세호"))
print(subway)
# 하하는 다음 정류장에서 다음칸에 탐
subway.append("하하") # 가장 마지막 번째로 추가됨
print(subway)
# 정형돈을 유재석 다음으로 추가
subway.insert(1, "정형돈")
print(subway)

#지하철에 있는 사람을 한명씩 뒤에서 꺼내기
# subway.pop()
# print(subway)
# subway.pop()
# print(subway)
# subway.pop()
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway.count("유재석"))


# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()

print(num_list)

# 뒤집기도 가능
num_list.reverse()
print(num_list)

# 모두다 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5,4,3,2,1]
mix_list = ["조세호", 20, True]

print(mix_list)

# list 확장
num_list.extend(mix_list)
print(num_list)