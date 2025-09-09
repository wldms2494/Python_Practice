# 속도가 리스트보다 빠르나 추가하거나 제거할 수 없다. 변경되지 않는 리스트를 쓸때 사용

menu = ("돈까쓰", "치즈돈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까쓰") -> 에러

name = "김종국"
age = 20
hobby = "코딩"

name, age, hobby = "김종국", 20, "코딩" # = (name, age, hobby) = ("김종국", 20, "코딩")  튜플은 괄호 활용

print(name, age, hobby)

