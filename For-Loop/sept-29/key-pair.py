#WAP to extract key-value pairs from the dictionary only if both keys and values are exactly same.
dict={'a':'a','b':'bob',10:10,20:200}
out={}
for i in dict:
    if i == dict[i]:
        out[i]=dict[i]
print(out)
