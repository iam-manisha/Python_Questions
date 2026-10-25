n=int(input("enter a number :"))
dup=n
l=len(str(n))
arm=0
while dup>0:
    rem=dup%10
    arm=arm+rem**l
    dup=dup//10
if n == arm:
    print("armstrong")
else:
    print("not a armstrong")