# Definicja zmiennych
d = 2

# Definicja funkcji
def intcheck(check):      #Definicja funkcji sprawdzającej czy podana przez użytkownika wartość jest liczbą całkowitą
    try:                  #Próba
        int(check)        #ustawienia wartości na liczbę
    except ValueError:    #Jeżeli program zwróci błąd
        return False      #funkcja zwróci "Fałsz"
    else:                 #W innym przypadku
        return True       #funkcja zwróci "Prawda"


# Opisanie zasad działania programu
print("Program ma za zadanie wyliczyć czynniki pierwsze podanej liczby naturalnej")

# Pierwsze pobranie n i sprawdzenie czy jest liczbą naturalną
n = input("Podaj liczbę do rozkładu na czynniki pierwsze ")  #Poproszenie użytkownika o podanie wartości zmiennej "n"

if intcheck(n) == True:      #Jeżeli funkcja "intcheck" zwróci wartość "Prawda"
    n = int(n)               #to typ zmiennej zmieni się na liczbę
    if n >= 1:               #Jeżeli liczba wprowadzona przez użytkownika jest większa od 1
        ncheck = True        #to program zmieniając wartość zmiennej "ncheck" na "Prawda" ustali że użytkownik podał liczbę spełniającą wszystkie kryteria
    else:                    #Jeżeli wprowadzona przez użytkownika liczba nie jest większa od 1
        ncheck = False       #to program zmieniając wartość zmiennej "ncheck" na "Fałsz" ustali że użytkownik podał liczbę niespełniającą wszystkie kryteria
else:                        #Jeżeli funkcja "intcheck" zwróci inną wartość niż "Prawda"
    ncheck = False           #to program zmieniając wartość zmiennej "ncheck" na "Fałsz" ustali że użytkownik podał błędne dane

# Pobieranie n i sprawdzanie czy jest liczbą naturalną do momentu gdy użytkownik wprowadzi liczbę naturalną
while ncheck == False:
    print("Podana wartość nie jest liczbą naturalną")
    n = input("Podaj liczbę do rozkładu na czynniki pierwsze ")
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
