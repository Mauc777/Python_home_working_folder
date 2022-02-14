# Для натурального n создать словарь индексзначение, состоящий из элементов
# последовательности 3n + 1.
    # n = 3
    # 0: 4
    # 1: 7
    # 2: 10
    # dictionary = {3*n + 1}
dictionary = { }
n = 3
for i in range(0,n+1):
    dictionary[i] = 3* i+1
print(dictionary)


# 2ой вариант решения
a = int(input(' N = '))
dictionary = {}
for i in range(1, a+1):
    dictionary.setdefault(i, 3* i + 1)
print(dictionary)

