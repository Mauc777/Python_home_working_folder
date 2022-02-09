# Дано число из отрезка[10, 99] Показать наибольшую цифру числа!

import os
clear = lambda: os.system('cls')
clear()

n = int(input('--->>'))
segment = list(range(10, 99))  #передает segment список из эл.от 10 до 99 по порядку!!!
# print(segment)
for el in segment:
    if n == el:
        if (n // 10) > (n %10):
            print(f'Число = {n}--> ПЕРВАЯ цифра числа {n//10} больше {n %10} ВТОРОЙ цифры числа')
        else:
            print(f'Число = {n} --> ВТОРАЯ цифра числа {n %10} больше ПЕРВОЙ цифры числа {n//10}')




