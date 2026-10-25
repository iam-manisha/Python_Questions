#wap to extract index number along with its character
st='python'
for i in range(len(st)):
    print(i,st[i])
print("-------------------------")

#reverse a string without using 3rd variable
st='python'
for i in range(len(st)-1,-1,-1):
    print(st[i],end='')
