# Определить, присутствует ли в заданном списке строк, некоторое число
import os
def clear(): return os.system('cls')


clear()
# n = input('-->')
# n = 12
# check = False
n = int(input(' '))
list = ['13', '16', '12', '123', '1', '8',
        '156', '12', '15', '16', '156', '8896']

for i in range(len(list)):
    list[i] = int(list[i])
    if n == list[i]:
        print(f'Yes {i}')
        # break
else:
    if list[i] != n:
        print('Закончили')
