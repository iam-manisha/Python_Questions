class Parent:

    def show(self):
        print("Parent method")


class Child(Parent):

    def show(self):
        print("Child method")


c1 = Child()
c1.show()
