from functools import reduce
import math

n = int(input("Count of numbers: "))

numbers = []
for i in range(n):
    number = int(input(f"Enter {i+ 1} st number: "))
    numbers.append(number)

result = reduce(lambda x, y: (x*y) // math.gcd(x, y), numbers)
print("Least Common Mulitple:", result)