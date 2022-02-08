# Показать последнюю цифру трехзначного числа

import os
clear = lambda: os.system('cls')
clear()

a = int(input("-->"))
if a > 99 and a < 999: 
    print(f'последняя цифра числа = {a % 10}')
else:
    print("Введено не корректное число")    
