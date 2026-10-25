#waptc if the string is palindrome or not without using slicing
st='wwwowww'
out = ''
for i in st:
    out = i + out
if out == st:
    print("palindrome")
else:
    print("not palindrome")

print("-------------------------")
# #Revesrse a tuple 
# t=(10,20,30,40,50)
# out=()
# for i in t:
#     out= (i,) + out
# print(out)

# print("-------------------------")

# #Reverse a List
# l=[10,20,30,40,50]
# out = []
# for i in l:
#     out= [i] + out
# print(out)

# print("-------------------------")
#Reverse a set
s={10,20,30,40,50}
ans=set()
for i in s:
    ans ={i} | ans
print(ans)
print("---------------------------")

#reverse a dict
d={'a':10,'b':20,'c':30}
res = {}
for i in d:
    res ={i:d[i]} | res
print(res)

print("---------------------------")

#approch 2 with typecasting
d={'a':10,'b':20,'c':30}
l= list(d.items())
l.reverse()
print(dict(l))
