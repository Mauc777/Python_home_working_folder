# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [1, 2, 3, 4]     имеем
# [ 1, 2, 6, 24 ]  должны получить
#   0  1  2   3

# 1 вариант решения детский )))
# n = 4
# a = list(range(1,n+1))
# print(f'{a[0] * a[0]}, {a[0] * a[1]}, {a[1] * a[2]}, {(a[1] * a[2])* a[3]}')
import os
clear = lambda: os.system('cls')
clear()
n = 4
a = list(range(1,n+1))
product = 1
print(a, end = ' --> ')
b = []
for i in a:
    product*= i
    b.append(product)
    # print(f'{product}', end=' ')  как вариант))
print(b)    
 



        
    


