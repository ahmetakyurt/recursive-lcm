import math

n = int(input("Count of numbers: "))

numbers = []
for i in range(n):
    number = int(input(f"Enter {i+ 1} st number: "))
    numbers.append(number)

result = math.lcm(*numbers)
print("Least Common Mulitple:", result)