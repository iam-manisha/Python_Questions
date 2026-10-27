class Hotel:
    h_name="Tropica"
    h_loc="Banglore"

    def __init__(self,name,aadhar,phone_no,add):
        self.name=name
        self.aadhar=aadhar
        self.phoneno=phone_no
        self.add=add

cus1 = Hotel("Piki",63252354812151,25431651335,"Whitefield")
for p,v in cus1.__dict__.items():
    print(p,v)

        