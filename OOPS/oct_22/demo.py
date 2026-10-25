class Demo:
    a=10
    b=20
ob1=Demo()
ob2=Demo()
print("before modification")
print(Demo.a)
print(Demo.b)

print(ob1.a)
print(ob1.a)

print(ob2.a)
print(ob2.a)

#modification
Demo.a=100
ob1.a=1000
Demo.a=10
print("-------------After modify----------------")
print(Demo.a)
print(Demo.b)

print(ob1.a)
print(ob1.b)

print(ob2.a)
print(ob2.b)



