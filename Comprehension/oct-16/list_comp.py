# #wap to check if the string start with vowel OR not if it is reverse it and add it to the list else add as it is
l=['apple','mango','orange','banana','grapes']
st=[i[::-1]  if i[0] in 'aeiouAEIOU' else i for i in l]
print(st)


#wap to extract only vowels from the string to the list
s='programming language'
l=[i for i in s if i in 'AEIOUaeiou']
print(l)
# out=[]
# for i in s:
#     if i in 'AEIOUaeiou':
#         out+=i
# print(out)

#wap to check the number end with even or not if is even multiple by 10 else multiply by 5 and add it to the list 
l=[1234,45645,436239,56432,64567]
out=[i*10 if i%10==0 else i*5 for i in l]
print(out)
