st="python is very easy"
d={}
for i in st.split():
    count=0
    for j in i:
        if j in "AEIOUaeiou":
            count+=1
    d[i] = count
print(d)

