#wap to find the divisors of a particular number  and add it ito a list
#o/p=[1,2,5,10]
num= int(input("enter a num :"))

l=[]

for i in range(1,num+1):
    if num % i == 0:
        l += [i]
print(l)
