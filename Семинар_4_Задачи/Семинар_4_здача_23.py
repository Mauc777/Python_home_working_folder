# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д. Пример: 
# [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
#    0  1  2  3  4
import os
def clear(): return os.system('cls')
clear()

list = [2, 3, 4, 5, 6]
list2 = []
print(list)
res = 0

# for i in range(0,math.ceil(len(list)//2)):
for i in range(len(list)):
     res = list[i]*list[len(list) - 1 - i]
     if i < len(list)/2:
        list2.append(res)
print(list2)

