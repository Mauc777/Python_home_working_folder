# 3. Посчитайте, сколько раз символ 'f' встречается в строке 'fmkasdo08f1fnacaofonfaf'.
# 1 варик
# str1 = 'fmkasdo08f1fnacaofonfaf'
# print(str1.count('f'))

# 2 варик через каунт
# from itertools import count
# from re import I
# initialString = 'fmkasdo08f1fnacaofonfaf'
# countF = initialString.count('f')
# print(countF)

# str = ['fmkasdo08f1fnacaofonfaf']
# f = ['f']
# # count = 0
# str2 = [ f for f in str ]
# print(str2)


my_str =[]
my_list = ['fmkasdo08f1fnacaofonfaf']
# count_bv = []
res = list(filter(lambda x: my_str.append(x) if x =='f' else False, 'fmkasdo08f1fnacaofonfaf'))
# res = list(filter(lambda x: count_bv.apptnd('f') if x == 'f' else False, my_list))
print(len(my_str))
