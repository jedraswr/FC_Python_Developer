import sys
# Inicjowanie i opis zmiennych:
baza = []                               # baza danych
fraza = str()                           # początkowy argument trybu przetwarz.
klasa = str()                           # nazwa klasy szkolnej użytkownika
klucz = str()                           # klucz wyszukiwania danych
marker_k = 1                            # znacznik kontyuowania przetwarzania
nazwa = str()                           # imię i nazwisko użytkownika
numer_klasy = str()                     # nazwa klasy użytkownika
procedura = str()                       # procedura obróbki danych
tryb = str()                            # tryb inicjacji programu
typ = str()                             # typ użytkownika
# Zapisywanie danych użytkowników w standardowym formacie: typ, imię i
# nazwisko, przedmiot, powiązana klasa.
fraza = str(sys.argv[1])
while marker_k == 1:
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
    nazwa = input()
    if typ == "u":                              # wprowadzanie ucznia
        print("Podaj nazwę klasy ucznia:")
        klasa = input()
        zapis = (typ, nazwa, "-", klasa)
        baza.append(zapis)
        continue
    elif typ == "n":                            # wprowadzanie nauczyciela
        print("Podaj nazwę przedmiotu nauczyciela:")
        przedmiot = input()
        while klasa:
            print("Podaj nazwę klasy nauczyciela:")
            klasa = input()
            if klasa:
                zapis = (typ, nazwa, przedmiot, klasa)
                baza.append(zapis)
        continue
    else:                                       #wprowadzanie wychowawcy
        while klasa:
            print("Podaj nazwę klasy wychowawcy:")
            klasa = input()
            if klasa:
                zapis = (typ, nazwa, "-", klasa)
                baza.append(zapis)
        continue
# Określanie trybu i wstępnego klucza przetwarzania:
if len(fraza) <= 5:                           # tryb klasa
    tryb = "klasa"
    klucz = fraza
else:                                          # tryby uczeń, naucz., wych.
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
    for zapis in baza:
        if zapis[3] == klucz and zapis[0] == "w":
            print(zapis[1])
if tryb == "klasa": # wyszukiwanie uczniów klasy
    for zapis in baza:
        if zapis[3] == klucz and zapis[0] == "u":
                    print(zapis[1])
# Procedura w trybie "wychowawca":
if tryb == "wychowawca":
    for zapis in baza:                  # wyszukiwanie klas wychowawcy
        if zapis[1] == klucz and zapis[0] == "w":
            numer_klasy = zapis[3]
            for zapis in baza:          # wyszukiwanie uczniów w klasach
                if zapis[3] == numer_klasy and zapis[0] == "u":
                    print(zapis[1])
# Procedura w trybie "nauczyciel":
if tryb == "nauczyciel":
    for zapis in baza:                  # wyszukiwanie klas nauczyciela
        if zapis[1] == klucz and zapis[0] == "n":
            numer_klasy = zapis[3]
            for zapis in baza:          # wyszukiwanie wychowawców klas,
# ... jeżeli wychowawca prowadzi >1 klas nauczyciela to zapis się powtórzy
                if zapis[3] == numer_klasy and zapis[0] == "w":
                    print(zapis[1])
# Procedura w trybie "uczeń":
if tryb == "uczen":
    for zapis in baza:                  # wyszukiwanie klasy ucznia
        if zapis[1] == klucz and zapis[0] == "u":
            numer_klasy = zapis[3]
            for zapis in baza:          # wyszukiwanie przedmiotów i nauczycieli
# ... jeżeli nauczyciel ma >1 przedmiotów to jego imię i nazwisko się powtórzy
                if zapis[3] == numer_klasy and zapis[0] == "n":
                    print(zapis[2])
                    print(zapis[1])
