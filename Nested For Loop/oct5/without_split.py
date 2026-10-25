st="python is very easy"
out = []
word =""
for i in st:
    if i != " ":
        word+=i
    else:
        out+=[word]
        word=""
out+=[word]
print(out)
       


