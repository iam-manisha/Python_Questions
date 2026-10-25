def isStrong(n):
    dup = n
    strong = 0
    while dup!=0:
        rem=dup%10
        fact=1
        for i in range(1,rem+1):
            fact*=i
        strong +=fact
        dup = dup//10
    if n == strong:
        return True
    else :
        return False

l=[]
st=int(input("enter the Start Range :"))
en=int(input("enter the end Range :"))
for i in range(st,en+1):
    if isStrong(i):
        l.append(i)
print(l)


