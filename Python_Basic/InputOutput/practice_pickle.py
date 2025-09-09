# 피클은 프로그램상에서 우리가 사용하고 있는 데이터를 파일형태로 저장해줌
# 받은 파일 역시 피클로 열 수 있음. 
import pickle
# profile_file = open("profile.pickle", "wb") #b는 바이너리, 피클에서는 별도의 인코딩 설정이 필요 없음
# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # 피클 파일 불러오기 load
print(profile)
profile_file.close()