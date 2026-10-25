import random
otp=random.randint(0000,9999)
print("generated otp:",otp)
user_otp=int(input("enter your otp:"))
chances=3
i=1
while i<=chances:
    if otp == user_otp:
        print("login Successfully")
        break
    
    chances -=1
    print("Attempts Left:",chances)
    i+=1

