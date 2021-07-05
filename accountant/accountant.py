import sys
# Listy kontrolne:
inicjatory = {"saldo", "sprzedaz", "zakup", "konto", "magazyn", "przeglad"}
operacje = {"Z", "S", "L", "O"}
# Inicjowanie i opis zmiennych:
cena = 0.00                 # cena produktu w operacji
ilosc = 0                   # ilość produktów w operacji
# inicjatory                  zbiór dozwolonych trybów inicjacji programu
konto = 0.00                # stan konta bankowego
kwota_b = 0.00              # kwota operacji bankowej
marker_k = 1                # znacznik czy kontynuować działanie programu
nowa_ilosc = 0              # pomocnicza zmienna do zmiany stanów magazynowych
nr = 0                      # numer listowanej operacji
nr_do = 0                   # numer końcowy operacji
nr_od = 0                   # numer początkowy operacji
# opercacje                   zbiór dozwolonych typów operacji
opis_b = str()              # opis operacji bankowej
rejestr_b = []              # wykaz operacji bankowych
rejestr_m = []              # wykaz operacji magazynowych
stan = 0                    # stan towarów w magazynie
towary = set()              # wykaz identyfikatorów towarów
towar_id = []               # identyfikator towaru
tryb = str()                # tryb startowego inicjowania programu
wartosc = 0.00              # wartość produktów w operacji
wpisy = []                  # lista entry do programu
zapasy = {}                 # stany towarów w magazynie
zapas_co = str()            # identyfikator towaru przy listingu z magazynu
zapas_ile = 0               # ilość towarów przy listingu z magazynu
zestawienie = str()         # znacznik uruchomienia listingu z konta bankowego
# Test prawidłowości wprowadzenia parametru inicjującego:
tryb = sys.argv[1]
if tryb not in inicjatory:
    print("Błędny tryb zainicjowania programu")
    marker_k = 0
while marker_k == 1:
    print("Wybierz rodzaj operacji:")
    print("Z=Zakup, S=Sprzedaż, L=saLdo, O=kOniec")
    akcja = input()
    wpisy.append(akcja)
# Test prawidłowości wyboru:
    if akcja not in operacje:
        marker_k = 0
        print("Błędny rodzaj operacji - program przerwany.")
    elif akcja == "O":
        print("Do zobaczenia! :-)")
        marker_k = 0
        break
    else:
# Operacje bankowe:
        if akcja == "L":
            print("Podaj kwotę operacji bankowej +wpłata/-wypłata:")
            kwota_b = float(input())
            wpisy.append(kwota_b)
            print("Podaj opis operacji bankowej")
            opis_b = input()
            wpisy.append(opis_b)
            zapis_b = (kwota_b, opis_b)
            konto += kwota_b
            rejestr_b.append(zapis_b)
            continue
# Operacje zakupu:
        if akcja == "Z":
            print("Podaj nazwę towaru:")
            towar_id = input()
            wpisy.append(towar_id)
            print("Podaj ilość towarów:")
            ilosc = int(input())
            if ilosc < 0:
                print("Błąd - ilość mniejsza niż 1, wprowadź operację ponownie!")
                continue
            wpisy.append(ilosc)
            print("Podaj cenę towaru w zł:")
            cena = int(input())
            if cena < 0:
                print("Błąd - ujemna cena, wprowadź operację ponownie!")
                continue
            wpisy.append(cena)
            wartosc = ilosc * cena
            if konto < wartosc:
                print("Za duży zakup - brak pieniędzy, wprowadź operację ponownie!")
                continue
            wartosc = wartosc * -1                  # uzupełnianie danych bankowych
            konto += wartosc
            zapis_b = (wartosc, "Zakup {}".format(towar_id))
            rejestr_b.append(zapis_b)
            zapis_m = (towar_id, ilosc, cena)       # uzupełnianie danych magazynowych
            rejestr_m.append(zapis_m)
            if towar_id not in towary:
                towary.add(towar_id)
            if towar_id not in zapasy:
                zapasy[towar_id] = ilosc
            else:
                nowa_ilosc = zapasy.get(towar_id) + ilosc
                zapasy[towar_id] = nowa_ilosc
            print(zapasy.get(towar_id))
            continue
# Operacje sprzedaży:
        if akcja == "S":
            print("Podaj nazwę towaru:")
            towar_id=input()
            if towar_id not in towary:
                print("Błąd - nieistniejący towar, wprowadź operację ponownie!")
                continue
            wpisy.append(towar_id)
            print("Podaj ilość towaru:")
            ilosc = int(input())
            if ilosc <=0:
                print("Błąd - ujemna lub zerowa ilość towarów, wprowadź operację ponownie!")
                continue
            wpisy.append(ilosc)
            stan = zapasy.get(towar_id)
            if ilosc > stan:
                print("Błąd - nie ma tylu towarów, stan = {}, wprowadź operację ponownie!"\
                      .format(stan))
                continue
            print("Podaj cenę jednostkową (zł):")
            cena = int(input())
            if cena <= 0:
                print("Błąd - cena ma ujemna lub zerowa, wprowadź operację ponownie!")
                continue
            wpisy.append(cena)
            wartosc = cena * ilosc
            konto += wartosc                            # uzupełnianie danych bankowych
            zapis_b = (wartosc, "Sprzedaż {}".format(towar_id))
            rejestr_b.append(zapis_b)
            zapis_m = (towar_id, - ilosc, cena)         # uzupełnienie danych magazynowych
            rejestr_m.append(zapis_m)
            nowa_ilosc = zapasy.get(towar_id) - ilosc
            zapasy[towar_id] = nowa_ilosc
            continue
# Dane z konta bankowego
if tryb == "konto":
    print("Aktualny stan konta: {}".format(konto))
    print("Czy chcesz zestawienie transacji w banku? (T/N)")
    zestawienie = input()
    if zestawienie == "T":
        print("Jeśli chcesz, zawęź zakres numerów operacji: od nr:")
        nr_od = input()
        if not nr_od:
            nr_od = 0
        else:
            nr_od = int(nr_od) - 1
        print("...do nr:")
        nr_do = input()
        if not nr_do:
            nr_do = 999999999
        else:
            nr_do = int(nr_do)
        nr = nr_od
        for elem in rejestr_b[nr_od:nr_do]:
            nr += 1
            kwota = elem[0]
            opis = elem[1]
            print("Nr {}    {}    {}".format(nr, round(kwota,2), opis))
# Stany magazynowe:
if tryb == "magazyn":
    print("Stan towarów w magazynie:")
    for elem in zapasy:
        zapas_co = elem
        zapas_ile = zapasy[zapas_co]
        print("{}    {}".format(zapas_co, zapas_ile))
# Przegląd operacji handlowych:
if tryb == "przeglad":
    print("Zestawienie operacji handlowych")
    print("Jeśli chcesz, zawęź zakres operacji: od nr:")
    nr_od = input()
    if not nr_od:
        nr_od = 0
    else:
        nr_od = int(nr_od) - 1
    print("...do nr:")
    nr_do = input()
    if not nr_do:
        nr_do = 999999999
    else:
        nr_do = int(nr_do)
    nr = nr_od
    print("nr - towar - ilość - cena:")
    for elem in rejestr_m[nr_od:nr_do]:
        nr += 1
        towar = elem[0]
        ilosc = elem[1]
        cena = elem[2]
        print("{}    {}    {}    {}".format(nr, towar, ilosc, cena))
# Końcowy listing danych wprowadzonych do systemu:
if tryb in inicjatory:
    print("Wprowadzone dane:")
    for zapis in wpisy:
        print(zapis)