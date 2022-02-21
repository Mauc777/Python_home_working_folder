# Задать список из n чисел последовательности (1+1*n)^n  и вывести на экран их сумму.

# n = int(input('Enter No: '))
# a = [i for i in range (1, n)]
# list = list(filter(lambda x: not x%2, a))
# print(list)

# n = (int(input('-->>  ')))
n= 12
my_list = [list(filter(lambda i:  not i%2, (i for i in range(1, n+1))))]
print(my_list)


