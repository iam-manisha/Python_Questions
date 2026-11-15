import sqlite3

connection = sqlite3.connect("demo.db")

# print("Database Created Successfully")

cursor = connection.cursor()

# Execute the Query

# 1.Create:

'''
query = 'CREATE TABLE EMPLOYEES(SNO NUMBER,NAME VARCHAR(32),DESIGNATION VARCHAR(32),PHONE NUMBER(10));'
cursor.execute(query)
print("Table Created Successfully")
'''

# Inserting the Data:

'''
query = "INSERT INTO EMPLOYEES VALUES(1,'BAGAVATHI','QA',9876543210);"
cursor.execute(query)
connection.commit()
print("Data Entered Successfully")
'''
'''
for i in range(2,7):
name = input("Enter the Name:")
designation = input("Enter the Role:")
phone_number = int(input("Enter The Phone Number:"))
query = f"INSERT INTO EMPLOYEES VALUES({i},'{name}','{designation}',{phone_number});"
cursor.execute(query)
connection.commit()
print("Data Created Successfully")
'''

# Retrive the data

query = 'SELECT \* FROM EMPLOYEES'
data = cursor.execute(query)

# print(list(data))

for i in data:
print(i)

---

import sqlite3

connection = sqlite3.connect("demo.db")

# print("Database Created Successfully")

cursor = connection.cursor()

# Execute the Query

# 1.Create:

'''
query = 'CREATE TABLE EMPLOYEES(SNO NUMBER,NAME VARCHAR(32),DESIGNATION VARCHAR(32),PHONE NUMBER(10));'
cursor.execute(query)
print("Table Created Successfully")
'''

# Inserting the Data:

'''
query = "INSERT INTO EMPLOYEES VALUES(1,'BAGAVATHI','QA',9876543210);"
cursor.execute(query)
connection.commit()
print("Data Entered Successfully")
'''
'''
for i in range(2,7):
name = input("Enter the Name:")
designation = input("Enter the Role:")
phone_number = int(input("Enter The Phone Number:"))
query = f"INSERT INTO EMPLOYEES VALUES({i},'{name}','{designation}',{phone_number});"
cursor.execute(query)
connection.commit()
print("Data Created Successfully")
'''

# Retrive the data

query = 'SELECT \* FROM EMPLOYEES'
data = cursor.execute(query)

# print(list(data))

for i in data:
print(i)
