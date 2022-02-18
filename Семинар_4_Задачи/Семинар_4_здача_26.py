# Дано число. Составить список чисел Фибоначчи,
#  в том числе для отрицательных индексов. 
from bisect import bisect
import os
def clear(): return os.system('cls')
clear()

# n = int(input('-->>  '))
n = 10
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fib(n-1)+ fib(n-2)     

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fib(n - 2) - fib(n - 1)

list = []
for e in range(1, n):
    list.append(fib(e))  
    list1 = list 
print(list)

list1.sort()
i = bisect(list1,0)
list1[i:]+list1[:i]
list==list1[:n]+list1[n:]


print(list1)







#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1,10):
#     list.append(fib(e))
# print(list)                # Даст:  1 1 2 3 5 8 13 21 34