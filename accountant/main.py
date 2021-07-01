# Listy kontrolne:
operacje = {"Z", "S", "L", "K", "M", "P", "O"}
# Inicjowanie i opis zmiennych:
cena = 0.00                 # cena produktu w operacji
ilosc = 0                   # ilość produktów w operacji
konto = 0.00                # stan konta bankowego
kwota_b = 0.00              # kwota operacji bankowej
marker_k = 1                # znacznik czy kontynuować działanie programu
nowa_ilosc = 0              # pomocnicza zmienna do zmiany stanów magazynowych
nr = 0                      # numer listowanej operacji
nr_do = 0                   # numer końcowy operacji
nr_od = 0                   # numer początkowy operacji
opis_b = str()              # opis operacji bankowej
rejestr_b = []              # wykaz operacji bankowych
rejestr_m = []              # wykaz operacji magazynowych
stan = 0                    # stan towarów w magazynie
towary = set()              # wykaz identyfikatorów towarów
towar_id = []               # identyfikator towaru
wartosc = 0.00              # wartość produktów w operacji
zapasy = {}                 # stany towarów w magazynie
zapas_co = str()            # identyfikator towaru przy listingu z magazynu
zapas_ile = 0               # ilość towarów przylistingu z magazynu
zestawienie = str()         # znacznik uruchomienia listingu z konta bankowego
while marker_k == 1:
    print("Wybierz rodzaj operacji:")
    print("Z=Zakup, S=Sprzedaż, L=saLdo, K=Konto, M=Magazyn, P=Przegląd, O=kOniec")
    akcja = input()
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
            print("Podaj opis operacji bankowej")
            opis_b = input()
            zapis_b = (kwota_b, opis_b)
            konto += kwota_b
            rejestr_b.append(zapis_b)
            continue
# Operacje zakupu:
        if akcja == "Z":
            print("Podaj nazwę towaru:")
            towar_id = input()
            print("Podaj ilość towarów:")
            ilosc = int(input())
            if ilosc < 0:
                print("Błąd - ilość mniejsza niż 1, wprowadź operację ponownie!")
                continue
            print("Podaj cenę towaru w zł:")
            cena = int(input())
            if cena < 0:
                print("Błąd - ujemna cena, wprowadź operację ponownie!")
                continue
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
            print("Podaj ilość towaru:")
            ilosc = int(input())
            if ilosc <=0:
                print("Błąd - ujemna lub zerowa ilość towarów, wprowadź operację ponownie!")
                continue
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
        if akcja == "K":
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
                continue
# Stany magazynowe:
        if akcja == "M":
            print("Stan towarów w magazynie:")
            for elem in zapasy:
                zapas_co = elem
                zapas_ile = zapasy[zapas_co]
                print("{}    {}".format(zapas_co, zapas_ile))
            continue
# Przegląd operacji handlowych:
        if akcja == "P":
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
            continue