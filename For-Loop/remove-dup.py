#wap to remove all duplicate
#approach-1
l=[10,10,20,20,30]
out = []
for i in l:
    if i not in out:
        out.append(i)
print(out)

print("------------------------")

#app-2
l=[10,10,20,20,30]
out = []
for i in l:
    if i not in out:
        out+=[i]
print(out)