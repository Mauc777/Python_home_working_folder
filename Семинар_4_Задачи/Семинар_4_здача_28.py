# Найти корни квадратного уравнения Ax² + Bx + C = 0
# Математикой
# Используя дополнительные библиотеки* самостоятельно

import math
import os
def clear(): return os.system('cls')


clear()


def simple(*args):
    a, b, c = args
    d = b**2 - 4*a*c
# a , b ,c = 3,2,3
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        # print('x1 = %.2f \n x2 = %.2f' % (x1, x2)) #печать x1 и x2 с округление до 2 
                                            # знач.после (,) плавающ.запят
        print(f'x1 = {x1},\nx2 = {x2}')
    elif d == 0:
        return -b / (2*a) , print('1')
    else:
        return None, print('корней нет')


print(simple(12, 144, 12))
