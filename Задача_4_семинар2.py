# Дано число. Проверить кратно ли оно 7 и 23

import os
def clear(): return os.system('cls')


clear()

a = 7
b = 23
c = int(input('-->'))
if c % a == 0 and c % b == 0:
    print(f'число кратно {a} и {b}')
else:
    print(f'число НЕ кратно {a} и {b}')
