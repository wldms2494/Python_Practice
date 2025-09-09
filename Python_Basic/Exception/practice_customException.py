
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg= msg
    def __str__(self):
        return self.msg + '(__str__ 호출)'
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 > 10 or num2 >= 10:
        # raise ValueError
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # raise에서 초기화 함수__init__
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError: 
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err: 
    # err는 BingNumberError의 객체, 인스턴스임으로 err를 프린트하려면 __str__메서드가 호출됨
    print("에러가 발생하였습니다. 한자리 숫자만 입력해주세요")
    print(err)