# 1
class Dog():
    age = 0
    name = ''
    weight = 0


dog = Dog()
dog.age = 4
dog.name = 'Lucy'
dog.weight = 1


# 2
class Person():
    name = ''
    cellPhone = ''
    email = ''


Vary = Person()
Mary = Person()
Vary.name = 'Gary'
Vary.cellPhone = '123'
Vary.email = 'a@c'
Mary.name = 'Tom'
Mary.cellPhone = '423'
Mary.email = 'c@c'


# 3
class Bird():
    color = ''
    name = ''
    breed = ''


myBird = Bird()
myBird.color = 'green'
myBird.name = 'Sunny'
myBird.breed = 'Sun Conure'


# 4
class Player():
    name = ''
    strength = 0
    coordinates = 0, 0


Herm = Player()
Herm.name = 'Herm'
Herm.strength = 50
Herm.coordinates = 100;
230


# 5
class Person:
    name = ''
    money = 0


nancy = Person()
# не был указан экземпляр атрибутов
nancy.name = 'Nancy'
nancy.money = 100


# 6-7
class Person:
    name = ''
    money = 0


bob = Person()
bob.name = 'Bob'
print(bob.name + ' has ' + str(bob.money) + ' dollars')


# Game1
# 1
class Cat():
    name = ''
    color = ''
    weight = 0

    def meow(self):
        print('Meow')


Barsic = Cat()
Barsic.name = 'Barsic'
Barsic.color = 'Black'
Barsic.weight = 12
Barsic.meow()


# 2
class Aadress():
    name = ''
    tel = ''

    def Print(self):
        print(self.tel, self.name)


ad = Aadress()
ad.name = 'dsd'
ad.tel = '434'
ad.Print()


# 3
class Monster():
    name = ''
    health = ''

    def deacreaseHealth(self, amount):
        self.health -= amount
        if self.health <= 0:
            print('Монстр {0} побеждён'.format(self.name))
        else:
            print(self.name + ' жива, у неё ' + str(self.health) + ' хп')


mon = Monster()
mon.name = 'ManGu'
mon.health = 20
mon.deacreaseHealth(10)
mon.deacreaseHealth(10)

# Game2
"""Модуль содержит класс Fighter"""
from random import randint

class Fighter():
    """Класс Fighter"""
    
    hp = 100
    name = ''

    def fight(self, p1, p2):
        """Метод рандомно отнимающий хп у игроков"""
        i = randint(0, 1)
        if i == 0:
            p1.hp -= 20
            print('Hp {0} '.format(p1.name) + str(p1.hp))
            if p1.hp <= 0:
                print('Игрок {}'.format(p1.name) + ' выйграл')



        if i == 1:
            p2.hp -= 20
            print('Hp {0} '.format(p2.name) + str(p2.hp))
            if p2.hp <= 0:
                print('Игрок {}'.format(p2.name) + ' выйграл')





Mari = Fighter()
Mari.name = 'Guru'
Vari = Fighter()
Vari.name = 'Gary'
F = Fighter()
F.fight(Mari, Vari)

while Mari.hp >= 0 and Vari.hp >= 0:
    if Mari.hp <= 0 or Vari.hp <= 0:
        break
    F.fight(Mari, Vari)

#Game3
"""Модуль содержит классы героев и солдатов"""
import random
class Unit:
    """Класс юнит предназначен для принимания номера юнита и номер команды"""
    def __init__(self, number, commandid):
        self.number = number
        self.commandId = commandid
class Hero(Unit):
    """Класс героев принимает Имя героя и его уровень"""
    def __init__(self,  number, commandid, name, level=1):
        Unit.__init__(self, number, commandid)
        self.name = name
        self.level = level
    def getlevel(self):
        """Метод для обновления уровня"""
        return self.level
    def inclevel(self):
        """Метод для подъема уровня и оповещения о нём"""
        self.level += 1
        print('Уровень героя', self.name,'увеличен на 1 и равен', self.level)
class Soldier(Unit):
    """Класс солдат.Выводит информацию о движениях солдата"""
    def gotohero(self, Hero):
        print('Солдат ', self.number, 'следует за героем', Hero.name, 'с номером', Hero.number)
H1 = Hero(1, 1, 'JIL')
H2 = Hero(2, 2, 'OOP')
armyH1, armyH2 = [], []

for i in range(3, 10):
    n = random.randint(0, 1)
    if n:
        armyH1.append(Soldier(i, 1))
        print('Солдат с номером', i, 'добавлен в армию', H1.name)
    else:
        armyH2.append(Soldier(i, 2))
        print('Солдат с номером', i, 'добавлен в армию', H2.name)
print('Армия героя', H1.name, ':', len(armyH1))
print('Армия героя', H2.name, ':', len(armyH2))
if len(armyH1) > len(armyH2):
    print('В армии', H1.name, 'больше солдат, увеличиваем его уровень')
    H1.inclevel()
else:
    print('В армии', H2.name, 'больше солдат, увеличиваем его уровень')
    H2.inclevel()
armyH1[1].gotohero(H2)
