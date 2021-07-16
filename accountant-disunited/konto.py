import sys
plik = sys.argv[1]

import funkcje_ogolne
from funkcje_ogolne import czyszczenie_logu
from funkcje_ogolne import import_danych
from funkcje_ogolne import test_kasowy
from funkcje_ogolne import test_handlowy

import funkcje_dodatkowe
from funkcje_dodatkowe import saldo_konta

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
    # Podanie aktualnego salda konta:
    saldo_konta()
    # Zakończenie:
    print("Wykaz wprowadzonych danych znajduje się w pliku data_export/log.txt\n")
    print("Saldo konta znajduje się w pliku data_export/saldo.txt\n")