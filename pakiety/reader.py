# Inicjacja zmiennych i importy:
import sys
import os
import csv
baza_danych = []                            # tablica z danymi do zmieniania
fields = []
ilosc_argumentow = int()                    # ilość argumentów przy wywołaniu
kolumna = int ()                            # nr kolumny tablicy dla zmiany
liczba_kolumn = int()                       # liczba kolumn tablicy
liczba_wierszy = int()                      # liczba wierszy tablicy
naglowek = []                               # linia nagłówka tablicy danych
nowe = str()                                # nowa wartość dla zmiany
nr = int()                                  # kolejny nr dla argv[n]
rows = []
scalone = str()                             # nowy zapis if # of , > 2
wiersz = int(1)                             # nr wierasza tablicy dla zmiany
zmiana = []                                 # zestaw danych o zmianie w argv[n]
# Lokalizacja pliku wejściowego:
importowy = sys.argv[1]
while not os.path.exists(importowy):
    print("Nie znaleziono pliku lub ścieżki.")
    print(os.listdir())
    print("Wpisz poprawną lokalizację źródła, lub Koniec:")
    poprawka = input()
    if poprawka == "Koniec":
        exit()
    importowy = poprawka
    continue
# Przygotowanie danych wejściowych:
with open(importowy, "r", encoding="utf-8", newline="") as plik_danych_csv:
    czytajcsv = csv.reader(plik_danych_csv)
    for line in czytajcsv:
        rows.append(line)
        if liczba_kolumn == 0:
            liczba_kolumn = len(line)
    liczba_wierszy = len(rows)
    print("\nDane wejściowe:\n")                # wydruk danych początkowych
    print("Liczba wierszy (z nagłówkiem): {}\n".format(liczba_wierszy))
    print("Dane przed zmianą:")
    for row in rows:
        print(", ".join(row))
        baza_danych.append(row)                 # tworzenie roboczej bazy danych
# Pobieranie danych o zmianie:
ilosc_argumentow = len(sys.argv[::])
zmiana = 1
nr = 3
print("\nZmiany w danych:")
while zmiana:
    zmiana = sys.argv[nr]
    skladniki_zmiana = zmiana.split(',')
    wiersz = int(skladniki_zmiana[0])
    kolumna = int(skladniki_zmiana[1])
    for skladnik in skladniki_zmiana[2:]:   # może być więcej niż 2 przecinki...
        scalone += skladnik + ","
    nowe = scalone[:-1]                     # bez oststniego przecinka
    if wiersz > liczba_wierszy:             # sprawdzanie poprawności zakresu
        print("Przekroczono zakres wierszy w poprawce {},{},{}"\
            .format(wiersz, kolumna, nowe))
    if kolumna > liczba_kolumn:
        print("Przekroczono zakres kolumn w poprawce {},{},{}"\
            .format(wiersz, kolumna, nowe))
    if wiersz <= liczba_wierszy and kolumna <= liczba_kolumn:
        baza_danych[wiersz][kolumna - 1] = nowe    # dodanie zmiany
        print("Dokonano zmianę {},{},{}".format(wiersz, kolumna, nowe))
    scalone = str("")
    if nr < ilosc_argumentow-1:
        nr += 1
    else:
        break
    continue
# Zapisywanie zmienionej tablicy danych:
eksportowy = sys.argv[2]
with open (eksportowy, "w", encoding="utf-8", newline="") as bazacsv:
    zapiszcsv = csv.writer(bazacsv)
    for row in baza_danych:
        zapiszcsv.writerow(row)
print("Zmienione dane zapisano w pliku {}.".format(eksportowy))