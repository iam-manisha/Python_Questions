class Payments:
    def __init__(self):
        print("RBI Guideliness")
        print("Paying through UPI....")

class Phonepe(Payments):
    def __init__(self):
        super().__init__()
        print("Payment Done using Phonepe")


class Gpay(Payments):
    def __init__(self):
        super().__init__()
       
        print("Payment Done using Gpay")

class Gpay(Payments):
    def __init__(self):
        super().__init__()
        print("Payment Done using Gpay")

class Mobile(Phonepe,Gpay):
    def __init__(self):
        print("Payment App:\n1.Phonepe\n2.Google Pay")
        choice = int(input("enter your choice"))
        if choice == 1:
            super().__init__()
        elif choice ==2:
            Gpay.__init__(self)
        else:
            print("Invalid Choice")


obj = Mobile()

              
