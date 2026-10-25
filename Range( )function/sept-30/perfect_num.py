num= int(input("enter a num :"))
out =0
for i in range(1,num//2+1):
    if num % i == 0:
        out+= i
if num == out:
    print("perfect")
else:
    print("not perfect")
        
