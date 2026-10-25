#wap to check a num is prime or not
num=int(input("enter a num:"))
i=2
count=0
while i<num:
    if num% i==0:
        print("it not a prime number")
        break
    i+=1
    
else:
    print("its a prime number")


