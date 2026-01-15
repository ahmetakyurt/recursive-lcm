def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x%y)


def lcm(liste):
    if len(liste) == 1:
        return liste[0]

    x, y = liste.pop(0), liste.pop(0)
    mini_ekok = x * y // gcd(x, y)
    liste.insert(0, mini_ekok)
    return lcm(liste)
    
n = int(input("Count of numbers: "))

numbers = []
for i in range(n):
    number = int(input(f"Enter {i+ 1} st number: "))
    numbers.append(number)

result = lcm(numbers)
print("Least Common Mulitple:", result)