#76. WAP to extract all the lowercase characters in a string only if the ASCII value is even.
st="Python"
for i in st:
    if i.islower():
        if ord(i) % 2 == 0 :
            print(i)