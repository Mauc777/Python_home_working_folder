#  Дана последовательность чисел. Получить список неповторяющихся элементов и
# сходной последовательности
# a = [1, 2, 2, 41, 12, 12, 333, 3, 41, 123, 123]

# b = [list(filter(lambda el: el+1!=el, [el for el in a])) ]
# print(b)

a = [1, 2, 2, 41, 12, 12, 333, 3, 41, 123, 123]
b = []
res = list(filter(lambda x: b.append(x) if x not in b else False, [x for x in a]))

print(b)

