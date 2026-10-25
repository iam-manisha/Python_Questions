#wap to return the position of vowel present in the given string
st="python"
for i in range(len(st)):
    if st[i] in "aeiouAEIOU":
        print(i,st[i])

#wap to find the divisors of a particular number  and add it ito a list
#o/p=[1,2,5,10]
num= int(input("enter a num :"))

l=[]

for i in range(1,num+1):
    if num % i == 0:
        l += [i]
print(l)

