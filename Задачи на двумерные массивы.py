#####1111
import random
n = int(input('Кол-во строк: '))
m = int(input('Кол-во элементов в строке: '))
a = [[random.randint(0,30) for j in range(m)] for i in range(n)]#Генерирую массивы рандомным генератором
for g in range(len(a)):#Создаю таблицу из полученых массивов
    for h in range(len(a[g])):
        print("{:4d}".format(a[g][h]),end = '')
    print()
max = a[0][0]
for i in range(len(a)):#поиск максимума 
    for j in range(len(a[i] )):
         if a[i][j] > max:
               max =  a[i][j]
index_max =[ (i,j) for i in range(len(a))  for j in range(len(a[i])) if a[i][j]  == max]#Поиск индекса максимума
line, column = index_max[0]
print('максимальный элемент = ',max)#вывод
print('строка =',line+1, 'столбец =',column+1)#вывод
#####2222
n = int(input())
a = [['.'] * n for i in range(n)]#Создание массива со всеми элементами .
for i in range(n):#Замена элементов на *
    a[i][i] = '*'
    a[n // 2][i] = '*'
    a[i][n // 2] = '*'
    a[i][n - i - 1] = '*'
for row in a:
    print(' '.join(row))#Соединение элементов 
######33333
n = int(input('Кол-во строк: '))
m = int(input('Кол-во столбцов: '))
a = [['.*'[(j + i) % 2] for j in range(m)] for i in range(n)]
for row in a:
    print(' '.join(row))
######44444
n = int(input('N: '))
a = [['0' for j in range(n)] for i in range(n)]#Генерируем Таблицу из нулей
b = 1#Счёт шагов от центральной диагонали + само число на которое меняем нули
while b<n:#цикл до достигания последней диагонали
    for i in range(n-b):#Цикл который меняет все числа над центровой диагональю
        a[i][i+b] = b
    for i in range(n-b):#Цикл который меняет все числа под центровой диагональю
        a[i+b][i] = b
    b+=1#Счётчик
for row in a:
    print(' '.join([str(elem) for elem in row]))#Оформление в таблицу
#####55555
n = int(input('N: '))
a = [['1' for j in range(n)] for i in range(n)]#Генерируем Таблицу из единиц
for i in range(n):
    a[i] = [0]*(n-1-i) + [1] + [2]*i
for row in a:
    print(' '.join([str(elem) for elem in row]))#Оформление в таблицу
######666666
def  swap_columns(a, i, j): # ТЗ
    for m in range(len(a)):
        for n in range(len(a[m])): #пробегаем по всем значениям меняем значения местами
            if a[m][n] == i:
                a[m][n]= j
            elif a[m][n] ==j:
                a[m][n]=i
    return a
a = []# создаём нужные переменные
n = int(input())
for i in range(n):
    a.append([int(j) for j in input().split()])#заполняем массив
print(a)
i =int(input())#выбираем какие значения поменять
j =int(input())
swap_columns(a,i,j)
#######7777777
n = int(input('N: '))
m = int(input('M: '))
a = [[i+(j*m) if j%2==0 else ((j+1)*m-1) - i for i in range(m)] for j in range(n)]
for row in a:
    print('  '.join([str(elem) for elem in row]))
    
    
    
    
    
    
    
