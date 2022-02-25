# [1,2,1,4,5] --> [4,5]

lst = [1,2,1,4,5]
lst2 = [list(filter(lambda z: z>3,lst))]
print(lst2)