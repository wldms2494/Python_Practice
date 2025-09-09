
# import travel.thailand # 클래스나 함수는 import를 직접 할 수 없고 모듈이나 패키지만 가능 . 
# trip_to = travel.thailand.ThailandPackage() # 객체 생성
# trip_to.detail() # 메서드 호출

# from travel.thailand import ThailandPackage # from ~ import 구문으로 모듈에서 클래스 직접 가져오기
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import * (랜덤에 있는 함수 모두 쓸꺼야)
from travel import *
# # trip_to = vietnam.VietnamPackage() 
# # L 그냥 이것만 쓰면 에러 발생 , *을 쓴다는것은 travel의 모든것을 가져 오겠다는건데 공개 범위를 설정해줘야함
# # L __init__.py에서 __all__ = ["vietnam"] 으로 설정해줘야함

# trip_to = thailand.ThailandPackage() 

# trip_to.detail()

import inspect
import random

print(inspect.getfile(random))  # random 모듈이 저장된 위치 출력
print(inspect.getfile(thailand))  # travel 패키지가 저장된 위치 출력