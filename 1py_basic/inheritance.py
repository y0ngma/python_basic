class Animal():
    
    def __init__(self, name, weight): #초기화함수
        self.name = name
        self.weight = weight
    
    def __str__(self): #문자열화 함수
        return "{} (몸무게 {}kg)".format(self.name, self.weight)
    
    def eat(self):
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다.".format(self.name, self.weight))
    
    def walk(self):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다.".format(self.name, self.weight))

class Human(Animal):
    
    def golf(self):
        self.weight -= 0.5
        print("{}가 골프를 쳐서 {}kg이 되었습니다.".format(self.name, self.weight))

class Dog(Animal):

    def wag(self):
        self.weight -= 0.01
        print("{}가 꼬리를 흔들어서 {}kg이 되었습니다.".format(self.name, self.weight))


person = Human("용희", 75.0)
person.eat()
person.walk()
person.golf()
print(person)

puppy = Dog("마당쇠", 13)
puppy.eat()
puppy.walk()
puppy.wag()
print(puppy)


