st ='aaaabbc'
max_count= 0
char=''
for i in st:
    if st.count(i) > max_count:
        max_count=st.count(i)
        char = i
print(char)

# WAP to extract all the key-value pairs from the dictionary only if the keys are of string datatype and values are integers.
d= {10:'hello','a':[10,20,30],'b':20,'c':{10,20},'d':40}
#o/p:[{'b':20,'d':40}]
out={}
for i in d:
    if type(i) == str and type(d[i]) == int:
        out[i] = d[i]
print(out)
    
