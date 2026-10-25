#wap to remove the vowel from the string
# st="apple"
# #o/p:- "ppl"
# out = ""
# for i in st:
#     if i not in 'aeiouAEIOU':
#         out = out+ i
# print(out)

#wap to count the vowel character
st='pyhon is easy'
#out=
out ={}
for i in st:
    if i in 'aeiouAEIOU':
        if not i == " ":
            if i not in out:
                out[i] = 1
            else:
                out[i] += 1
print(out)               


#wap to find the longest substring
st='pyhon is a programming language'
#out = 'programming'
out = ''
length = 0
for i in st.split():
    if len(i) > length:
        length = len(i)
        out = i
print("longest:",out)

    
