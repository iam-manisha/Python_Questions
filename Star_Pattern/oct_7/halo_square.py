num = 5
for i in range(1,6):
    for j in range(1,6):
        if i ==1 or j==1 or j==num or i == num:
            print("*",end="")
        else:
            print(" ",end="")
    print()
                        