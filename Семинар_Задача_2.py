# Пользователь задаёт две строки. Определить
# количество вхождений одной строки в другую.
# Метод find(): Вернет индекс самого ПЕРВОГО СОВПОДЕНИЯ!!!!!!!!!
# >>> x = 'раз два три раз два три раз'
# >>> x.find('раз')
# # 0
# >>> x.find('раз', 10, 23)
# # 12
# >>> x.find('раз', -12)
# # 24
# >>> x = 'раз два три раз два три раз'
# >>> x.find('четыре')
# # -1

# st1 = 'qwertyqwqw'
# st2 = 'qw'
# x = st1.find('qw')
# print(x)

from itertools import count


st1 = 'qwertyqwqw'
st2 = 'qw'

flag = True
count = 0
while flag:
    now_index = st1.find(st2)
    if now_index != -1:
        st1 = st1[now_index + len(st2):]
        count += 1
    else:
        print(count)
        flag = False    



