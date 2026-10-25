num = 13
sum = 0
place = 1

while num > 0:
    rem = num % 2
    sum = sum + rem * place
    place = place * 10
    num = num // 2

print(sum)