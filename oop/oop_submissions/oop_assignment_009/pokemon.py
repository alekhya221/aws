class Pokemon:
    sound = ""
    value = 0
    
    def __init__(self,name,level=1):
        self._name = name
        self._level = level
        if self._name == "":
            raise ValueError("name cannot be empty")
        if self._level <= 0:
            raise ValueError("level should be > 0")
            
    @property
    def name(self):
        return self._name
        
    @property
    def level(self):
        return self._level
        
    def __str__(self):
        return "{} - Level {}".format(self._name,self._level)
    
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
class ElectricPokemon:
    pokemon_run=""
    value = 10
    level=1
    
    def attack(self):
        print("Electric attack with {} damage".format(self.value * self.level))
        
    @classmethod
    def run(cls):
        print(cls.pokemon_run)
        
class WaterPokemon:
    pokemon_run = ""
    pokemon_swim = ""
    value = 9
    level = 1
    def attack(self):
        print("Water attack with {} damage".format(self.value * self.level))
        
    @classmethod
    def run(cls):
        print(cls.pokemon_run)
        
    @classmethod
    def swim(cls):
        print(cls.pokemon_swim)

class FlyingPokemon:
    pokemon_fly = ""
    value = 5
    level = 1
    def attack(self):
        print("Air attack with {} damage".format(self.value * self.level))
        
    @classmethod
    def fly(cls):
        print(cls.pokemon_fly)
        
class Pikachu(Pokemon,ElectricPokemon):
    sound = "Pika Pika"
    pokemon_run = "Pikachu running..."
    value = 10
    
class Squirtle(Pokemon,WaterPokemon):
    sound = "Squirtle...Squirtle"
    pokemon_run = "Squirtle running..."
    pokemon_swim = "Squirtle swimming..."
    value = 9
    
class Pidgey(Pokemon,FlyingPokemon):
    sound = "Pidgey...Pidgey"
    pokemon_fly = "Pidgey flying..."
    value = 5
    
class Swanna(Pokemon,WaterPokemon,FlyingPokemon):
    sound = "Swanna...Swanna"
    pokemon_fly = "Swanna flying..."
    pokemon_swim = "Swanna swimming..."
    value = 9
    
    def attack(self):
        WaterPokemon.attack(self)
        self.value = 5
        FlyingPokemon.attack(self)

class Zapdos(Pokemon,ElectricPokemon,FlyingPokemon):
    sound = "Zap...Zap"
    pokemon_run = "Zapdos running..."
    pokemon_fly = "Zapdos swimming..."
    value = 10
    def attack(self):
        ElectricPokemon.attack(self)
        self.value = 5
        FlyingPokemon.attack(self)
        
class Island:
    island_list = []
    
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        Island.island_list.append(self)
        
    @property
    def name(self):
        return self._name
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    @property 
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
        
    def __str__(self):
        return "{} {} pokemon - {} food".format(self._name,self._pokemon_left_to_catch,self._total_food_available_in_kgs)

    
    def add_pokemon(self,pokemon):
        if self._pokemon_left_to_catch > self._max_no_of_pokemon:
            print("Island at its max pokemon capacity")
        else:
            self._pokemon_left_to_catch += 1
    @classmethod       
    def get_all_islands(cls):
        return cls.island_list
    
        
        
class Trainer:
    
    def __init__(self,name,experience,max_food_in_bag):
        self._name = name
        self._experience = experience
        self._max_food_in_bag = 10 * experience
        self._food_in_bag = 0
        self._current_island = ""
        self.pokemon_count = []
        
    @property
    def name(self):
        return self._name
        
    @property
    def experience(self):
        return self._experience
        
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
        
    @property
    def current_island(self):
        if self._current_island == "":
            print("You are not on any island")
        else:
            return self._current_island
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
"""class Pokemon:
    sound = ""
    running = ""
    att_val = 0
    class_type = ""
    
    
    def __init__(self,name,level=1):
        self._name = name
        self._level = level
        
        if self._name == "":
            raise ValueError("name cannot be empty")
        if self._level <=0 :
            raise ValueError("level should be > 0")
            
        
    @property
    def name(self):
        return self._name
        
    @property
    def level(self):
        return self._level
        
        
    def __str__(self):
        return "{} - Level {}".format(self._name,self._level)
        
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
    def attack(self):
         print("{} attack with {} damage".format(self.class_type,self.att_val*self._level))  
    
    
class Electric(Pokemon):
    running = ""
    
    @classmethod
    def run(cls):
        print("{} running...".format(cls.running))
    
    
        
        
class Water():
    swimming  = ""
   
    @classmethod 
    def swim(cls):
        print("{} swimming...".format(cls.swimming))
        
class Fly:
    fl = ""
    
    @classmethod
    def fly(cls):
        print("{} flying...".format(cls.fl))
    
    
        
        
class Pikachu(Electric,Pokemon):
    sound = "Pika Pika"
    running = "Pikachu"
    att_val = 10
    class_type = "Electric"
    
class Squirtle(Electric,Pokemon,Water):
    sound = "Squirtle...Squirtle"
    running="Squirtle"
    swimming="Squirtle"
    att_val = 9
    class_type = "Water"
    
class Pidgey(Fly,Pokemon):
    sound = "Pidgey...Pidgey"
    fl="Pidgey"
    att_val = 5
    class_type = "Air"
    
class Swanna(Fly,Pokemon,Water):
    sound = "Swanna...Swanna"
    swimming = "Swanna"
    fl="Swanna"
    class_type = "Water"
    att_val= 9
    
    def attack(self):
        if Swanna.class_type == "Air" and Swanna.att_val == 5:
            Swanna.class_type = "Water"
            Swanna.att_val = 9
            super().attack()
        else:
            Swanna.class_type = "Water"
            Swanna.att_val = 9
            super().attack()
            
        if Swanna.class_type == "Water" and Swanna.att_val == 9:
            Swanna.class_type = "Air"
            Swanna.att_val = 5
            super().attack()
        else:
            Swanna.class_type = "Air"
            Swanna.att_val = 5
            super().attack()

class Zapdos(Electric,Fly,Pokemon):
    sound = "Zap...Zap"
    fl="Zapdos"
    class_type = "Electric"
    att_val= 10
    
    def attack(self):
        if Zapdos.class_type == "Air" and Zapdos.att_val == 5:
            Zapdos.class_type = "Electric"
            Zapdos.att_val = 10
            super().attack()
        else:
            Zapdos.class_type = "Electric"
            Zapdos.att_val = 10
            super().attack()
            
            
        if Zapdos.class_type == "Electric" and Zapdos.att_val == 10:
            Zapdos.class_type = "Air"
            Zapdos.att_val = 5
            super().attack()
        else:
            Zapdos.class_type = "Air"
            Zapdos.att_val = 5
            super().attack()
            
    
    
class Island:
     
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        self.list_of_pokemons=[]
        
    @property
    def name(self):
        return self._name

    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
        
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
        
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
        
    def __str__(self):
        return "{} - {} pokemon - {} food".format(self._name,self._pokemon_left_to_catch,self._total_food_available_in_kgs)
    

    def add_pokemon(self,pokemon):
        self.list_of_pokemons.append(pokemon)
        self._pokemon_left_to_catch  += 1
        if self._pokemon_left_to_catch > self._max_no_of_pokemon:
            print("Island at its max pokemon capacity")
            self._pokemon_left_to_catch = self._max_no_of_pokemon
        

class Trainer(Island):
    
    def __init__(self,name,experience=100):
        self._name = name
        self._experience = experience
        self._max_food_in_bag = 10*experience
        self._food_in_bag=0
        self._current_island=""
        
    @property
    def name(self):
        return self._name
    
    @property
    def experience(self):
        return self._experience
        
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
        
    @property
    def food_in_bag(self):
        return self._food_in_bag
    
    @property
    def current_island(self):
        return self._current_island
    
    def __str__(self):
        return "{}".format(self._name)
        
        
    #def max_food_in_bag(self):
        #print(list(10*self._experience))
        #return max_food
        
    def get_all_islands(self):
        for i in self.list_of_pokemons:
            print(i)
            
            
    def move_to_island(self,island):
        pass
    
    def collect_food(self):
        self._food_in_bag=self._total_food_available_in_kgs-self._experience
        self._total_food_available_in_kgs -= self._max_food_in_bag"""

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"""class Pokemon:
    sound = ""
    value = 0
    def __init__(self, name="", level = 1):
        if len(name) == 0:
            raise ValueError("name cannot be empty")
        self._name = name
        if level <= 0:
            raise ValueError("level should be > 0")
        self._level = level
        self._master = ""
        
    @property
    def name(self):
        return self._name
        
    @property
    def master(self):
        if self._master == "":
            print("No Master")
        else:
            return self._master
        
    @property
    def level(self):
        return self._level
        
    def __str__(self):
        return f'{self.name} - Level {self.level}'
        
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    
class ElectricPokeman:
    value = 10
    level = 1
    pokemon_run = ""
    def attack(self):
        print(f'Electric attack with {self.level * self.value} damage')
        
    @classmethod
    def run(cls):
        print(cls.pokemon_run)
        
class WaterPokeman:
    value = 9
    level = 1
    pokemon_run = ""
    pokemon_swim = ""
    def attack(self):
        print(f'Water attack with {self.level * self.value} damage')
        
    @classmethod
    def run(cls):
        print(cls.pokemon_run)
        
    @classmethod
    def swim(cls):
        print(cls.pokemon_swim)
        
class FlyingPokeman:
    value = 5
    level = 1
    pokemon_fly = ""
    def attack(self):
        print(f'Air attack with {self.level * self.value} damage')
    @classmethod
    def fly(cls):
        print(cls.pokemon_fly)
        
class Pikachu(Pokemon, ElectricPokeman):
    sound = "Pika Pika"
    pokemon_run = "Pikachu running..."
    value = 10
    
class Squirtle(Pokemon, WaterPokeman):
    sound = "Squirtle...Squirtle"
    pokemon_swim = "Squirtle swimming..."
    pokemon_run = "Squirtle running..."
    value = 9
    
class Pidgey(Pokemon, FlyingPokeman):
    sound = "Pidgey...Pidgey"
    pokemon_fly = "Pidgey flying..."
    value = 5

class Swanna(Pokemon, WaterPokeman, FlyingPokeman):
    sound = "Swanna...Swanna"
    pokemon_fly = "Swanna flying..."
    pokemon_swim = "Swanna swimming..."
    value = 9
    
    def attack(self):
        WaterPokeman.attack(self)
        self.value = 5 
        FlyingPokeman.attack(self)
        
class Zapdos(Pokemon, FlyingPokeman, ElectricPokeman):
    sound = "Zap...Zap"
    pokemon_fly = "Zapdos flying..."
    value = 10
    
    def attack(self):
        ElectricPokeman.attack(self)
        self.value = 5
        FlyingPokeman.attack(self)
        
class Island:
    islands_count = []
    def __init__(self, name, max_no_of_pokemon, total_food_available_in_kgs):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        self.islands_count.append(self)
    
    @property
    def name(self):
        return self._name
    
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
        
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
        
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
        
    def __str__(self):
        return f'{self.name} - {self._pokemon_left_to_catch} pokemon - {self._total_food_available_in_kgs} food'
        
    def add_pokemon(self, pokemon):
        if self._pokemon_left_to_catch != self.max_no_of_pokemon:
            self._pokemon_left_to_catch += 1
        else:
            print("Island at its max pokemon capacity")
            
    @classmethod
    def get_all_islands(cls):
        return cls.islands_count
            
class Trainer:
    def __init__(self, name):
        self._name = name
        self._experience = 100
        self._max_food_in_bag = 10 * self._experience
        self._food_in_bag = 0
        self._current_island = ""
        self.count_pokemon = []
        
    @property
    def name(self):
        return self._name
        
    @property
    def experience(self):
        return self._experience
        
    @property
    def current_island(self):
        if self._current_island == "":
            print("You are not on any island")
        else:
            return self._current_island
        
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
        
    @property
    def food_in_bag(self):
        return self._food_in_bag
       
    def catch(self, pokemon):
        if self.experience >= (100 * pokemon.level):
            self.count_pokemon.append(pokemon)
            pokemon._master = self
            self._experience = self.experience + (pokemon.level * 20)
            print(f'You caught {pokemon.name}')
        else:
            print(f'You need more experience to catch {pokemon.name}')
            
    def collect_food(self):
        if self._current_island == "" or self._current_island._total_food_available_in_kgs == 0:
            print("Move to an island to collect food")
        elif self._current_island._total_food_available_in_kgs < self._max_food_in_bag:
            self._food_in_bag = self._current_island._total_food_available_in_kgs
            self._current_island._total_food_available_in_kgs = 0
        elif self._food_in_bag != self._max_food_in_bag:
            self._current_island._total_food_available_in_kgs -= 1000
            self._food_in_bag = 1000
        
    def move_to_island(self, island):
            self._current_island = island
    
    def get_my_pokemon(self):
        return self.count_pokemon  """     
   
        
    
    
    

        