# Дано число. Составить список чисел Фибоначчи,
#  в том числе для отрицательных индексов. 
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
# print(fib(5)) 
# n1 = -1
# list2 = []
# for i in range(1,10):
#     n2 = -1*(fib(n-1) - fib(n-2)) 
#     i+= i+1

#     print(fib(i))
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fib(n - 2) - fib(n - 1)

list = []
for e in range(1, 10):
    list.append(fib(e))
print(list)







#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1,10):
#     list.append(fib(e))
# print(list)                # Даст:  1 1 2 3 5 8 13 21 34