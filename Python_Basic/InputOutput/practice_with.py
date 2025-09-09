# 파일을 처리할때 열고 닫는 작업을 할때 with를 사용하면 편하게 쓸 수 있음.
# import pickle
# with open("profile.pickle", "rb") as profile_file: #profile_file이라는 변수에 저장하겠다.
#     print(pickle.load(profile_file)) # with문을 탈출할때 자동으로 close시켜줌

# pickle을 사용하지 않는 일반 파일을 열고 닫기 with "with"
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())