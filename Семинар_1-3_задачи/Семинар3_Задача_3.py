# Подсчитать сумму цифр в вещественном числе.


a = float(input('введи число : '))
# либо так: a = a.replace('.', ' ')   мы избавиться от плавательной точки
sum = 0
for i in str(a):
    if i != '.':
        sum+= int(i)
print(f' sum = {sum}')        


















# a = 25.16
# b = list = [a * 100]

# print(b)
