#wap to find the largest and smallest number in a list and return index number along with value
l=[10,15,30,40,60]
largest=0
smallest = l[0]
l_index=None
s_index= None
for i,j in enumerate(l):
    if j > largest:
        largest = j
        l_index=i
    if j < smallest:
        smallest=j
        s_index=i
    elif smallest==j:
        s_index = i
print("largest:",largest,"index no: ",l_index)
print("smallest:",smallest,"index no: ",s_index)

    