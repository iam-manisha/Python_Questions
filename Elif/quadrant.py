# #23. Check the quadrant in which the given point is lying
# #       +Y
#         |
#  II     |     I
#         |
# --------+-------- +X
#         |
#  III    |     IV
#         |


# + + → 1st
# - + → 2nd
# - - → 3rd
# + - → 4th

x= int(input("enter x :"))
y= int(input("enter y :"))

if x > 0 and y > 0 :
    print("Ist Quadrant")
elif x < 0 and y > 0 :
    print("2nd Quadrant")
elif x < 0 and y < 0 :
    print("3rd Quadrant")
elif x > 0 and y < 0 :
    print("4th Quadrant")
else:
    print("pointless")