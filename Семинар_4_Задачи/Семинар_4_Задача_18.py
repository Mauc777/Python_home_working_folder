# Реализовать алгоритм перемешивания списка. 

# import random
# n = int(input('-->>'))
# my_list = list(range(9))
# # random.shuffle(my_list)
# for i in range(n//2-1):
#     my_list[i], my_list[i+1]= my_list[i+1], my_list[i]

# print(my_list)

# Второй вариант решения ПЕРЕМЕШАТЬ ИНДЕКСЫ РАНДОМНО
import random 
first_list = list(range(9))
for i in range(0,len(first_list)-1):
    j = random.randint(0,len(first_list)-1)
    first_list[i], first_list[j] = first_list[j], first_list[i]

print (first_list)

#  3 ВАРИАН зеркальный перемес
# from re import I
mylist = list(range(9))
print(mylist)
currentIndex = len(mylist)-1
for i in range(0,len(mylist)//2):
    mylist[i],mylist[currentIndex] = mylist[currentIndex],mylist[i]
    currentIndex -= 1
    print(f'{mylist[i]} ', end = "")

print()