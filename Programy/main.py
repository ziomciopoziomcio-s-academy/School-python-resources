#Deklarowanie wartości zmiennych
x = float(0)
pozycja = 1
lista = []

#Definicja funkcji
def floatcheck(x):
    try:
        float(x)
    except ValueError:
        return False

#Przedstawienie zasad działania programu
print("Program ma za zadanie sortowanie wprowadzonych przez użytkownika liczb")
print("Program przyjmuje liczby całkowite i dziesiętne")
print("UWAGA! W celu wpisania liczby dziesiętnej należy użyć kropki a nie przecinka!")
print("W celu zatrzymania programu należy wpisać jakąkolwiek inną wartość niż liczba całkowita lub dziesiętna")

#Dopisywanie wartości do listy
while type(x) == float or type(x) == int:
    print("Podaj liczbę numer ", pozycja, ":")
    x = input()
    if x.isnumeric():
        x = int(x)
        lista.append(x)
    elif floatcheck(x) != False:
        x = float(x)
        lista.append(x)
    pozycja = pozycja + 1

#Segregacja listy oraz oddanie wyników
lista.sort()
print(lista)

#Zamknięcie programu
input("Wciśnij ENTER w celu zamknięcia programu")