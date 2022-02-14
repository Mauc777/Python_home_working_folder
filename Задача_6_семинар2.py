#Программа проверяет пятизначное число на палиндромом

num = input("-->")     #.split('')
if num[0] == num[4] and num[1]== num[3]:
    print('Полиндром')
else:
    print('НЕ Полиндром')    


    ############################################
revers_num=''    
for i in reversed(num):  # ведет i в обратном порядке
    revers_num +=i
if num == revers_num:
# if num == num[::-1]    #срез  
    print("+")
else:
     print("-")       




         