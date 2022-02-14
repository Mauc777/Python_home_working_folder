#  Показать числа от -N до N
import os
def clear(): return os.system('cls')
clear()

n = int(input('-->'))
for i in range(-n-1, n):
    if (n != 0):
        print(f'{(i+1)}',)







