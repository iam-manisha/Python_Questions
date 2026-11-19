"""
conn = sqlite3.connect("demo.db")
cursor = conn.cursor()
"""

# Create a Table:

"""
query = "CREATE TABLE PRODUCTS (SNO NUMBER,PRODUCT_NAME VARCHAR(100),PRICE NUMBER(10),QUANTITY NUMBER(5));"
cursor.execute(query)
print("Table is Created Successfully")
"""

# Insert values:

'''
query = "INSERT INTO PRODUCTS VALUES(1,'IPHONE 17',89999,10)"
cursor.execute(query)
conn.commit()
print("Data Entered Successfully")  
'''

# Read the Data from the data base

"""
query = "SELECT \* FROM PRODUCTS"
data = cursor.execute(query)

# print(data)

# App 1 (Type Casting)

# print(list(data))

# App 2 (For Loop)

# for i in data:

# print(i)

"""

# Adding a column to products Table:

"""
query = 'ALTER TABLE PRODUCTS ADD DISCOUNT NUMBER(3)'
cursor.execute(query)
print("Column Added Successfully")
"""

# Updating the price of iphone 17

"""
query = "UPDATE PRODUCTS SET PRICE=86999 WHERE PRODUCT_NAME='IPHONE 17'"
cursor.execute(query)
conn.commit()
print("UPdated Successfully")
"""

# Delete the Column

'''
query = "ALTER TABLE PRODUCTS DROP COLUMN DISCOUNT"
cursor.execute(query)
print("Deleted Successfully")
'''

# Delete the Data

"""
query = "DELETE FROM PRODUCTS WHERE PRODUCT_NAME='IPHONE 17'"
cursor.execute(query)
conn.commit()
print("Product Deleted Successfully")
"""

# Creating a table to store the credential of a user

conn = sqlite3.connect("credentials.db")
cursor = conn.cursor()
"""
query = "CREATE TABLE USER (SNO NUMBER(4),FIRSTNAME VARCHAR(100),LASTNAME VARCHAR(100),EMAIL VARCHAR (100),PHONE_NUMBER NUMBER(10),PASSWORD VARCHAR(100),CONFIRM_PASSWORD VARCHAR(100))"
cursor.execute(query)
"""
"""
query = f"INSERT INTO USER VALUES(1,'john','cena','john@gmail.com',1234567890,'johncena','johncena')"
cursor.execute(query)
conn.commit()
"""
class LoginFunctionality:

    def signup(self):
        print("Welcome to Signup")
        data = list(cursor.execute("SELECT * FROM USER"))
        sno = int(data[-1][0])+1

        firstname = input("Enter your FirstName:")
        lastname = input("Enter your LastName:")
        email = input("Enter your Email:")
        phoneno = int(input("Enter your Phone No:"))
        password = input("Enter Your Password:")
        confirm_password = input("Enter Your Confirm Password:")
        if password == confirm_password:
            query = f"INSERT INTO USER VALUES({sno},'{firstname}','{lastname}','{email}',{phoneno},'{password}','{confirm_password}')"
            cursor.execute(query)
            conn.commit()
            print("Account Created Successfully")
        else:
            print("Password Mismatch")

    def login(self):
        print("Welcome to Login Page")
        email = input("Enter the Mail id:")
        password = input("Enter the Password")

        query = f"SELECT EMAIL,PASSWORD FROM USER WHERE EMAIL='{email}' and PASSWORD='{password}'"

        data = list(cursor.execute(query))
        if data != []:
            print("Logged in Successfully")
        else:
            print("Invalid Username or Password")

    def main(self):
        while True:
            print("1.Signup\n2.Login\n3.quit")
            choice = int(input("Enter Your choice:"))
            if choice == 1:
                self.signup()
            elif choice == 2:
                self.login()
            elif choice == 3:
                print("Thank You")
                break
            else:
                print("Enter the Valid Option")

ob = LoginFunctionality()
ob.main()
