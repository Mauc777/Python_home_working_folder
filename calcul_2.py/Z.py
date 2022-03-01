import view
import Model_summ
import Model_deduction
import Model_mult
import Model_difference
import inite

# def Znak():
#     return 

def Znach():
    znak = ''
    if view.Znakk_leter() == '+'  :
        return Model_summ.summ_now()
    elif view.Znakk_leter() == '-'  :
        return Model_deduction.deduction_now()
    elif view.Znakk_leter() == '*'  :
        return Model_mult.mult_now()       
    elif view.Znakk_leter() == '//'  :
        return Model_difference.difference_now()    