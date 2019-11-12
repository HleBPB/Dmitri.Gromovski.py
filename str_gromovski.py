#1
a=input('Строка: ')
print('Сначала выведите третий символ этой строки',a[2])
print('Во второй строке выведите предпоследний символ этой строки',a[-2])
print('В третьей строке выведите первые пять символов этой строки',a[0:5])
print('В четвертой строке выведите всю строку, кроме последних двух символов',a[0:-2])
print('В пятой строке выведите все символы с четными индексами',a[0::2])
print('В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки',a[1::2])
print('В седьмой строке выведите все символы в обратном порядке',a[-1:0])
print('В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего',a[-1:0:2])
print('Длинна строки',len(a))
#2
b=input('Слова плз: ')
print(b.count(' ',0,len(b))+1)
#3
u=input('Строки наше всё:')
print(u[round(len(u)/2):-1]+u[0:round(len(u)/2)])
#4
u=input('Вводи не стесняйся: ')
print(u[u.find(' '):len(u)],u[0:u.find(' ')])
#5
s=input('Важная информация по букве F: ')
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))
#6
s=input('ff: ')
if s.count('f') == 1:
    print('-1')
elif s.count('f') == 0:
    print(-2)
elif s.count('f') >= 2:
    print(s.find('f',s.count('f')+1))
#7
s = input()
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)
#8
s=input('Жми хоть иногда(2 или больше раз)h:')    
a = s[:s.find('h')] 
b = s[s.find('h'):s.rfind('h') + 1]
c = s[s.rfind('h') + 1:]
s = a + b[::-1] + c
print(s)
#9
s = input()
print(s.replace('1','one'))
#10
s = input()
print(s.replace('@',' '))
#11
s = input()
a = s[:s.find('h')+1]
b = s[s.rfind('h'):]
c = s[s.find('h')+1:s.rfind('h')]
s = a + c.replace('h','H') + b
print(s)
#12
s = input()
t = ''
for i in range(len(s)):
    if i % 3 != 0:
        t = t + s[i]
print(t)


