#24. Find the greatest of 3 numbers
a = int(input("enter 1st number:"))
b = int(input("enter 2nd number:"))
c = int(input("enter 3rd number:"))
if a > b and a>c:
    print(f"A is greatest:{a}")
elif  b>a  and b>c:
    print(f"B is gretaest :{b}")
else:
    print(f"C is greatest: {c}")