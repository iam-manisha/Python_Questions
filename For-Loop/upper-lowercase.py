#wap to count no.of uppercase and lowercase characters
st="PytHon124@"
upper=0
lower=0
for i in st:
    if i.isalpha():
        if i.isupper():
            upper+=1
        else:
            lower+=1
print("upper",upper)
print("lower",lower)




