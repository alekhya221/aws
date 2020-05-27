class Animal:
    
    sound = "Animal Sound"
    bre = ""
    growth_factor = 0
    
    def __init__(self,age_in_months=0,breed="None",required_food_in_kgs=0):
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
             
        if self._age_in_months != 1:
            raise ValueError("Invalid value for field age_in_months: {}".format(self._age_in_months))
             
        if self._required_food_in_kgs <= 0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(self._required_food_in_kgs))
        
    @property
    def age_in_months(self):
        return self._age_in_months
        
    @property
    def breed(self):
        return self._breed
            
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
    @classmethod   
    def make_sound(cls):
        print(cls.sound)


    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += self.growth_factor
            
         
class LandAnimals:
    
    @classmethod
    def breathe(cls):
        print("Breathe in air")
        
class WaterAnimals:
    
    @classmethod
    def breathe(cls):
        print("Breathe oxygen from water")
        
class HuntingAnimals:
    
    else_msg = "No deers to hunt"
    name = "Deer"
     
    def hunt(self,animals_list):
        c=0
        for i in animals_list.animals_in_given_zoo:
            if self.name in i:
                (animals_list.animals_in_given_zoo).remove(i)
                c += 1
        if c==0:
            print(self.else_msg)
                
class Deer(Animal,LandAnimals):
    sound ="Buck Buck"
    growth_factor = 2
    

class Lion(Animal,LandAnimals,HuntingAnimals):
    sound = "Roar Roar"
    growth_factor = 4
    name = "Deer"
        
class Shark(Animal,WaterAnimals,HuntingAnimals):
    sound = "Shark Sound"
    growth_factor = 8
    name = "GoldFish"
    else_msg = "No GoldFish to hunt"    
    
    
class GoldFish(Animal,WaterAnimals):
   sound = "Hum Hum"
   growth_factor = 0.2
   
   
class Snake(Animal,LandAnimals,HuntingAnimals):
   sound = "Hiss Hiss"
   growth_factor = 0.5
   name = "Deer"

    
class Zoo:
    total_animals=[]
    
    def __init__(self,reserved_food_in_kgs=0):
        self._reserved_food_in_kgs = reserved_food_in_kgs
        self.animals_in_given_zoo = []

        
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    def add_food_to_reserve(self,food):
        self._reserved_food_in_kgs += food
        
    def count_animals(self):
        return len(self.animals_in_given_zoo)
        
    def add_animal(self,animal):
        (self.animals_in_given_zoo).append(type(animal).__name__)
        (self.total_animals).append(animal)
        
    def feed(self,animal):
        if self._reserved_food_in_kgs > 0:
             self._reserved_food_in_kgs -= animal._required_food_in_kgs
             animal.grow()
        
        
    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(cls.total_animals)
        
    @staticmethod
    def count_animals_in_given_zoos(animals):
        count=0
        for i in animals:
            count += i.count_animals()
            
        return count
   



    

    
    
    