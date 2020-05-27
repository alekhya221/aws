class Car:
    def __init__(self,color,acceleration):
        self.color = color
        self.acceleration = acceleration
        self.speed = 0
    
    def accelerate(self):
        print("Speeding Up!")
        self.speed += self.acceleration
    
    def apply_brakes(self):
        print("Applying Breaks!!!")
        self.speed -= 10