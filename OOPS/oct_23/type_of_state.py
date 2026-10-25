class Institute:
    i_name="Qspider"
    i_loc="Marathahalli"
    class_rooms=11

rahul=Institute()
manisha=Institute()
ritib=Institute()

#Assign the Specific Properties
rahul.name="Rahul"
rahul.age=21

manisha.name="Manisha"
manisha.age=22

ritib.name="Ritib"
ritib.age=22
#Assign the Specific and Generic Properties by using object
print("Institute Name:",rahul.i_name)
print("Institute Location:",rahul.i_loc)
print("Name:",rahul.name)
print("Age:",rahul.age)

print("-"*80)

print("Institute Name:",manisha.i_name)
print("Institute Location:",manisha.i_loc)
print("Name:",manisha.name)
print("Age:",manisha.age)

print("-"*80)


print("Institute Name:",ritib.i_name)
print("Institute Location:",ritib.i_loc)
print("Name:",ritib.name)
print("Age:",ritib.age)

print("-"*80)

#Modification
manisha.i_name="Data Mites"
manisha.i_loc="Marathahalli"

print("-"*80)

ritib.i_name="Qspider"
ritib.i_loc="BTM Layout"

print("Institute Name:",rahul.i_name)
print("Institute Location:",rahul.i_loc)
print("Name:",rahul.name)
print("Age:",rahul.age)

print("-"*80)

print("Institute Name:",manisha.i_name)
print("Institute Location:",manisha.i_loc)
print("Name:",manisha.name)
print("Age:",manisha.age)

print("-"*80)


print("Institute Name:",ritib.i_name)
print("Institute Location:",ritib.i_loc)
print("Name:",ritib.name)
print("Age:",ritib.age)

print("-"*80)

