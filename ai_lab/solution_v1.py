
def ebob(a, b):
    
    return ebob(b, a % b) if b else a

def ekok_hesapla(liste):
    
    res = liste[0]
    for i in range(1, len(liste)):
        res = (res * liste[i]) // ebob(res, liste[i])
    return res

n = int(input("Count of numbers: "))

numbers = []
for i in range(n):
    number = int(input(f"Enter {i+ 1} st number: "))
    numbers.append(number)

result = ekok_hesapla(numbers)
print("Least Common Mulitple:", result)