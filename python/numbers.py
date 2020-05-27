"""def first_n_even_numbers(n):
     for num in range(2,n*2+1):
         if num%2==0:
            print(num,end=' ')
            
def first_n_odd_numbers(n):
     for num in range(2,n*2+1):
         if num%2!=0:
            print(num,end=' ')"""


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
f=fib2(200)
print(f)






















