# Set (집합) ; 중복안됨, 순서없음
my_set = {1,2,3,3,3} #Dictionary도 중괄호를 썼지만 키값이 없은게 다름
print(my_set)


java_develop = {"유재석", "김태호", "양세형"}
python_develop = set(["유재석", "박명수"]) 

# 교집합을 출력(java와 python이 모두 가능한 사람)
print(java_develop & python_develop)
print(java_develop.intersection(python_develop))

# 합집합( java나 python이 하나라도 가능한 사람)
print(java_develop | python_develop)
print(java_develop.union(python_develop))

# 차집합 (Java는 할 수 있지만 Python은 할 수 없는 개발자)
print(java_develop - python_develop)
print(java_develop.difference(python_develop))


# 파이썬을 할 줄 아는 사람이 늘어남
python_develop.add("김태호")
print(python_develop)

java_develop.remove("김태호")
print(java_develop)