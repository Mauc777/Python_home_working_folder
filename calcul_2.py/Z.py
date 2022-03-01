import view
import Model_summ
import Model_deduction
import Model_mult
import Model_difference
import inite


# def Znak():
#     return 

def Calc():
    sing_now = view.Vvod_sing()
    if sing_now == '+'  :
        return Model_summ.summ_now()
    if sing_now  == '-'  :
        return Model_deduction.deduction_now()
    if sing_now == '*'  :
        return Model_mult.mult_now()       
    if sing_now == '//'  :
        return Model_difference.difference_now()    