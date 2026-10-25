def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a//b

def main():
    while True:
        print("welcome to my calculator")
        n1=int(input("enter a number:"))
        n2=int(input("enter a number:"))
        print("1.Addition\n 2.Substraction\n 3.Multiplication\n 4.Division")
        choice=int(input("enter your choice:"))
        if choice==1:
            print(add(n1,n2))
        elif choice==2:
            print(sub(n1,n2))
        elif choice==3:
            print(mul(n1,n2))
        elif choice==4:
            print(div(n1,n2))
main()

    
