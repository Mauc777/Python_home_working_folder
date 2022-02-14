# # Определить, позицию второго вхождения
# строки в списке либо сообщить, что её нет.

list = ['qwe', 'rte', 'аооа', 'qwe', 'res' 'qwe']
x = 'qwe'

count =0
# print(list.count(x))

for i in range(len(list)):
        if list[i] == x:
            count +=1
            # print(x)
        if count == 2:
            print(i)
        


