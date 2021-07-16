import sys
plik = sys.argv[1]
nr_od = sys.argv[2]
nr_do = sys.argv[3]

import funkcje_ogolne
from funkcje_ogolne import czyszczenie_logu
from funkcje_ogolne import import_danych
from funkcje_ogolne import test_kasowy
from funkcje_ogolne import test_handlowy

import funkcje_dodatkowe
from funkcje_dodatkowe import przeglad_akcji

# Import danych:
print("Czy chcesz zaimportować operacje z pliku T/N?")
decyzja = input()
if decyzja == "T":
    czyszczenie_logu()
    import_danych(plik)
    print("Wykonano import danych.\n")
    # Testy poprawności merytorycznej zaimportowanych danych:
    test_kasowy()
    test_handlowy()
    # Wykonywanie przeglądu akcji:
    przeglad_akcji(nr_od, nr_do)
    # Zakończenie:
    print("Wykaz wprowadzonych danych znajduje się w pliku data_export/log.txt\n")
    print("Wykaz podjętych akcji, bankowych i handlowych, \
znajduje się w pliku data_export/akcje.txt\n")