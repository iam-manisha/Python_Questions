#11
st =input("String :")
i=0
out=""
while i < len(st):
    if "a" <=st[i] <="z":
        out=out+chr(ord(st[i])-32)
    else:
        out=out+chr(ord(st[i])+32)


    i+=1
print(out)
