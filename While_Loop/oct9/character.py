#wap to print all the character of a string
st =input("String :")
i=0
while i <= len(st):
    print(st[i])
    i+=1


#7
st =input("String :")
i=0
out=""
while i <= len(st):
    if i%2==0:
        out+=st[i]
    i+=1
print(out)

#9
st =input("String :")
vowel=""
i=0
out=""
while i <= len(st):
    if st[i] in 'aeiouAEIOU' :
        vowel+=st[i]
    i+=1
print(vowel)

#10
n=int(input("enter a number "))
i=1
out=[]
while i<=n:
    if n%i==0:
        out+=[i]
    i+=1
print(out)

#11
st =input("String :")
i=0
out=""
while i <= len(st):
    if "a" <=st[i] <="z":
        out=out+chr(ord(st[i])-32)
    else:
        out=out+chr(ord(st[i])+32)


    i+=1
print(out)
