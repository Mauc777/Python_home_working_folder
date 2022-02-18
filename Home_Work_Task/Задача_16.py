# Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму

def find():
    List = []
    n = 10
    summ = 0
    now_summ =0
    print(n)
    for i in range(1, n+1):
        now_summ = (1+1/n)**n
        summ= summ + now_summ
        List.append(summ)
    print(List)    
find()    
