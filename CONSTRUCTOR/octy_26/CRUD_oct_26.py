class Hospital:
    h_name="Saint john"
    h_loc="madiwala"
p1=Hospital()
p2=Hospital()

def add_patient_details(ob):
    data=ob.__dict__
    pname=input("enter the pname")
    value=input("enter the value")
    if pname in data:
        data[pname]=value
        print("data modified successfully")
    else:
        data[pname]=value
        print("data added successfully")
def display_patient_details(ob):
    data=ob.__dict__
    for i in data:
        print(i,data[i])

def remove_patient_details(ob):
    data=ob.__dict__
    pname=input("enter the pname")
    if pname in data:
        data.pop(pname)
        print("Data Remove Successfully")
    else:
        print("data not available")


def main(ob):
    while True:
        print("1.Add Detail\n2.Read Data\n3.Modify Data\n4.Remove Data\n5.Quit")
        choice=int(input("Enter Your Choice:"))
        if choice==1:
            add_patient_details(ob)
        elif choice == 2:
            display_patient_details(ob)
        elif choice==3:
            add_patient_details(ob)
           
        elif choice == 4:
            remove_patient_details(ob)
        elif choice== 5:
            print("Thankyou!!!!")
            break
        else:
            print("enter valid option")

main(p1)



