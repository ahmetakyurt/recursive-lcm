def ebob_hesapla(x, y):
    if x % y == 0:
        return y
    else:
        return ebob_hesapla(y, x%y)


def ekok_hesapla(liste):
    if len(liste) == 1:
        return liste[0]

    x, y = liste.pop(0), liste.pop(0)
    mini_ekok = x * y // ebob_hesapla(x, y)
    liste.insert(0, mini_ekok)
    return ekok_hesapla(liste)
    
n = int(input("Count of numbers: "))

numbers = []
for i in range(n):
    number = int(input(f"Enter {i+ 1} st number: "))
    numbers.append(number)

result = ekok_hesapla(numbers)
print("Least Common Mulitple:", result)