try:
    age = int(input("Enter the Number:"))

except:
    print("Enter Only Numbers")

else:
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not Eligible to vote")

finally:
    print("Thank You For Entering")
