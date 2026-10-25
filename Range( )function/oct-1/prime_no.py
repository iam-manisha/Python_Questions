n= 5
flag=False
for i in range (2,n):
    if n% i == 0:
        flag = False
        break
    else:
        flag=True
if flag== True:
    print("prime number")
else:
    print("not a prime number")

print("---------------------------")

n=4
for i in range(2,n):
    if n % i ==0:
        print("not a prime number")
        break
else:
    print("prime number")

