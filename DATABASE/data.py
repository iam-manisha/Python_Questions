import sqlite3

connection = sqlite3.connect("mydatabase.db")
cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS EMPLOYEES (
    ID INTEGER PRIMARY KEY,
    NAME TEXT,
    DESIGNATION TEXT,
    PHONE_NUMBER TEXT
)
""")

# # Insert data
# cursor.execute("""
# INSERT INTO EMPLOYEES
# VALUES (1, 'manisha', 'Developer', '9876543210')
# """)

# connection.commit()

# print("Data inserted successfully!")

# Step 4: Insert multiple records
for i in range(2, 7):
    name = input("Enter the Name: ")
    designation = input("Enter the Role: ")
    phone_number = input("Enter The Phone Number: ")

    query = "INSERT INTO EMPLOYEES VALUES (?, ?, ?, ?)"

    cursor.execute(query, (i, name, designation, phone_number))
    connection.commit()

    print("Data Created Successfully")

# Display data
cursor.execute("SELECT * FROM EMPLOYEES")
for row in cursor.fetchall():
    print(row)
connection.close()
