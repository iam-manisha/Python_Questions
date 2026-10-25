st="abc**ab*ac*"
#o/p='aaa'
out=""
for i in st:
    if i == "*":
        out = out[:-1]
    else:
        out+= i
print(out)