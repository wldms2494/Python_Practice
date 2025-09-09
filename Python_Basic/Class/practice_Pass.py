# 메소드 오버라이딩

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
              .format(self.name, location , self.speed) )
    
# 공격 유닛
class AttackUnit(Unit): # 상속을 받으려면 클래스명 우측에 괄호에 상속 받는 클래스를 넣어줌 
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed) 
        # L self.name = name 를 쓸 필요가 없음
        # L self.hp = hp 를 쓸 필요가 없음
        # L Unit 클래스에 있는 거 가져다가 쓰겠다.
        self.damage = damage

    def attck(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
              .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다. ".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기. 공격 X
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
              .format(name, location, self.flying_speed))
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location): # 메소드 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 벌쳐 : 지상유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중유닛
battleCruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battleCruiser.move("9시")

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 아무것도 안하고 일단 넘어감

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛 생성
supply_depot = BuildingUnit("서플라잇 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다")

def game_over():
    pass
game_start()
game_over()
print("Player : gg") # good game    