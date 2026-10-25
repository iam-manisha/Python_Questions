#Check whether the given character is special or not
ch =input("enter a character:")
if ch.isalnum():
    print("not a special char.")
else:
    print("its a special")


print("----------------")

# without using built-in function
ch =input("enter a character:")
if  not (('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9')):
    print("special char")
else:
    print("not special")