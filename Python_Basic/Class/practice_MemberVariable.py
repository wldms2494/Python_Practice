class Unit:
    def __init__(self, name, hp, damage):
        self.name = name # 멤버변수 name, 클래스 내에서 정의된 변수
        self.hp = hp # 멤버변수 hp, 클래스 내에서 정의된 변수
        self.damage = damage # 멤버변수 damage, 클래스 내에서 정의된 변수
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


# 레이스 : 공중 유닛
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력: {1}".format(wraith1.name, wraith1.damage))


