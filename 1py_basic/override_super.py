class Animal():
    
    def __init__(self, name, weight): #초기화함수
        self.name = name
        self.weight = weight
    
    def __str__(self): #문자열화 함수. 없으면 print(person)불가
        return "{} (몸무게 {}kg {}잡이)".format(self.name, self.weight, self.hand)
        
    def greet(self):
        print("{}가 당신에게 인사한다".format(self.name))
        
    
class Human(Animal):
    
    def __init__(self, name, weight, hand):
        super().__init__(name, weight)
        self.hand = hand
    
    def wave(self):
        print("{}을 흔들면서".format(self.hand))
    
    def greet(self):
        self.wave()
        super().greet()


person = Human("용희", 75.0, "오른손")
person.greet()
print(person)
