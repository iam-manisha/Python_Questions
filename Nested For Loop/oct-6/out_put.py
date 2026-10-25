#WAP to get the following output
In=[100,200,50,400,300]
Num =300
# Out=[[100,200],[300]]
Out=[]
for i in range(len(In)):
    if In[i]== Num:
        Out.append(In[i])
    for j in range(i+1,len(In)):
        if In[i] + In[j] == Num:
            Out.append([In[i],In[j]])
print(Out)

