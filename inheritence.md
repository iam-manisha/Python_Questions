4.Inheritance:
A child class Inheriting the property from parent class
is called inheritance
Inheritance classified into 5 Types
1.Single Level Inheritance
2.Multi Level Inheritance
3.Multiple Inheritance
4.Hierarchical Inheritance
5.Hybrid Inheritance

1.Single Level Inheritance:
A single child class Inheriting the property from a single
parent is called single level inheritance
Syntax:
class ClassName1:
pass

    	class ClassName2(ClassName1):
    		pass

**\*\***\*\***\*\***\*\***\*\***\*\***\*\*** Examples 124.py **\*\*\*\***\*\***\*\*\*\***\*\*\*\***\*\*\*\***\*\***\*\*\*\***
2.Multi Level Inheritance:
A child class inheriting the property from its parent class and parent class
inheriting the property from its own parent is called multi level Inheritance
Syntax:
class ClassName1:
pass

    	class ClassName2(ClassName1):
    		pass
    	class ClassName3(ClassName2):
    		pass

**\*\***\*\***\*\***\*\***\*\***\*\***\*\*** Examples 124.py **\*\*\*\***\*\***\*\*\*\***\*\*\*\***\*\*\*\***\*\***\*\*\*\***
3.Multiple Inheritance:
A single child class inheriting the property from multiple parent class
is called Multiple Inheritance
Syntax:
class ClassName1:
pass
class ClassName2:
pass
class ClassName3(ClassName1,ClassName2):
pass

**\*\***\*\***\*\***\*\***\*\***\*\***\*\*** Examples 124.py **\*\*\*\***\*\***\*\*\*\***\*\*\*\***\*\*\*\***\*\***\*\*\*\***
4.Hierarchical Inheritance:
Multiple child class inheriting the property from single parent is called
Hierarchical Inheritance
Syntax:
class ClassName1:
pass
class ClassName2(ClassName1):
pass
class ClassName3(ClassName1):
pass

**\*\***\*\***\*\***\*\***\*\***\*\***\*\*** Examples 124.py **\*\*\*\***\*\***\*\*\*\***\*\*\*\***\*\*\*\***\*\***\*\*\*\***
5.Hybrid Inheritance:
Combination of two or more type of inheritance is called Hybrid Inheritance

**\*\***\*\***\*\***\*\***\*\***\*\***\*\*** Examples 124.py **\*\*\*\***\*\***\*\*\*\***\*\*\*\***\*\*\*\***\*\***\*\*\*\***
When to Go Inheritance:
Inheritance we want to inherit a property from one class to another class
then we will go for Inheritance
Inheritance is also known as 'IS_A' Relationship

super() calling:
super() calling statement will be used only in inhertance
When Parent class and child class members name are same to call or
differentiate superclass member name then we go super() calling Statement
Super() calling is an inbult function
By using super()calling we can call variable name,method,constructor
of superclass
Syntax:
super().Parent_class_member_name

METHOD CHAINING:
calling super class method in subclass.
both superclass and subclass method names should be same
SYNTAX:
super().method_name()

**\*\***\*\***\*\***\***\*\***\*\***\*\*** Examples refer 124.py **\*\***\*\*\*\***\*\***\*\***\*\***\*\*\*\***\*\***
CONSTRUCTOR CHAINING:
calling superclass Constructor in subclass is called constructor chaining
Syntax:
super().**init**()

**\*\***\*\***\*\***\***\*\***\*\***\*\*** Examples refer 124.py **\*\***\*\*\*\***\*\***\*\***\*\***\*\*\*\***\*\***

MRO(Method Resolution Order):
In multiple inheritance a child class will inherit a property from multiple
parents there is a possibility of both the parent can have same member
Whenever we are accessing same member name will give ambigity error/Confusion
which parent member
To Avoid this confusion we have MRO Mechanism
MRO will follow left to right priority (child,parent1,parent2)
Whenever we are accessing any member first it will check in child,if the member
is present and it will ignore other parent else it will check for parent1
If the member is not present in ay class then it will throw attributr Error

---

Polymorphism:

    Poly --> Many/ Multiple
    morphism --> Different Forms
    A single object/ identity showing different behaviour at different stages throughout the

life cycle is known as polymorphism.

    Example for polymorphism is method overloading and method overriding

METHOD OVERLOADING:
Developing a multiple methods with the same name but variation in argument list
is called method over loading.
In other programming languages based on no.of.arguments that respective function
will get executed but in python method overriding takes place

    We can't achieve method overloading in python.

METHOD OVERRIDING:

    Developing a method in a subclass with same name and signature as present in

super class but different implementation in subclass is called method overriding.

Operator overloading:
It is a phenemenon of making operators to work on objects of user defined
data type by invoking the respective magic method
Eg:
To make + operator to work on objects user defined datatype it is required
to use **add** magic method
