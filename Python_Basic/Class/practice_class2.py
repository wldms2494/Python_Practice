class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit ):
    def __init__(self):
        # super().__init__() # 다중 상속시에는 첫번째 부모 클래스의 생성자만 호출됨
        Unit.__init__(self)
        Flyable.__init__(self)
    

# 드랍쉽 만들기
dropship = FlyableUnit()