import math
class Car:
    horn="Beep Beep"
    def __init__(self,color=None,max_speed=0,acceleration=0,tyre_friction=0):
        self._color=color
        self._max_speed=max_speed
        self._acceleration=acceleration
        self._tyre_friction=tyre_friction
        self._is_engine_started=False
        self._current_speed=0
        
        if self._max_speed<0:
            raise ValueError("Invalid value for max_speed")
            
        if self._acceleration<0:
            raise ValueError("Invalid value for acceleration")
            
        if self._tyre_friction<0:
            raise ValueError("Invalid value for tyre_friction")
        
                    
    @property
    def color(self):
        return self._color
    
    @property
    def is_engine_started(self):
        return self._is_engine_started

            
    @property
    def max_speed(self):
        return self._max_speed
        
    @property
    def acceleration(self):
        return self._acceleration
        
    @property
    def tyre_friction(self):
        return self._tyre_friction
        
    @property   
    def current_speed(self):
        return self._current_speed
        
    def start_engine(self):
        self._is_engine_started=True
        
    def accelerate(self):
        if self._is_engine_started:
            self._current_speed += self._acceleration
            if self._current_speed>=self._max_speed:
                self._current_speed=self._max_speed
        else:
            print("Start the engine to accelerate")
            
    def apply_brakes(self):
        if  self._is_engine_started:
            self._current_speed -= self._tyre_friction
            if self._current_speed<self._tyre_friction:
                self._current_speed=0
            
     
    def sound_horn(self):
        if self._is_engine_started:
            print(self.horn)
        else:
            print("Start the engine to sound_horn")
            
            
    def stop_engine(self):
        if self._is_engine_started:
            self._is_engine_started=False
            
            
            
            
            
            
            
"""def filter(self,query):
        self.query=query
        
        if query.operation=="EQ":
            for i in range(len(Store.list_items)):
                if Store.list_items[i].name==query.value:
                    Store.list1.append(Store.list_items[i])
        
        elif query.operation=="GT":
            for i in range(len(Store.list_items)):
                if Store.list_items[i].price>query.value:
                    Store.list1.append(Store.list_items[i])
        
        elif query.operation=="GTE":
            for i in range(len(Store.list_items)):
                if Store.list_items[i].price>=query.value
    
    
    
    
item1 = Item(name="Oreo Biscuits", price=30, category="Food") 
item2 = Item(name="Oreo Biscuits", price=0, category="Food")  

query = Query(field="name", operation="EQ", value="Oreo Biscuits")  

store = Store() 

store.add_item(item1)
item = Item(name="Boost Biscuits", price=20, category="Food")  
store.add_item(item2)  
print(store)"""   



"""if query.operation=="EQ":
            for i in range(len(Store.list_items)):
                if Store.list_items[i].name==query.value:
                    Store.list1.append(Store.list_items[i])"""
                    
                    
 """def filter(self,query):
        self.query=query
        for i in range(len(Store.list_items)):
            if Store.list1_items[i].value==query.value:
                return True
            else:
                return False"""
        

            