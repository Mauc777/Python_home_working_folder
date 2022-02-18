# По заданному номеру дня недели вывести его название.

import os
clear = lambda: os.system('cls')
clear()

day_of_the_week = [ ' ','Monday', 'Tuesday', 'Wednesday',
                   'Thursday', 'Fridey', 'Saturday', 'Sunday']

print('Введите порядковый номер Дня Недели ')
n = int(input("--> "))

if n <= 5 : 
    print(f'Будние - {day_of_the_week[n]}')
elif n !=5 or n > 5 or n <= 7:
    print(f'Выходные - {day_of_the_week[n]}')

    
# else n > 8 
    # print()                                  //проработать данный блок кода, НЕ РАБОТАЕТ!!
#     print('Введи число нормально!!')      

