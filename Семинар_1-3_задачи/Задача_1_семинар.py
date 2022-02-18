# Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
                                 # not(X + Y) = not X * not Y

# Конъюнкция (Логическое умножение):  F = A & B.  // F = A * B
# Дизъюнкция (Логическое сложение) :  F = A + B.

import os
clear = lambda: os.system('cls')  
clear()  

# X = True
# Y = False

def Disjunction(X, Y):
    if X == True and Y == True:
        X + Y == True, print("True")
    if X == True and Y == False:
        X + Y == True, print("False")
    elif X == False and Y == True:
        X + Y == True, print("False") 
    elif X == False and Y == False:
        X + Y == False, print("False")  

def Сonjunctionality(X, Y):  
    if X == True and Y == True:
        X * Y == True, print("True")
    if X == True and Y == False:
        X * Y == False, print("False")
    elif X == False and Y == True:
        X * Y == False, print("False")          
    elif X == False and Y == False:
        X * Y == False, print("False")  

X = True
Y = False

# ¬(X ⋁ Y) = ¬X ⋀ ¬Y
if  not(X or Y) ==  (not X) and (not Y):
    print('+ = True')
else: 
    print('- = False')    

Сonjunctionality(X, Y)
Disjunction(X, Y)
