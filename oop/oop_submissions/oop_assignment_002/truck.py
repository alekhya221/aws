from car import Car
class Truck(Car):
    horn = "Honk Honk"
    def __init__(self,color=None,max_speed=0,acceleration=0,tyre_friction=0,max_cargo_weight=0):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        
        self._max_cargo_weight=max_cargo_weight
        self._cargo_weight=0
        
        if self._max_cargo_weight<0:
            raise ValueError("Invalid value for max_cargo_weight")
        
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
        
    @property
    def cargo_weight(self):
        return self._cargo_weight


    def load(self,weight):
        if weight<0:
            raise ValueError("Invalid value for cargo_weight")
            
        else:
            if self._current_speed>0:
                print("Cannot load cargo during motion")
            else:
                if self._cargo_weight + weight > self._max_cargo_weight:
                    print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
                else:
                    self._cargo_weight += weight 
        
    def unload(self,weight):
        if weight<0:
            raise ValueError("Invalid value for cargo_weight")
            
        else:
            if self._current_speed>0:
                print("Cannot unload cargo during motion")
            else:
                if self._is_engine_started==False:
                    self._cargo_weight -= weight 
    








































        