#wap to print only mutable data from the given list
l=[10,'python',(10,),[10,20],{10,20,30}]
for i in l:
    if type(i) in [list,set,dict]:
        print(i)