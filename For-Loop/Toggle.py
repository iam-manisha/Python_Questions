#Toggle a String
st='PyThOn'
out=''
#O/P:-'pYtHoN'
for i in st:
    if i.isalpha():
        if i.isupper():
            out+=i.lower()
        else:
            out+=i.upper()
print(out)

print("---------------------")
#without built in
st='PyThOn'
out=''
#O/P:-'pYtHoN'
for i in st:
    if  'A' <= i <= 'Z':
        out+=chr(ord(i)+32 )
    else:
         out+=chr(ord(i)-32 )
print(out)
