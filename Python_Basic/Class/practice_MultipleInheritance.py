# 다중 상속
# 상속을 하나의 클래스만 받지 않고 여러개의 클래스를 받음

# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
# 공격 유닛
class AttackUnit(Unit): # 상속을 받으려면 클래스명 우측에 괄호에 상속 받는 클래스를 넣어줌 
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) 
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
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일을 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")