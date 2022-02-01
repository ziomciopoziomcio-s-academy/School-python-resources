
#Definicja funkcji
def intcheck(check):
    try:
        int(check)
    except ValueError:
        return False
    else:
        return True

#Pierwsze pobranie n i sprawdzenie czy jest liczbą naturalną
n = input("Podaj liczbę do rozkładu na czynniki pierwsze")

if intcheck(n) == True:
    n = int(n)
    if n >= 1:
        ncheck = True
    else:
        ncheck = False
else:
    ncheck = False
    
#Pobieranie n i sprawdzanie czy jest liczbą naturalną do momentu gdy użytkownik wprowadzi liczbę naturalną
while ncheck == False:
    print("Podane dane nie są liczbą naturalną")
    n = input("Podaj liczbę do rozkładu na czynniki pierwsze")
    if intcheck(n) == True:
        n = int(n)
        if n >= 1:
            ncheck = True
        else:
            ncheck = False
    else:
        ncheck = False

print(n)
