#83. WAP to check whether the list is homogeneous or not.
l=[10.0,10.0,0.9,]
for i in l:
    if type(i) == type(l[0]):
        print("homo")
    else:
        print("hetero")
print("---------------------")
#84. WAP to replace the space by * present in a string.
s="star moon"
out = ""
for i in s:
    if i == " ":
        out+= "*"
    else:
        out+=i
print(out)
print("--------------------------")
#85. WAP to count the number of occurrences of a specified character.
s="hello"
ch="l"
count=0
for i in s:
    if i == ch:
        count+=1
print(count)

print("--------------------------")
   


S = 'always keep smiling'

out = ' '

for i in S.split():
    out = out + i[::-1] + ' '

print(out)
