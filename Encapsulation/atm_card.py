#Public access Specifier    #no underscore
#Protected access specifier #single underscore
#Private access specifier   #double underscore

class ATMCard:
    card_name = "ICICI Bank"   #Public
    _cvv="564"                 #protected

    def get_cvv(self):
        return self._cvv

    def set_cvv(self,new):
        self._cvv = new

p1=ATMCard()
print(p1.get_cvv())
p1.set_cvv(456)
print(p1.get_cvv())

