# Показать последнюю цифру трехзначного числа

import os
clear = lambda: os.system('cls')
clear()

a = 120
print(f'последняя цифра числа = {a % 10}')
