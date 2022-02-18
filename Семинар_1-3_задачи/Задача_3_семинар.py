# Дано число обозначающее день недели. Выяснить является номер дня недели выходным

import os
def clear(): return os.system('cls')
clear()


a = 365  
day_of_the_week = [ ' ','Monday', 'Tuesday', 'Wednesday',
                   'Thursday', 'Fridey', 'Saturday', 'Sunday']

print('Введите порядковый номер Дня в году --> ')
n = int(input("--> "))   

# if a % 1 ==0 and a % 2 ==0 and a % 3 ==0  and a % 4 ==0 and a % 5 ==0: 
#     print(f'Будние') # - {day_of_the_week[n]}')
if n % 7 ==6: 
    print(f'Выходные')
elif a % 7 ==0:
    print(f'Выходные')# - {day_of_the_week[n]}')

else:
    print('отвали и ВАЛИ на работу')
