# Найти сумму чисел списка стоящих на нечетной позиции
import os
def clear(): return os.system('cls')
clear()
list = [1, 2, 3, 4, 5, 8, 7, 9, 1, 2, 25, 64]
# for i in range(0, len(list)-1)
print(sum(list[1::2]))