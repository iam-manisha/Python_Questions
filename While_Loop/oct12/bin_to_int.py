#wap to convert binary to decimal
num = 1100
sum=0
power = 0

while num > 0:
    rem = num % 10
    sum = sum + rem * (2 ** power)
    power = power + 1
    num = num // 10

print(sum)









