##Constructor with Arguments/Parameterize Constructor

class Company:
    cname="wipro"
    cloc="Banglore"

    def __init__(self,ename,eloc,eid,age,phone_no):
        print(ename,eloc,eid,age,phone_no)

emp1=Company("Manisha","Odisha","CS0034",22,6372033120)
#objname.pname
print(emp1.ename) #AttributeError: 'Company' object has no attribute 'ename'.