# 9-1) 클래스
'''
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name   # 멤버변수
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp, self.damage))
'''
'''
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank1 = Unit("탱크", 150, 35)
tank2 = Unit("탱크", 150, 35)
'''


# 9-2) __init__ : 객체 생성시 자동호출
# 객체 : 클래스로부터 생성되는 것들

# marin = Unit("마린", 60) -> 오류



# 9-3) 멤버변수 : 클래스 내에서 정의된 변수
'''
# 레이스 : 공중 유닛, 비행기. 클로킹 기능(투명)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {}, 공격력 : {}".format(wraith1.name, wraith1.damage))
# "."를 통해 멤버변수에 접근(사용) 가능

# 상대 다크 아칸 -> 마인드 컨트롤 사용 : 상대 유닛 내 것으로 변환
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True  # 외부에서 추가로 멤버변수 생성 및 사용 가능

if wraith2.clocking == True:
    print("{} 는 현재 클로킹 상태입니다.".format(wraith2.name))
'''


# 9-4) 메소드

# ex) 공격 유닛
'''
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name   # 멤버변수
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp, self.damage))
    
    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다. 공격력은 {} 입니다."\
            .format(self.name, location, self.damage))
        # self.-- : 클래스 내부의 변수를 사용
        # self x : 전달받은 변수 사용

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))
'''
'''
# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)
'''


# 9-5) 상속
from turtle import speed


class Unit:   # 부모클래스
    def __init__(self, name, hp, speed):
        self.name = name   # 멤버변수
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도 {}]"\
            .format(self.name, location, self.speed))

# class 새 클래스(상속받을 클래스)
class AttackUnit(Unit):    # 자식클래스
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다. 공격력은 {} 입니다."\
            .format(self.name, location, self.damage))
        # self.-- : 클래스 내부의 변수를 사용
        # self x : 전달받은 변수 사용

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))
'''
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)
'''


# 9-6) 다중 상속 : 부모클래스가 여러개

# 드랍쉽 : 공중 유닛, 수송기. 유닛들을 수송. 공격 기능 x
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class Flyable_AttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드 = 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
'''
# 발키리 : 공중 공격 유닛, 미사일 14발 연속(동시) 발사.
valkyrie = Flyable_AttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
'''


# 9-7) 연산자 오버라이딩
'''
# 벌쳐 : 지상 유닛, 기동성 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력 많음, 공격력 높음
battlecruiser = Flyable_AttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")
'''


# 9-8) pass : 아무 행동을 하지 않고 넘어감
'''
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()
'''


# 9-9) super
'''
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, location)
        super().__init__(name, hp, 0)  # self 적으면 안됨
        # super : 다중상속시에는 처음 상속받은 클래스만 호출됨
        self.location = location
'''