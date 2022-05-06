# Definicja zmiennych
d = 2       #Najniższy dodatni całkowity dzielnik liczby większy niż 1

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
while ncheck == False:                                              #Do momentu jak zmienna "ncheck" ma wartość "Fałsz"
    print("Podana wartość nie jest liczbą naturalną")               #
    n = input("Podaj liczbę do rozkładu na czynniki pierwsze ")     #Poproszenie użytkownika o podanie wartości zmiennej "n"
    if intcheck(n) == True:                                         #Jeżeli funkcja "intcheck" zwróci wartość "Prawda"
        n = int(n)                                                  #to typ zmiennej zmieni się na liczbę
        if n >= 1:                                                  #Jeżeli liczba wprowadzona przez użytkownika jest większa od 1
            ncheck = True                                           #to program zmieniając wartość zmiennej "ncheck" na "Prawda" ustali że użytkownik podał liczbę spełniającą wszystkie kryteria
        else:                                                       #Jeżeli wprowadzona przez użytkownika liczba nie jest większa od 1
            ncheck = False                                          #to program zmieniając wartość zmiennej "ncheck" na "Fałsz" ustali że użytkownik podał liczbę niespełniającą wszystkie kryteria
    else:                                                           #Jeżeli funkcja "intcheck" zwróci inną wartość niż "Prawda"
        ncheck = False                                              #to program zmieniając wartość zmiennej "ncheck" na "Fałsz" ustali że użytkownik podał błędne dane

# Rozkład liczby na czynniki pierwsze
if n == 1:                                                          #Jeżeli zmienna "n" posiada wartość 1
    print("Liczby 1 nie da się rozłożyć na czynniki pierwsze")      #to nie da się tej wartości rozłożyć na czynniki pierwsze
else:                                                               #W innym przypadku
    print("Czynniki liczby ", n, ":")                               #Program drukuje komunikat "Czynniki liczby n:"
    while n > 1:                                                    #Do momentu jak zmienna "n" jest większa od 1
        while n % d == 0:                                               #Do momentu jak reszta z dzielenia zmiennej "n" przez aktualny dzielnik zapisany jako "d" wynosi 0
            print(d)                                                    #Wyprowadzenie wartości dzielnika "d"
            n = n / d                                                   #Zmiana wartości "n" na "n" podzielone przez dzielnik "d"
        d = d + 1                                                   #Zwiększenie dzielnika "d" o 1

# Zamknięcie programu
input("Wciśnij ENTER w celu zamknięcia programu")
