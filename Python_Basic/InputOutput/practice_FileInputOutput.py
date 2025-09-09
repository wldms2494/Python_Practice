# score_file = open("score.txt", "w", encoding="utf8")
# print("수학:0", file=score_file)
# print("영어:50", file=score_file)
# score_file.close()

# score_file = open("score.txt","a", encoding="utf8") # a는 append, 엎어쓰기
# score_file.write("과학:80")
# score_file.write("\n코딩:100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8" )
# print(score_file.read())
# score_file.close()


#한줄씩 읽어줌, 자동줄바꿈 기능까지 있어서 end=""처리 안하면 한줄 더 띄워짐
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") 
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

#총 몇줄인줄 모르는데 한줄한줄 읽을 수 없잖앙
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

#리스트로 처리할 수도 있음
score_file = open("score.txt", "r", encoding="utf8")
lines= score_file.readlines() # 리스트 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()