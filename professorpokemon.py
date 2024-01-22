#v1
class FlyingMixin
    def fly(self):
        return f"{slef.name}이(가) 훨훨 납니다."
class SwmminMixin
    def fly(self):
        return f"{slef.name}이(가) 수영을 합니다."
class Pokemon:
    def __init__(self, name):
        self.name = name
    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")

#class Pikachu(Pokemon):
class Pikachu(Pokemon): #is - a
    def __init__(self, name, type):
        super().__init__(name) #super() -> 부모클래스 호출, 부모클래스의 init method를 이용해서 초기화
        self.type = type
    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) {self.type} 공격!")
    def electric_info(self):
        print("전기 계열의 공격을 합니다.")

class Squirtle(Pokemon): #is - a
    pass
class Agumon:
    pass

p1 = Pikachu("피카츄", "전기")
p2 = Squirtle("꼬부기")
p3 = Pokemon("근육몬")
p1.electric_info()
#p3.electric_info() #AttributeError: 'Pokemon' object has no attribute 'electric_info'
p1.attack(p2)
p2.attack(p1)
print(p1.name, p1.type)
print(issubclass(Pikachu,Pokemon))
#오버라이드: 부모가 가진 메서드를 자식이 재정의함


#v2
class FlyingMixin:
    def fly(self):
        return f"{slef.name}이(가) 훨훨 납니다."
class SwmminMixin:
    def fly(self):
        return f"{slef.name}이(가) 수영을 합니다."

class Pokemon:
    def attack(self):
        print("공격")

    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name

class Pokemon:


#v3

class FlyingMixin:
    def fly(self):
        return f"{self.__name}이(가) 하늘을 훨훨 날아갑니다~"


class SwimmingMixin:
    def swim(self):
        return f"{self.__name}이(가) 수영을 합니다."


class Pokemon:
    def __init__(self, name):
        self.__name = name

    def attack(self):
        print("공격~")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    # name = property(get_name, set_name)
    def __str__(self):
        return self.__name + " 입니다"

    def __add__(self, target):
        return self.__name + "+" + target.__name  # 연산자 오버로딩


class Charizard(Pokemon, FlyingMixin):
    pass


class Gyarados(Pokemon, SwimmingMixin):
    pass


g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")
print(g1)
print(c1)
print(g1 + c1)

#v4
class FlyingMixin:
    def fly(self):
        return f"{self.__name}이(가) 하늘을 훨훨 날아갑니다~"

class SwimmingMixin:
    def swim(self):
        return f"{self.__name}이(가) 수영을 합니다."

class Pokemon:
    def __init__(self, name, hp):
        self.__name = name
        self.hp = hp

    def attack(self):
        print("공격~")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    #name = property(get_name, set_name)
    def __str__(self):
        return self.__name + " 입니다"

    def __add__(self,target):
        #return self.__name+"+"+target.__name #연산자 오버로딩
        return f"두 포켓몬스터 체력의 합은 {self.hp+target.hp} 입니다."


class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados("갸라도스", 100)
c1 = Charizard("리자몽", 120)
print(g1)
print(c1)
print(g1+c1)

#v5
class FlyingBehavior:
    def fly(self): #메서드 형태 #fly라는 instance
        return f"하늘을 훨훨 날아갑니다~"

class JetPack(FlyingBehavior):
    def fly(self):
        return f"로켓 추진기로 하늘을 날아갑니다."

class NoFly(FlyingBehavior):
    def fly(self):
        return f"하늘을 날 수 없습니다."

class FlyWithWings(FlyingBehavior):
    def fly(self):
        return f"날개로 하늘을 훨훨 날아갑니다."

class SwimmingBehavior:
    def swim(self):
        return f"{self.__name}이(가) 수영을 합니다."

class Pokemon:
    def __init__(self, name, hp, fly_behavior):
        self.__name = name
        self.hp = hp
        self.fly_behavior = fly_behavior #클래스의 객체

    def set_fly_behavior(self, fly):
        self.fly_behavior = fly


    def attack(self):
        print("공격~")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    #name = property(get_name, set_name)
    def __str__(self):
        return self.__name + " 입니다"

    def __add__(self,target):
        #return self.__name+"+"+target.__name #연산자 오버로딩
        return f"두 포켓몬스터 체력의 합은 {self.hp+target.hp} 입니다."


class Charizard(Pokemon):
    pass

class Pikachu(Pokemon):
    def __init__(self, name, hp, fly):
        self.name = name
        self.hp = hp
        #self.fly_behavior = fly #aggregation
        self.fly_behavior = NoFly() #composition

#nofly=NoFly()
p1 = Pikachu("피카츄", 35, NoFly) #lsp
print(p1.fly_behavior.fly())
'''
wings = FlyWithWings()
c1 = Charizard("리자몽", 120, wings) #다른 클래스의 객체를 인수로 전달 #lsp
print(c1.fly_behavior.fly()) #리자몽객체 -> flyingbehavior클래스의 객체 -> " 가 가지고 있는 속성
print(p1.fly_behavior.fly())
print(p1) #cannot fly
print(c1)
p1.set_fly_behavior(JetPack())
print(p1+c1)
'''

#v6
