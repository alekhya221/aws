"""def print_helloworld():
    print('Hello World')
def one():
    print('1')
def print_helloworld1():
    print('Hello World')
    
import sys
print (sys.argv)
command=""
while command.lower()!= "quit":
    command=input(">")
    print("ECHO",command)
    
2 + 2
4
50 - 5*6
20
(50 - 5*6) / 4
5.0
8 / 5  
1.6"""
def fib(n):
    a,b=0,1
    while a<n:
        print(a)
        a,b=b,a+b
def fib2(n):
    result=[]
    a,b=0,1
    while(a<n):
        result.append(a)
        a,b=b,a+b
        return result