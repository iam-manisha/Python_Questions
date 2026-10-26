# #USER DEFINED CONSTRUCTOR
class Sample:
    def __init__(self):
        print(self)
        print("Constructor is Executing")
ob1=Sample()
print(ob1)
print("----------------------------------------")
class Sample:
    def __init__(self):
        a=10
        return a