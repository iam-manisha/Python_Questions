#HCF 
a=12
b=18
if a<b:
    i=a
else:
    i=b
while i!=0:
    if a % i == 0 and b%i == 0:
        print(i)
        break
    i-=1

