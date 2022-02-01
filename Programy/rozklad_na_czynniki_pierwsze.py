# Definicja zmiennych
d = 2

# Definicja funkcji
def intcheck(check):
    try:
        int(check)
    except ValueError:
        return False
    else:
        return True


# Opisanie zasad działania programu
print("Program ma za zadanie wyliczyć czynniki pierwsze podanej liczby naturalnej")

# Pierwsze pobranie n i sprawdzenie czy jest liczbą naturalną
n = input("Podaj liczbę do rozkładu na czynniki pierwsze")

if intcheck(n) == True:
    n = int(n)
    if n >= 1:
        ncheck = True
    else:
        ncheck = False
else:
    ncheck = False

# Pobieranie n i sprawdzanie czy jest liczbą naturalną do momentu gdy użytkownik wprowadzi liczbę naturalną
while ncheck == False:
    print("Podana wartość nie jest liczbą naturalną")
    n = input("Podaj liczbę do rozkładu na czynniki pierwsze")
    if intcheck(n) == True:
        n = int(n)
        if n >= 1:
            ncheck = True
        else:
            ncheck = False
    else:
        ncheck = False

# Rozkład liczby na czynniki pierwsze
if n == 1:
    print("Liczby 1 nie da się rozłożyć na czynniki pierwsze")
else:
    print("Czynniki liczby ", n, ":")
    while n > 1:
        while n % d == 0:
            print(d)
            n = n / d
        d = d + 1

# Zamknięcie programu
input("Wciśnij ENTER w celu zamknięcia programu")
