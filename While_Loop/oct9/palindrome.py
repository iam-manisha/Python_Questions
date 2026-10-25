n=int(input("enter a number:"))
sum=0
dup = n
while n!=0:
    rem = n% 10
    sum=sum *10 + rem
    n=n//10

if dup== sum:
    print("it a Palindrome")
else:
    print("it not a palindrome")
