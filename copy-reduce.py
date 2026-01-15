def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x%y)


def reduce_copy(func, liste):
    result = liste[0]

    for i in range(1, len(liste)):
        result = func(result, liste[i])

    return result
n = int(input("Count of numbers: "))

numbers = []
for i in range(n):
    number = int(input(f"Enter {i+ 1} st number: "))
    numbers.append(number)

result = reduce_copy(lambda x,y : (x*y) // gcd(x,y), numbers)
print("Least Common Mulitple:", result)