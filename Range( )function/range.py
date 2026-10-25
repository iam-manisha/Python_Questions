#wap to generate 5 natural numbers
for i in range(1,6):
    print(i)
print("---------------------------")
#wap to generate 5 whole numbers
for i in range(5):
    print(i)
print("---------------------------")

#wap to generate 5 natural numbers in reverse
for i in range(5,0,-1):
    print(i)
print("---------------------------")
#wap to generate only odd number from 1 to 50

for i in range(1,51):
    if i%2 != 0:
        print(i)

print("---------------------------")
#approach-2
#wap to generate only odd number from 1 to 50
for i in range(1,51,2):
    print(i)
print("---------------------------")

#wap to generate sum of odd number from 1 to 50
odd_sum = 0
for i in range(1,51):
    if i%2 != 0:
        odd_sum+=i
print(odd_sum)


