# 구글에서 List of python Modules를 검색 -> 외장함수 목록을 볼 수 있음.

# glob : 경로 내의 폴더 / 파일 목록을 조회 ( 윈도우의 dir 과 비슷 )
import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일


# os : 운영체제에서 제공하는 기본 기능
import os
# # print(dir(os))
# print(os.getcwd()) # 현재 디렉토리 표시
# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder) # 폴더 삭제
#     print(folder, "폴더를 삭제합니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성합니다.")

# print(os.listdir()) # 현재 디렉토리의 모든 파일과 폴더를 표시

import time
# print(time.localtime()) # 현재 시간 표시
# print(time.strftime("%Y-%m-%d %H:%M:%S")) # 내가 원하는 형태로 시간 표시

import datetime
print("오늘 날짜는 ",datetime.date.today()) # 오늘 날짜 표시

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은 ", today + td)

target= datetime.date(2025, 12, 25)
diff = target - today
print("오늘부터 크리스마스까지 남은 일수:", diff)