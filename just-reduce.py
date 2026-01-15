from functools import reduce

def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x%y)

n = int(input("Count of numbers: "))

numbers = []
for i in range(n):
    number = int(input(f"Enter {i+ 1} st number: "))
    numbers.append(number)

result = reduce(lambda x,y: (x*y) // gcd(x, y), numbers)
print("Least Common Mulitple:", result)