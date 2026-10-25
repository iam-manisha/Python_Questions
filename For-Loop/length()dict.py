st='pyhon is easy'
#{'p': 1, 'y': 2, 'h': 1, 'o': 1, 'n': 1, ' ': 2, 'i': 1, 's': 2, 'e': 1, 'a': 1}

out ={}
for i in st:
    if i not in out:
        out[i] = st.count(i)
print(out)
print("------------------------------")
#without built-in
st='pyhon is easy'
res ={}
for i in st:
    if not i == " ":
        if i not in res:
            res[i] = 1
        else:
            res[i]+=1
print(res)


    
        