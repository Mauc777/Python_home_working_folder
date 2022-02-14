# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
#data.writelines(colors)
# data.write('\nLine 121 \n')
# data.write('Line 132\n')
# data.close()


# with open('file.txt', 'w') as data:
#     data.write('line 15\n')
#     data.write('line 2\n')
#     data.write('red green blue\n')
      # в данном варианте записи в файл разрыв связи происходит автоматически!!!


# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()    


# Передача неограниченного кол-ва аргументов
# def concatenatio(*params):
#     res: str = ""  #либо res = 0 (для чисел)
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w'))  #asdw
# print(concatenatio('a', '1', 'd', '2'))  #a1d2
# print(concatenatio(1,2,3,4))    #TypeError: ...


# Рекурсия!!!
# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1,10):
#     list.append(fib(e))
# print(list)                # Даст:  1 1 2 3 5 8 13 21 34


# Кортежи!!! это НЕИЗМЕНЯЕМЫЕ СПИСКИ. Обр можно, присвоить новые значения элементам -НЕТ!!
# from re import T


# a = (3,4,5,6,8,15)
# for item in a:
#     print(item)

    # Картежи можно распаковать в ОТДЕЛЬНЫЕ ПЕРЕМЕННЫЕ, след образом:
# t = tuple(['red','green','blue'])
# red, green, blue = t 
# print('r:{} g:{} b:{}'.format(red,green,blue))   #r:red g:green b:blue

# Словари
# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
    # }
# print(dictionary)  # дает {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary['left']) #даст -> значение ← 
    
    # Можно распечатать все ключи принтом через цикл for:
# for k in dictionary.keys():
#     print(k)                 # даст все ключи = up left down right

# for k in dictionary.values():
#     print(k)                  # дАСТ ВСЕ значения = ↑ ← ↓ →

# еще один способ добраться до значений:
# for v in dictionary:
#     print(dictionary[v]) #Также получим значения = ↑ ← ↓ →

    # Чтоб задвоить и вывести ключ и само значение смотри ниже: 
# print(dictionary['up'])   
# dictionary['up'] = 'up'
# print(dictionary['up'])


#  Множества!!!
# colors = {'red', 'green', 'blue'}
# colors.add('red')       # при попытки добавит то что имеется он его повторно не добавит
# colors.add('grey')      # добавит 'grey'
# colors.remove('blue')   # удалит 'blue'
# colors.discard('red')   # проверит не удален ли 'blue', если удален то скажет 'ok'
# colors.clear()          #очистит множества
# print(colors)           #











