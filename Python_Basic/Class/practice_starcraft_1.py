from random import *
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다. ".format(name))

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


# 마린 
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

        # 스팀팩 : 일정 시간 동안 공격 속도를 증가. 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)")
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))   


# 탱크
class Tank(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False; # 기존의 공격 유닛에 없던 멤버변수를 추가 
    
    # 시즈모드 : 탱크를 지상에 고정시켜 더 높은 파워로 공격 가능. 이동 불가
    seize_developed = False # 시즈모드 개발 여부
    def set_seize_mode(self):
        if Tank.seize_developed == True:
            return 
        # 현재 시즈 모드가 아닐 때
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈 모드일 때 
        else :
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False 
tank1 = Tank()
tank1.set_seize_mode()
tank1.set_seize_mode()
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

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드 (해제 상태)
    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else :
            print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
            self.clocked = True




# 벌쳐 : 지상유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중유닛
battleCruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battleCruiser.move("9시")

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0) # Unit.__init__(self, name, hp, 0)와 같음 # 건물은 스피드 0, super를 사용할때는 self를 사용하지 않음
        self.location = location

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛 생성
supply_depot = BuildingUnit("서플라잇 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다")

def game_over():
    print("Player : gg") # good game    
    print("[Player] 님이 게임에서 퇴장하였습니다. ") # good game    


# 실제 게임 시작
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

# 유닛 일괄 관리 
attack_units = []
attack_units.append(m1) # 리스트에 추가
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")


# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attck("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21)) # 공격은 랜덤으로 받음 (5~20)


# 게임 종료
game_over()
