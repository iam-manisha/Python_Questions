s= 'power star'
out =""
for i in s:
    if i == " " :
        out += "*"
    else:
        out += i
print(out)
print("--------------------------")

#wap to get 
s= "always keep smiling"
# out =syawla peek gnilims
out=""
for i in s.split():
    out+= i[::-1] + " "
print(out)

print("---------------------------")
#wap to get 
In ='push maadi kushi padi' 
out={}
for i in In.split():
    if len(i) % 2 == 0:
        out[i] = i[0] + i [-1]
    else:
        out[i]=i[ len(i)//2]
print(out)

#wap 
s= "jio.com qsp.in  edu.in file.py"
#out={'com':['jio','fb'],'in':['qsp','edu'],'py':['file']]}
out={}
for i in s.split():
    a= i.split('.')
    if a[-1] not in out:
        out[a[-1]]=[a[0]]
    else:
        out[a[-1]] +=[a[0]]
print(out)
print("---------------------------")

st='aaaaabbbbcccdd'
#o/p:-'a5b4c3d2'
out=''
for i in st:
    if i not in out:
        out+= i + str(st.count(i))
print(out)

print("---------------------------")

st='76124953'
#out='71539624'
even=''
odd=''
for i in st:
    if int(i) %2 ==0:
        even += str(i)
    else:
        odd+= str(i)

print(odd+even)




