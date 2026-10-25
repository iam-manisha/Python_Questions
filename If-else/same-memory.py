#Check whether 2 values are pointing to the same memory or not
a=[10,20,30]
# b=[10,20,30]
b = a


if a is b:
    print("same")
else:
    print("not same")
