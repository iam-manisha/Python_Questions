#71. WAP to print all the integers present in a list.
l=[10,20,'abc',10.5,True,[13,34]]
for i in l:
    if type(i) == int:
        print(i)
