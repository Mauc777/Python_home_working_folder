# Реализовать алгоритм задания случайных чисел. Без использования встроенного 
# генератора псевдослучайных чисел

# from pyspectator import Cpu
# print(ctime()%10)
# print(time())

from time import time
print(int(float(time())%20))  #Вариант получения ПСЕВДО-СЛУЧ-ЧИСЕЛ
