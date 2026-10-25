# 18. consider a tuple of length of 2 and Check whether a tuple is homogeneous or heterogeneous

# Homogeneous → all values have the same type.

# Heterogeneous → values have different types.

a=(10,'hi')
if type(a[0]) == type(a[1]):
    print("Homogeneous")
else:
    print("Heterogeneous")