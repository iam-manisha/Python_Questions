st="java is dabba language"
# o/p:={'java':['java',2,avaj]}
out={}

for i in st.split():
    count=0
    for j in i:
        if j in "AEIOUaeiou":
            count+=1
            out[i]=[i,count,i[::-1]]
print(out)
