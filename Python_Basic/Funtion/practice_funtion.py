# 함수 정의 방법 : def ():
def open_account(): 
    print("새로운 계좌가 개설되었습니다 .")


def deposit(balance, money) :
    print("입금이 완료되었습니다. 잔액이 {0}원입니다.".format(balance+money))
    return balance+money

balance = 0
balance = deposit(balance, 1000)

def withdraw(balnace, money) : 
    if balance > money : 
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance
    
balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)

def withdraw_night(balance, money): 
    commission = 100 #수수료 100원
    return commission, balance-money - commission # 튜플 형식으로 반환

commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1} 원입니다. ".format(commission, balance))

print('************************************************************************************************')

# 함수 기본값 설정
# .format을 다음줄로 넘겨도 \를 함께 쓰면 두 문장을 연결시킬 수 있음
# def profile(name, age=17, main_lang="파이썬") : 
#     print("이름:{0}\t 나이:{1}\t 주 사용 언어:{2}" \
#         .format(name, age, main_lang))

# # profile("유재석",20,"파이썬")
# profile("유재석")
# profile("김태호")

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=29) # 순서가 바뀌어도 괜찮
profile(main_lang="자바", age=30, name="김태호")

print('************************************************************************************************')
# 가변인자
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름:{0}\t 나이:{1}\t".format(name, age), end="") # end를 통해 다음 문장과 연결 가능, 안하면 줄바꿈으로 넘어감
    # print("이름:{0}\t 나이:{1}\t".format(name, age))
    print(lang1,lang2,lang3,lang4,lang5)

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 20, "Kotlin", "Siwft", "", "", "") # 항상 빈값 처리를 할 수 없음. 언어가 늘어나면 함수 파라미터 자체를 바꿔야함.

def profile(name, age, *language): # 가변인자
    print("이름:{0}\t 나이:{1}\t".format(name, age), end="")
    for lang in language:
        print(lang, end=" ")
    print()


profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 20, "Kotlin", "Siwft"  ) # 항상 빈값 처리를 할 수 없음. 언어가 늘어나면 함수 파라미터 자체를 바꿔야함.
