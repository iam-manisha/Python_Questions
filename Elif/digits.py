#22. Check whether integer is single digit, two digits, three digits or more than three digits
num = int(input("enter a number :"))

if num>= 0 and num<=9:
    print("single digit")
elif num>=10 and num<= 99:
    print("TWO -DIGIT NUMBER")
elif num >= 100 and num<= 999:
    print("THREE-DIGIT NUMBER")
else:
    print("MORE THAN THREE DIGITS")
