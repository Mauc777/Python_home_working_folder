# Определить номер четверти плоскости, в которой находится
# точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

x = int(input('-->'))
y = int(input('-->'))

if x != 0 and y != 0:
    if 0 < x < 1000 and 0 < y < 1000:
        print("точка находится в 1 четверти")
    elif -1000 < x < 0 and 0 < y < 1000:
        print("точка находится в 2 четверти")

    elif -1000 < x < 0 and -1000 < y < 0:
        print("точка находится в 3 четверти")

    elif 0 < x < 1000 and -1000 < y < 0:
        print("точка находится в 2 четверти")
