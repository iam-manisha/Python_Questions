class Bank:
    bank_name="ICICI"
    bank_branch="Marathahalli"
    balance=0

    def __init__(self,name,phone,aadhar,account_no):
        self.name=name
        self.phone=phone
        self.aadhar=aadhar
        self.account_no=account_no

    def available_balance(self):
        print(f"Available Balance is Rs.{self.balance}")

    def deposit(self):
        print("Deposit")
        amount = int(input("enter the amount:"))

        if amount >0:
            self.balance +=amount
            print(f"Amount Deposit successfully Rs.{amount}")
            print("Do you want to check Balance Y/n")
            choice = input("Enter your choice:").lower()

            if choice=="y":
                self.available_balance()
            elif choice == "n":
                print("Thank you")
            else:
                print("enter the valid choice")
        else:
            print("enter the valid amount")
