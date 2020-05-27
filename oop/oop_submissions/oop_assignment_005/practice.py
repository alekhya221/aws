class Fruit:
    
    def __init__(self):
        self.list1=[]
        
    def is_fruit(self,* l1 ):
        for item in l1:
            if item=="mango":
                self.list1.append(item)
    def print(self):
        if len(self.list1)>0:
            print(self.list1)
        
l1=["apple","mango","banana","orange"]  
f1=Fruit()
f1.is_fruit(l1)
#f1=Fruit("mango",20,"green")
#f2=Fruit("banana",15,"yellow")