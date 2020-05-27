class Animal:
    
    sound = "Animal Sound"
    br = ""
    growth_factor = 0
    
    def __init__(self,age_in_months=0,breed="None",required_food_in_kgs=0):
        
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        
        
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
        self._required_food_in_kgs += self.growth_factor
        self._age_in_months += 1
        
class LandAnimals:
    br = "Breathe in air"
    
    @classmethod
    def breathe(cls):
        print(cls.br)
        
class WaterAnimals:
    br = "Breathe oxygen from water"
    @classmethod
    def breathe(cls):
        print(cls.br)
        
class HuntingAnimals:
    else_msg = "No deers to hunt"
    name = "Deer"
    def hunt(self,ani):
        c = 0
        for i in ani.animals_list:
            if self.name in i:
                (ani.animals_list).remove(i)
                c += 1
        if c==0:
            print(self.else_msg)
                    
        
        
        
class Deer(Animal,LandAnimals):
    
    sound = "Buck Buck"
    growth_factor = 2
    
class Lion(Animal,LandAnimals,HuntingAnimals):
    sound = "Roar Roar"
    growth_factor = 4
    name = "Deer"
    
class Shark(Animal,WaterAnimals,HuntingAnimals):
    sound = "Shark Sound"
    growth_factor = 8
    name = "GoldFish"
    
class GoldFish(Animal,WaterAnimals):
    sound = "Hum Hum"
    growth_factor = 0.2
    
class Snake(Animal,LandAnimals,HuntingAnimals):
    sound = "Hiss Hiss"
    growth_factor = 0.5
    name="Deer"
    
class Zoo:
    total_animals = []
    
    def __init__(self,reserved_food_in_kgs=0):
        self._reserved_food_in_kgs = reserved_food_in_kgs
        self.animals_list = []
    
        
    def add_food_to_reserve(self,food):
        self._reserved_food_in_kgs  += food
        
    def count_animals(self):
        return len(self.animals_list)
        
    def add_animal(self,animal):
        self.animals_list.append(type(animal).__name__)
        self.total_animals.append(animal)
        
    def feed(self,animal):
        if self._reserved_food_in_kgs > 0:
            self._reserved_food_in_kgs -= animal._reserved_food_in_kgs
            animal.grow()
        
    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(cls.total_animals)
        
    @staticmethod
    def count_animals_in_given_zoos(animals):
        count=0
        for i in animals:
            count += i.count_animals
         
        return count   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
"""class Deer:
    sound="Buck Buck"
    air="Breathe in air"
    def __init__(self,age_in_months=0,breed="None",required_food_in_kgs=0):
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
             
        if self._age_in_months >= 10:
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

    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 2
            
         
    @classmethod   
    def make_sound(cls):
        print(cls.sound)
         
    @classmethod   
    def breathe(cls):
        print(cls.air)
        
    def hunt(self):
        pass
    
            
            
class Lion:
    sound="Roar Roar"
    air="Breathe in air"
    def __init__(self,age_in_months=0,breed="None",required_food_in_kgs=0):
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
             
        if self._age_in_months >= 10:
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

    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 4
            
         
    @classmethod   
    def make_sound(cls):
        print(cls.sound)
         
    @classmethod   
    def breathe(cls):
        print(cls.air)
            
    def hunt(self,obj):
        if "Deer" in obj.no_of_animals_in_all_zoos:
            Zoo.no_of_animals_in_all_zoos.remove("Deer")
        else:
            print("No deers to hunt")
            
            
            
            
class Shark:
    sound="Shark Sound"
    air="Breathe oxygen from water"
    def __init__(self,age_in_months=0,breed="None",required_food_in_kgs=0):
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
             
        if self._age_in_months >= 10:
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



    def grow(self):
            #if self._age_in_months==1:
        self._age_in_months += 1
        self._required_food_in_kgs += 8
            
         
    @classmethod   
    def make_sound(cls):
        print(cls.sound)
         
    @classmethod   
    def breathe(cls):
        print(cls.air)
        
        
    def hunt(self,obj):
        if "GoldFish" in obj.no_of_animals_in_all_zoos:
            Zoo.no_of_animals_in_all_zoos.remove("GoldFish")
        else:
            print("No GoldFish to hunt")

            
class GoldFish:
    sound="Hum Hum"
    air="Breathe oxygen from water"
    def __init__(self,age_in_months=0,breed="None",required_food_in_kgs=0):
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs

             
        if self._age_in_months >= 10:
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


    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 0.2
        
    def hunt(self,obj):
        pass
            
         
    @classmethod   
    def make_sound(cls):
        print(cls.sound)
         
    @classmethod   
    def breathe(cls):
        print(cls.air)
        
    
            

class Snake:
    sound="Hiss Hiss"
    air="Breathe in air"
    def __init__(self,age_in_months=0,breed="None",required_food_in_kgs=0):
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
             
        if self._age_in_months >= 10:
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

    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 0.5
        
    def hunt(self,obj):
        if "Deer" in obj.no_of_animals_in_all_zoos:
            Zoo.no_of_animals_in_all_zoos.remove("Deer")
        else:
            print("No deers to hunt")
            
         
    @classmethod   
    def make_sound(cls):
        print(cls.sound)
         
    @classmethod   
    def breathe(cls):
        print(cls.air)
            
            

            
class Zoo:
    count=0
    no_of_animals_in_all_zoos=[]
    
    def __init__(self):
        self._reserved_food_in_kgs=0
        self.animals_list = []
        #Zoo.count += 1
        
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    def add_food_to_reserve(self,food):
        self._reserved_food_in_kgs += food
        
    def count_animals(self):
        return(len(self.animals_list))
        
    def add_animal(self,animal):
        self.animals_list.append(animal)
        Zoo.no_of_animals_in_all_zoos.append(animal)
        
    def feed(self,ani):
        if self._reserved_food_in_kgs > 0:
             self._reserved_food_in_kgs -= ani._required_food_in_kgs
             ani._age_in_months += 1
        
        
    @classmethod
    def count_animals_in_all_zoos(cls):
        return(len(Zoo.no_of_animals_in_all_zoos))
    
    def count_animals_in_given_zoos(self):
        return(len(self.animals_list))"""
        
        
    
        
        
    
        
        
    
            






"""
class Lion(Deer):
    horn="Roar Roar"
    breathe_air="Breathe in air"
    
    def __init__(self,age_in_months=0,breed="None",required_food_in_kgs=0):
        super().__init__(age_in_months,breed,required_food_in_kgs)
        
    def grow(self):
        #if self._age_in_months ==1:
        super().grow()
        self._required_food_in_kgs += 2
    
    
    def feed(self,animal):
        if self._reserved_food_in_kgs > 0:
            self._reserved_food_in_kgs -= self._required_food_in_kgs

            
            
class Shark(Deer):
    horn = "Shark Sound"
    breathe_air="Breathe oxygen from water"
    
    
    def __init__(self,age_in_months=0,breed="None",required_food_in_kgs=0):
        super().__init__(age_in_months,breed,required_food_in_kgs)

     
     
    def grow(self):
        #if self.age_in_months ==1:
        super().grow()
        self._required_food_in_kgs += 6
        
    def feed(self,animal):
        if self._reserved_food_in_kgs > 0:
            self._reserved_food_in_kgs -= self._required_food_in_kgs
        
       
     
class GoldFish(Deer):
    horn = "Hum Hum"
    breathe_air="Breathe oxygen from water"
    
    
    def __init__(self,age_in_months=0,breed="None",required_food_in_kgs=0):
        super().__init__(age_in_months,breed,required_food_in_kgs)

    
    
    def grow(self):
        #if self._age_in_months ==1:
        self._age_in_months += 1
        self._required_food_in_kgs += 0.2
        
    def feed(self,animal):
            self._reserved_food_in_kgs -= self._required_food_in_kgs

        
class Snake(Deer):
    horn = "Hiss Hiss"
    breathe_air="Breathe in air"
    
    
    def __init__(self,age_in_months=0,breed="None",required_food_in_kgs=0):
        super().__init__(age_in_months,breed,required_food_in_kgs)

    
    
    def grow(self):
        #if self._age_in_months ==1:
        self._age_in_months += 1
        self._required_food_in_kgs += 0.5
        
    def feed(self,animal):
        if self._reserved_food_in_kgs > 0:
            self._reserved_food_in_kgs -= self._required_food_in_kgs"""
            
            

        
        
        
        
        
        
        
        
        
        
    
