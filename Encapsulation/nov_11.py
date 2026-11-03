class Company:
    cname="Google"

    def __init__(self,name):
        self.name=name


    @classmethod
    def ch_cname(cls,new):
        cls.name=new

emp1=Company("Manisha")
emp2=Company("Adri")

emp1.ch_cname("Manisha Google")
print(emp1.cname)
print(emp2.cname)
