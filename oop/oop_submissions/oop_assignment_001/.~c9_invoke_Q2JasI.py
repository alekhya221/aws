class Car:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self.color=color
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction
        self.is_engine_started=False
        self.current_speed=0
        
    def start_engine(self):
        self.is_engine_started=True
        
    def accelerate(self):
        if is_engine_started:
            self.current_speed += self.acceleration

"""if __name__=="__main__":
    color=input()
    max_speed=float(input())
    acceleration=int(input())
    tyre_friction=int(input())
    car =Car(color=color,max_speed=max_speed,acceleration=acceleration,tyre_friction=tyre_friction)
    
    print(car.color)
    print(car.acceleration)
    print(car.max_speed)
    print(car.tyre_friction)

try:
    car.max_speed>0
    print(car.max_speed)
except ValueError as e:
    print("{}: Invlid_value for max_speed".format(e))"""
    