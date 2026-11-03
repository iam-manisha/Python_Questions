class Company:
    cname="Dell"
    cloc="Banglore"

    def __init__(self,ename,eloc):
        self.ename=ename
        self.eloc=eloc

    def display(self):
        print("Name:",self.ename)
        print("Location:",self.eloc)
        print("Company Location:",self.cloc)

    @classmethod
    def ch_cloc(cls,new_value):
        cls.cloc=new_value

emp1=Company("abc","MP")
emp2=Company("def","AP")

emp1.display()
emp2.display()

Company.ch_cloc("Hyderabad")
print("-"*50)


emp1.display()
emp2.display()

    