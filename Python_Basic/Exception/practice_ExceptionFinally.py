class BigNumberError(Exception):
    pass


try:    
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요"))
    num2 = int(input("두번쨰 숫자를 입력하세요"))
    if num1 >= 10 or num2 >= 10 :
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리만 입력해주세요")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한자리만 입력하세요")
    print(err)

finally:
    print("계산기를 이용해 주셔서 감사합니다.")