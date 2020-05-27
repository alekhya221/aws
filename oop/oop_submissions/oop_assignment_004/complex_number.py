import math
class ComplexNumber:
    
    def __init__(self,real=0,imaginary=0):
        self.real_part=real
        self.imaginary_part=imaginary
        
        if self.real_part==str(self.real_part) and self.imaginary_part==str(self.imaginary_part):
            raise ValueError("Invalid value for real and imaginary part")
        
        elif self.real_part==str(self.real_part):
            raise ValueError("Invalid value for real part")
        elif self.imaginary_part==str(self.imaginary_part):
            raise ValueError("Invalid value for imaginary part")
        
    def __str__(self):
        return "{}{}{}i".format(self.real_part,'+' if self.imaginary_part >=0 else '-', abs(self.imaginary_part))
        
        
    def conjugate(self):
        return ComplexNumber(self.real_part,-self.imaginary_part)
        
    def __add__(self,other):
        return ComplexNumber(self.real_part+other.real_part,self.imaginary_part+other.imaginary_part)
    
    def __sub__(self,other):
        return ComplexNumber(self.real_part-other.real_part,self.imaginary_part-other.imaginary_part)
        
    def __mul__(self,other):
        real_part=self.real_part*other.real_part-self.imaginary_part*other.imaginary_part
        imaginary_part=self.imaginary_part*other.real_part+self.real_part*other.imaginary_part
        return ComplexNumber(real_part,imaginary_part)
    
    def __truediv__(self,other):
        sr,si,oor,ooi=self.real_part,self.imaginary_part,other.real_part,other.imaginary_part
        result=float(oor**2 + ooi**2)
        return ComplexNumber((sr*oor+si*ooi)/result,(si*oor-sr*ooi)/result)
        
        
    def __abs__(self):
        return round(math.sqrt(self.real_part**2 + self.imaginary_part**2),3)
        
        
    def __eq__(self,other):
        return self.real_part==other.real_part and self.imaginary_part==other.imaginary_part
        
        
             
        
        
        
        
        
        
        
        