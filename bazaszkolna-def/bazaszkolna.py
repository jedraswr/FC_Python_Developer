import sys

#inicjacja i formatowanie zmiennych:
baza = []                               # baza danych
czlowiek = str()                        # imię i nazwisko użytkownika
fraza = str()                           # początkowy argument trybu przetwarz.
klasa = str()                           # nazwa klasy szkolnej użytkownika
klucz = str()                           # klucz wyszukiwania danych
marker_k = 1                            # znacznik kontyuowania przetwarzania
przedmiot = str()                       # przedmiot nauczyciela
tryb = str()                            # tryb inicjacji programu
typ = str()                             # typ użytkownika

# Funkcje:

def dodaj_zapis(typ, osoba, przedmiot, klasa):
    zapis = (typ, osoba, przedmiot, klasa)
    baza.append(zapis)

def znajdz_osobe_po_klasie(klucz, funkcja):
    for zapis in baza:
        if zapis[3] == klucz and zapis[0] == funkcja:
            czlowiek = zapis[1]
            print(czlowiek)
            continue

def znajdz_osobe_po_osobie(klucz, funkcja1, funkcja2):
    for zapis in baza:
        if zapis[1] == klucz and zapis[0] == funkcja1:
            klasa = zapis[3]
            for zapis in baza:
                if zapis[0] == funkcja2 and zapis[3] == klasa:
                    czlowiek = zapis[1]
                    print(czlowiek)
                    continue

def znajdz_osobe_i_przedmiot_po_osobie(klucz, funkcja1, funkcja2):
    for zapis in baza:
        if zapis[1] == klucz and zapis[0] == funkcja1:
            klasa = zapis[3]
            for zapis in baza:
                if zapis[0] == funkcja2 and zapis[3] == klasa:
                    przedmiot = zapis[2]
                    czlowiek = zapis[1]
                    print(przedmiot)
                    print(czlowiek)
                    continue

# Zapisywanie danych użytkowników w formacie: typ, osoba, przedmiot, klasa:
fraza = str(sys.argv[1])
while marker_k == 1:
    przedmiot = "-"
    klasa = "_"
    print("Podaj typ użytkownika:")
    print("u=uczeń, n=nauczyciel, w=wychowawca, k=koniec")
    typ = input()
    if typ == "k" or typ == "":
        marker_k = 0
        break
    if typ != "u" and typ != "n" and typ != "w":
        print("Błędny parametr, podaj jeszcze raz!")
        continue
    print("Podaj imię i nazwisko:")
    osoba = input()
    if typ == "u":                              # wprowadzanie ucznia
        print("Podaj nazwę klasy ucznia:")
        klasa = input()
        dodaj_zapis(typ, osoba, przedmiot, klasa)
        continue
    elif typ == "n":                            # wprowadzanie nauczyciela
        print("Podaj nazwę przedmiotu nauczyciela:")
        przedmiot = input()
        while klasa:
            print("Podaj nazwę klasy nauczyciela:")
            klasa = input()
            if klasa:
                dodaj_zapis(typ, osoba, przedmiot, klasa)
                continue
    else:                                       #wprowadzanie wychowawcy
        while klasa:
            print("Podaj nazwę klasy wychowawcy:")
            klasa = input()
            if klasa:
                dodaj_zapis(typ, osoba, przedmiot, klasa)
        continue

# Określanie trybu i wstępnego klucza przetwarzania:
if len(fraza) <= 5:                 # tryb klasa
    tryb = "klasa"
    klucz = fraza
else:                               # tryby uczeń, nauczyciel, wychowawca
    for zapis in baza:
        if zapis[1] == fraza:
            klucz = zapis[1]
            if zapis[0] == "w":
                tryb = "wychowawca"
            elif zapis[0] == "n":
                tryb = "nauczyciel"
            elif zapis[0] == "u":
                tryb = "uczen"
            else:
                print("W bazie brak zapisu z zawartą frazą.")
            break

# Procedura w trybie "klasa":
if tryb == "klasa":                  # wyszukiwanie wychowawców klasy
    klucz = fraza
    funkcja = "w"
    znajdz_osobe_po_klasie(klucz, funkcja)
    funkcja = "u"
    znajdz_osobe_po_klasie(klucz, funkcja)

# Procedura w trybie "wychowawca":
if tryb == "wychowawca":            # wyszukiwanie klas wychowawcy
    klucz = fraza
    funkcja1 = "w"
    funkcja2 = "u"
    znajdz_osobe_po_osobie(klucz, funkcja1, funkcja2)

# Procedura w trybie "nauczyciel":
if tryb == "nauczyciel":
    klucz = fraza
    funkcja1 = "n"
    funkcja2 = "w"
    znajdz_osobe_po_osobie(klucz, funkcja1, funkcja2)

# Procedura w trybie "uczeń":
if tryb == "uczen":
    klucz = fraza
    funkcja1 = "u"
    funkcja2 = "n"
    znajdz_osobe_i_przedmiot_po_osobie(klucz, funkcja1, funkcja2)
