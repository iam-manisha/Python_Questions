#Check whether the character is uppercase, lowercase, digit or special character
ch = input("enter a character :")
if ('A' <=ch <= 'Z'):
    print("Uppercase")
elif 'a' <= ch <= 'z':
    print("Lowercase")
elif '0' <= ch <= '9' :
    print("digit")
else:
    print("Special Character")