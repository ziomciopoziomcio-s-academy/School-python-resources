#Deklarowanie wartości zmiennych
x = 0 #Zmienna x służy do przechowywania danych wprowadzonych przez użytkownika
pozycja = 1 #Zmienna pozycja służy do przechowywania aktualnej pozycji listy
lista = [] #Tworzy listę

#Definicja funkcji
def floatcheck(x):      #Definuje funkcje i podstawia otrzymane dane pod wewnętrzną zmienną x
    try:                #Jeżeli próba się powiedziedzie to funkcja odda wartość True
        float(x)        #Sprawdzenie czy zmienna x może być ułamkiem dziesiętnym
    except ValueError:  #Jeżeli próba zwróci błąd
        return False    #Funkcja zwróci False
    else:               #W innym przypadku
        return True     #Funkcja zwróci True

#Przedstawienie zasad działania programu
print("Program ma za zadanie sortowanie wprowadzonych przez użytkownika liczb")
print("Program przyjmuje liczby całkowite i dziesiętne")
print("UWAGA! W celu wpisania liczby dziesiętnej należy użyć kropki a nie przecinka!")
print("W celu zatrzymania programu należy wpisać jakąkolwiek inną wartość niż liczba całkowita lub dziesiętna")

#Dopisywanie wartości do listy
while type(x) == float or type(x) == int: #Pętla będzie działała do momentu jeżeli użytkownik wprowadzi liczbę
    print("Podaj liczbę numer ", pozycja, ":") #Drukuje prośbę o podanie liczby numer
    x = input() #Podstawia wpisane dane pod zmienną x
    if x.isnumeric(): #Sprawdza czy zmienna x jest liczbą całkowitą
        x = int(x) #Ustawia typ zmiennej x jako liczba całkowita
        lista.append(x) #Dodaje zmienną x do listy
    elif floatcheck(x) != False: #Uruchamia funkcję floatcheck z wartością zmiennej x a później sprawdza czy funkcja działa
        x = float(x) #Ustawia typ zmiennej x jako ułamek dziesiętny
        lista.append(x) #Dodaje zmienną x do listy
    pozycja = pozycja + 1 #Zwiększa zmienną pozycja o 1

#Segregacja listy oraz oddanie wyników
lista.sort() #Funkcja .sort() sortuje listę rosnąco
print(lista) #Wydruk listy

#Zamknięcie programu
input("Wciśnij ENTER w celu zamknięcia programu") 
