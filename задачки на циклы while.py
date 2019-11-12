#111111
i=1
n=int(input('Введи число:'))
while i**2<n:
    print(i**2)
    i+=1
#22222
b=2
a=int(input('Введи число:'))
while a%b!=0:
    b+=1
print(b)
#3333333
n=int(input('Введи число'))
two_in_power = 2
power = 1
while two_in_power <= n:
    two_in_power *= 2
    power += 1
print(power - 1, two_in_power // 2)
#4444444
n=int(input('Км за первый день:'))
c=int(input("Км за какой-то день:"))
g=1
while n<=c:
    n*=1.1
    g+=1
print(g)
#5555555
x=int(input("Вклад:"))
p=int(input("(Только число)Проценты:"))
y=int(input("Итоговый вклад:"))
g=1
while x<=y:
    x=x*((p/100)+1)
    g+=1
print(g)
#66666666666
import random
b=1
h=0
while b!=0:
    b=random.randint(0,10)
    h+=1
    print("b= ", b)
print(h)
#777777777
import random
b=1
h=0
while b!=0:
    b=random.randint(0,19)
    h+=b
print(h)
#88888
import random
b=1
y=0
g=0
max=0
while b!=0:
    b=random.randint(0,99)
    y+=1
    g+=b
    if b>max:
        max=b
print(int(g/y),max)
#9
import random
max = 0
index_of_max = 0
element = -1
len = 0
while element != 0:
    element = random.randint(0,10)
    if element > max:
        max = element
        index_of_max = len
    len += 1
print("Индекс ",index_of_max,'максимальное чилсло',max)
#10
import random
b=1
y=0
g=0
max=0
while b!=0 and y<20:
    b=random.randint(0,99)
    y+=1
    g+=b
    if b>max:
        max=b
print(int(g/y),max)


    