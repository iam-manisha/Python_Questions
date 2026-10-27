#object method

class Company:
    cname="wipro"
    cloc="Banglore"

    def __init__(self,ename,eloc,eid,designation,phone_no):
        self.ename=ename
        self.eid=eid
        self.eloc=eloc
        self.designation=designation
        self.phone_no=phone_no

    def display(self):
        for i,j in self.__dict__.items():
            print(i,j)

    def ch_loc(self)