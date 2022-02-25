# 5. Напишите программу, которая выводит чётные числа из заданного списка 
# ( список чисел можно задачать любой самостоятельно ) и останавливается, 
# если встречает число 237.

# 1ый вариант (ПОЛИНЫ)
a = [8, 1, 2, 3, 5, 8, 13, 21, 6, 3, 2, 34, 237, 55, 66, 12, 89, 14]
# res = list(filter(lambda x: not x % 2 if x == 237: break else False, a))
# print(res)
num_index = [i for i in range(len(a)) if a[i]==237]

if num_index != []:
    a = a[:num_index[0]]
print([x for x in a if not x%2])    
