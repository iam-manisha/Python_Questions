#WAP to extract all the non-default values from a list.
l=[10,0,0.0,23,45,90,False,0j,None,[],(),'python']
out=[]
for i in l:
    if bool(i) ==True:
        out+=[i]
print(out)
print("--------------------------")

#Wap to replace the space by * present in a string.
s= 'power star'
out =""
for i in s:
    if i == " " :
        out += "*"
    else:
        out += i
print(out)
print("--------------------------")

