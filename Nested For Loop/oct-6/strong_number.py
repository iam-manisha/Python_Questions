# 118.
# WAP to check whether the number is strong or not.
num = 145
sum = 0
dup = num

for i in range(len(str(num))):
    rem = num%10
    fact=1
    for j in range(1,rem+1):
        fact=fact*j
    sum+=fact
    num=num//10
if sum == dup:
    print("strong")
else:
    print("not")

# num = 145
# dup = num
# sum = 0

# for j in range(len(str(num))):
#     rem = num % 10

#     fact = 1
#     for i in range(1, rem + 1):
#         fact = fact * i

#     sum = sum + fact
#     num = num // 10

# if sum == dup:
#     print("Strong Number")
# else:
#     print("Not a Strong Number")
