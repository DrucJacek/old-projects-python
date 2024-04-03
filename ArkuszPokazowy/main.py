# f = open("liczby_pokaz.txt").read
# l= f.split()
# for i in l:

def pierwsz(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

licz = 0
with open("liczby_pokaz.txt") as plik:
    for wiersz in plik:
        wiersz = wiersz.rstrip()
        m, a, b = wiersz.split(" ")
        m = int(m)
        a = int(a)
        b = int(b)
        if pierwsz(m):
            licz += 1

print(f"Liczba wierszy w których liczba M jest pierwsza: {licz}")