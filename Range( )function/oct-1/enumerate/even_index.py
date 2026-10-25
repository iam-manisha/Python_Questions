#wapt extract the value only if the index number is even 
st="hello world"
for i,j in enumerate(st):
    if i%2 ==0:
        print(j)