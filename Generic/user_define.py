class Eligibility(Exception):
    pass


age = int(input("Enter your Age: "))

if age >= 18:
    print("Eligible to Vote")

else:
    raise Eligibility("Not Eligible")
