# Даны два числа. Показать большее и меньшее число

#  Дописать код
# 
def my_max(a, b):    
    if (a > b):
        print(f'a = {a}, b = {b} --> {a > b}')
        return a
    elif(a < b):
        print(f'a = {a}, b = {b} --> {a < b}')
        return b
num1 = (int(input('-->')))
num2 = (int(input('-->')))

my_max(num1, num2)
#my_max(input('a= '), input('b= '))
