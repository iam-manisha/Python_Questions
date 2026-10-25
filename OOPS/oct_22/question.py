class Company:
    employees = [
    {"emp_id": 101, "name": "Rahul", "age": 25, "department": "IT", "salary": 45000},
    {"emp_id": 102, "name": "Priya", "age": 28, "department": "HR", "salary": 40000},
    {"emp_id": 103, "name": "Amit", "age": 30, "department": "Finance", "salary": 55000},
    {"emp_id": 104, "name": "Sneha", "age": 26, "department": "Marketing", "salary": 42000},
    {"emp_id": 105, "name": "Kiran", "age": 32, "department": "IT", "salary": 60000},
    {"emp_id": 106, "name": "Neha", "age": 27, "department": "Sales", "salary": 38000},
    {"emp_id": 107, "name": "Arjun", "age": 29, "department": "IT", "salary": 50000},
    {"emp_id": 108, "name": "Divya", "age": 24, "department": "HR", "salary": 35000},
    {"emp_id": 109, "name": "Vikram", "age": 35, "department": "Finance", "salary": 65000},
    {"emp_id": 110, "name": "Ananya", "age": 31, "department": "Marketing", "salary": 48000}
    ]
print("-"*50)
print("------dispaly all employe details-------")
for i in Company.employees:
    print(i)
print("-"*50)
print("-----Display only the names of all employees----------")
for i in Company.employees:
    print(i["name"])
print("-"*50)
print("------Display the names and salaries of all employees.---------------")
for i in Company.employees:
    print(f'{i["name"]} : {i["salary"]}')
print("-"*50)
print("------Find the employee details whose emp_id is 105----------")
for i in Company.employees:
    if i["emp_id"]==105:
        print(i)
print("-"*50)
print("------# Display employees whose salary is greater than 45,000--------")

for i in Company.employees:
    if i["salary"]>45000:
        print(i)
print("-"*50)
print("------## Display employees whose salary is less than 40,000.##--------")

for i in Company.employees:
    if i["salary"]<45000:
        print(i)

print("-"*50)
print("------## Display employees who work in the IT department..## -------")

for i in Company.employees:
    if i["department"]=="IT":
        print(i)

print("-"*50)
print("------##..Count the total number of employees..## -------")
count=0
for i in Company.employees:
    count+=1
print(count)

print("-"*50)
print("------##...Find the employee who receives the highest salary...## -------")
sal=0
for i in Company.employees:
    if i["salary"]>sal:
        name=i["name"]
        sal=i["salary"]
print(name)
# print("------##... Find the employee who receives the lowest salary...## -------")

# sal=0
# for i in Company.employees:
#     if i["salary"]<sal:
#         name=i["name"]
#         sal=i["salary"]
# print(name)
# print("------##...Display employees whose age is greater than 28. ...## -------")
# for i in Company.employees:
