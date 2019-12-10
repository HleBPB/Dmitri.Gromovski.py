budzet = 0
nalog = 0
netto = 0
def net():
    global netto,budzet,nalog
    brutto = float(input('Введите доход: '))
    if brutto >540:
        if (brutto*12)>14400:
            nalog = (brutto - 540)*0.266
            netto = (brutto - 540 -((brutto - 540)*0.266)) + 540
            budzet += netto
            print('Сумма подоходного налога:',round(((brutto - 540)*0.23),2),'\nНакопительный пенсионный фонд:',round(((brutto - 540)*0.02),2),'\nНалог по безработице:',round(((brutto - 540)*0.016),2),'\nи бюджет равен с этого человека: ',netto)
        elif (brutto*12)<25200 and (brutto*12)>14400:
            nalog = (brutto - (500 - 0.55556*(brutto - 1200)))*0.236
            netto = (500 - 0.55556*(brutto - 1200) + (brutto - (500 - 0.55556*(brutto - 1200)))*0.236)
            budzet += netto
            print('Сумма подоходного налога:',round(brutto - (500 - 0.55556*(brutto - 1200)*0.20),2),'\nНакопительный пенсионный фонд:',round(brutto - (500 - 0.55556*(brutto - 1200)*0.02),2),'\nНалог по безработице:',round(brutto - (500 - 0.55556*(brutto - 1200)*0.016),2),'\nи бюджет равен с этого человека: ',netto)
        else:
            nalog = brutto*0.266
            netto = brutto - brutto*0.266
            budzet += netto
            print('Сумма подоходного налога:',round((brutto*0.20),2),'\nНакопительный пенсионный фонд:',round((brutto*0.02),2),'\nНалог по безработице:',round((brutto*0.016),2),'\nи бюджет равен с этого человека: ',netto)
    else:
        budzet += brutto
        print('При минималке или ниже налог не берётся и бюджет равен: ',brutto)
def deti():
    global child,budzet
    child = int(input('Введите кол-во детей в семье: '))
    if child <=2:
        budzet += 60*child
        print('Дотация за детей равна:',60*child)
    else:
        budzet += 100*child
        print('Дотация за детей равна:',100*child)
i = int(input('Сколько взрослых с зп в семье?: '))
for i in range(i):
    net()
    print('Бюджет с зарплат:',budzet)
deti()
print('Итоговый бюджет за месяц:',budzet,',а снято налогами:',round(nalog,2),'\nИтоговый бюджет за год:',budzet*12,'\nИтоговая сумма налогов за год:',nalog*12)
