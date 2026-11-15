Blocks in Python:
In Exception Handling we have a 4 types Blocks. 1. Try Block 2. Exception Block 3. Else Block 4. Final Block
1.Try Block  
 ● Try block is a block, when the programmer raises the risky code.
● For the Try Block Exception Block Is mandatory.
● For one Try Block we can create multiple Exception Blocks.
2.Exception Block
● If there is an error is occurred in the Try Block, then control will go to Exception Block.
● We can create multiple Exception Blocks for one Try Block to handle multiple elements.
3.Else Block
● If there is no error in Try Block, then Else Block is executed.
http://4.Final Block
● It is always executed weather the Exception is raised or not.

-------------------------------- Examples refer http://124.py File-----------------------------

# Raise

It is a keyword, it is used to throw exception, whenever user need of it.

-------------------------------- Examples refer http://124.py File-----------------------------
#. User defined Exception  
 ● User defined exceptions are the “Exception Class” created by user
based on the requirement.
● It is used to rectifying an error.
● Every user defined exception should be defined from the exception
class is called “Exception.

-------------------------------- Examples refer http://124.py File-----------------------------

#. Assertion:
● Assert is a keyword; it is used to compare and raised an exception.
● If the condition if False, then it throws exception error.

# Generic Exception:

    # Handling the exception by using Exception Class

'''
Syntax:
try:
pass
except Exception as AliasName:
pass
'''
'''
Syntax:
try:
pass
except BaseException as AliasName:
pass
'''

'''
try:
print({10,20}+{30,40})
except Exception as e:
print(e)
'''

# Blocks in Python

'''
try:
age = int(input("Enter the Number:"))
except:
print("Enter Only Numbers")
else:
if age>=18:
print("Eligible to vote")
else:
print("Not Eligible to vote")

finally:
print("Thank You For Entering")
'''

# raise:

'''
age = int(input("Enter Your Age:"))
if age>=18:
print("Eligible")
else:
raise Exception("Not Eligible")
print("1.EEE\n2.CS\http://n3.IS\http://n4.IT\n5.ECE")
course = input("Enter Your Course:")
print("Enrolled Successfully")
'''

# Assertion:

"""
Syntax:
assert <condition>,FSB
TSB
"""
'''
age = int(input("Age:"))
assert age>=18
print("1.EEE\n2.CS\http://n3.IS\http://n4.IT\n5.ECE")
course = input("Enter Your Course:")
print("Enrolled Successfully")
'''

# Creating user defined Exception:

'''
Syntax:

class ExceptionName(Exception):
pass
'''
'''
class Eligiblity(Exception):
pass

age = int(input("Enter your Age:"))
if age>=18:
print("Eligible to Vote")
else:
raise Eligiblity("Not Eligible")
'''
