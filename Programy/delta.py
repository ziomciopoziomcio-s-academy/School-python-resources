#Importowanie bibliotek
import math

#Określanie zmiennych 
check = False

#Przedstawienie zasad działania programu
print("Program ma za zadanie wyliczenie możliwych rozwiązań równania kwadratowego")
print("Program przyjmuje liczby całkowite i dziesiętne")
print("UWAGA! W celu wpisania liczby dziesiętnej należy użyć kropki a nie przecinka!")

#Definicja funkcji
def floatcheck(check):
    try:
        float(check)
    except ValueError:
        return False
    else:
        return True

#Pobranie a i sprawdzenie czy to liczba
while check != True:
    a = input("Podaj a: ")
    if a.isnumeric():
        a = int(a)
        check = True
    elif floatcheck(a) != False:
        a = float(a)
        check = True
    else:
        print("Podana wartość jest nieprawidłowa")
check = False
#Pobranie b i sprawdzenie czy to liczba
while check != True:
    b = input("Podaj b: ")
    if b.isnumeric():
        b = int(b)
        check = True
    elif floatcheck(b) != False:
        b = float(b)
        check = True
    else:
        print("Podana wartość jest nieprawidłowa")
check = False
#Pobranie c i sprawdzenie czy to liczba
while check != True:
    c = input("Podaj c: ")
    if c.isnumeric():
        c = int(c)
        check = True
    elif floatcheck(c) != False:
        c = float(c)
        check = True
    else:
        print("Podana wartość jest nieprawidłowa")

if a == 0:                                          #Sprawdzenie czy a to 0
    print("Podana funkcja jest funkcją liniową")
else:
    delta = b ** 2 - (4 * a * c)
    print(delta)
    if delta < 0:                                           #Sprawdzenie czy delta jest mniejsza od 0
        print("To równanie kwadratowe nie ma rozwiązań")
    elif delta == 0:                                        #Sprawdzenie czy delta jest równa 0
        x = -b / (2 * a)
        print("x wynosi ", x)
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print("x1 wynosi ", x1, " a x2 wynosi ", x2)

#Zamknięcie programu
input("Wciśnij ENTER w celu zamknięcia programu")
