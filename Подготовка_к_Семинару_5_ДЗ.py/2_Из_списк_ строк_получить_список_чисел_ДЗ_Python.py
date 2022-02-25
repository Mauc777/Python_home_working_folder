# 2. Из списка строк получить список, содержащий только те элементы, 
#  которые являются числами. Пример:
#  lst = ['asd', '123', '1.23', 'ht', 'fwef322f'] --> ['123', '1.23']
# from curses.ascii import isdigit
# isdigit() 
# 1 варик
# lst = ['asd', '123', '1.23', 'ht', 'fwef322f']
# print(lst[2].isdigit())  # Почему не видит это как цифру? Нужен split?
# mylist = list(filter(lambda i: i.isdigit() == True, lst))
# print(mylist)

lst = ['asd', '123', '1.23', 'ht', 'fwef322f']
my_list  = list(filter(lambda i: i.isdigit(), lst))
print(my_list)