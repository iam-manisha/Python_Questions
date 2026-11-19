import sqlite3

# 1. Establish connection
connection = sqlite3.connect("demo.db")

# 2. Create cursor
cursor = connection.cursor()

# 3. Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS EMPLOYEES(
    SNO INTEGER,
    NAME TEXT,
    DESIGNATION TEXT,
    PHONE TEXT
)
""")

# 4. Insert data
query = """
INSERT INTO EMPLOYEES
VALUES (?, ?, ?, ?)
"""

cursor.execute(query, (1, "Rocky", "Developer", "9876543210"))

# 5. Save changes
connection.commit()

# 6. Retrieve data
data = cursor.execute("SELECT * FROM EMPLOYEES")

for row in data:
    print(row)

# 7. Close connection
connection.close()
