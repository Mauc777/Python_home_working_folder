# Показать последнюю цифру трехзначного числа

import os
def clear(): return os.system('cls')
clear()

print('Введите ТРЕХзначное число ...')

a = int(input("-->"))
if a > 99 and a < 999:
    print(f'последняя цифра числа = {a % 10}')
else:
    print("Введено не корректное число")
