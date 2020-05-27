#radius=4
#pi=3.14
#pi
#perimeter=2*pi*radius
#print(perimeter)

#area=pi*(radius**2)
#print(area)
#print(pi)
#print("Hello", end="-")
#print("World")
#print("Python",3.6,sep="-",end="-")
#a=input("Enter a number")
"""age=int(input())
if 12<age<18:
    growth_stage=str(15)
    print("Growth Stage: " + growth_stage)
else:
    if 18<age<21:
        print("Growth Stage:Young Adult")
    elif age>21:
        print("Growth Stage:Adult")
    else:
       print("Growth Stage:child")
print(str(age) + "years old")"""
"""n=int(input())
i=1
while i<=n:
    print(i,end=' ')
    i=i+1"""
"""fruits=['Apple','Banana','Grapes','Oranges']
i=0
while i < len(fruits):
    print(fruits[i],end=' ')
    i=i+1"""
#num=[1,-24,-11]
"""for i in num:
    print("Evaluating "+str(i))
    if i<0:
        print("There is a negative number.")
else:
    print("All numbers are non-negative.")"""
"""first_ten_even_numbers=[]
first_ten_even_numbers=[item*2 for item in range(0,10)]
print(first_ten_even_numbers)"""
"""pairs=[]
pairs=[caps+small for caps in ['A','B','C'] for small in ['a','b','c']]
print(pairs)
odd=[]
odd=[item for item in range(1,100) if item%2!=0]
print(odd)"""
"""multiples=[]
multiples=[[multiplier*multiplicand for multiplicand in range(1,5)] for multiplier in range(1,5)]
print(multiples)"""
"""strings=[convert_to_string(integer) for integer in range(5,10+1)]
print(strings)"""
def my_sum(*args):
    result=0
    for x in args:
        result+=x
    return result
print(my_sum(1,2))
print(my_sum(1,2,10))

    
    
