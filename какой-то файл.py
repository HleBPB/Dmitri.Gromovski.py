#1
A=1
B=10
for A in range(A,B+1):
    print(A)
#2
print('='*15)
a=int(input('Введи число:'))
b=int(input('Введи число:'))   
if a < b:
    for a in range(a,b+1):
        print(a)
else:
    for a in range(a,b, -1):
        print(a)
#3
print('='*15)
a=int(input('ВВедите число:'))
b=int(input('Введите число:'))
for i in range(a-int((a%2)==0),b-1,-2):
    print(i)
    
    
#4
import random
sum=0
for b in range(10):
    a=random.randint(0,99)
    sum+=a
print(sum)
#5
import random
sum=0
N=int(input('введи кол-во чисел:'))
for i in range(N):
    a=random.randint(0,99)
    sum+=a
print(sum)
#6
a=int(input('Введи n:'))
i=1
sum=-1
for i in range(a+1):
    b=i**3
    i+=1
    sum+=b
    print(b)
print(sum)
#7
n=int(input('Введи кол-во чисел:'))
b=1
sum=1
for u in range(n):
    z=b*(b+1)
    print('b= '+str(b))
    b+=2
    sum*=z
    print('z= '+str(z))
print(sum)
#8
n=int(input('Введи кол-во чисел:'))
b=1
sum=1
for u in range(n):
    z=b*(b+1)
    print('b= '+str(b))
    b+=2
    sum+=z
    print('z= '+str(z))
print(sum)
    
