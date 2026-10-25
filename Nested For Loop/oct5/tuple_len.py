st = "python is very easy"
#o/p:-[(python,6),('is',2),('very',4),('easy',4)]
#without len()
out=[]
for i in st.split():
    len=0
    for j in i:
        len+=1
    out= out+[(i,len)]
    # out.append((i,len))

print(out)   


