# without context manager:(explictly)
# create a file:
"""file = open("demo.txt", "x")
print(file)
print("file created successfully")
"""

# with context manager:
# create a file :
with open("demo.txt", "x") as file:
    print("file created successfully")

# note:
# if the file already exist and trying
