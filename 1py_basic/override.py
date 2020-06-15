class Animal():
    
    def __init__(self, name, weight): #초기화함수
        self.name = name
        self.weight = weight
    
    def __str__(self): #문자열화 함수
        return "{} (몸무게 {}kg)".format(self.name, self.weight)
        
    def greet(self):
        print("{}가 당신에게 인사한다".format(self))
        
        
        
class Human(Animal):
    
    def wave(self):
        print("무게 {}인 사람이 손을 흔든다".format(self.weight))
    def greet(self):
        self.wave()
        
        
class Dog(Animal):

    def wag(self):
        print("{}가 꼬리를 흔든다".format(self.name))
    def greet(self):
        self.wag()
        
        
class Cow(Animal):
    '''소'''



person = Human("용희", 75.0)
person.greet()

puppy = Dog("마당쇠", 13)
puppy.greet()
    
bull = Cow("젖소", 255)
bull.greet() 
