# 9. Check whether the string is palindrome or not

# A palindrome reads the same from both sides. 
a = input("enter a string :")

if a == a[::-1]:
    print("palindrome")
else:
    print("not palindrom")