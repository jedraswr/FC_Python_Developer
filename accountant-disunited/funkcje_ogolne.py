#inicjacja:
baza_handlowa = []
baza_kasowa = []
baza_magazynowa = {}
sciezka = "data_import/"
opis = str()
wartosc = int()
operacja = ()
transakcja = ()

#funkcje:

def czyszczenie_logu():
    logi = open("data_export/log.txt", "w", encoding="utf-8")
    logi.write("")
    logi.close()

def wpis_do_logu(input):
    logi = open("data_export/log.txt", "a", encoding="utf-8")
    logi.write(input + "\n")
    logi.close()

def import_danych(plik):
    tresc_danych = open(sciezka+plik, "r", encoding="utf-8")
    zapisy = tresc_danych.readlines()
    for linia in zapisy:
        skladnik = linia.split(" ")
        if skladnik[0].isdigit() or (skladnik[0])[1:].isdigit():
            wartosc = int(skladnik[0])
            opis = skladnik[1]
            if "\n" in opis:
                opis = opis[0:-1]
            operacja = (wartosc, opis)
            baza_kasowa.append(operacja)
            wpis_do_logu(skladnik[0])
            wpis_do_logu(skladnik[1])
            continue
        else:
#     tresc_danych.close()
#
# def import_handlowy():
#     tresc_danych = open(dane_handlowe, "r", encoding="utf-8") #czytanie danych
#     zapisy = tresc_danych.readlines()
#     for linia in zapisy:                    #zapis handlowy
#         skladnik = linia.split(" ")
            towar = skladnik[0]
            ilosc = int(skladnik[1])
            cena = skladnik[2]
            if "\n" in cena:
                cena = cena[0:-1]
            cena = int(cena)
            transakcja = (towar, ilosc, cena)
            baza_handlowa.append(transakcja)
            if ilosc <0:                        #zapis kasowy
                opis = "sprzedaż_"+towar
            else:
                opis = "zakup_"+towar
            wartosc = -ilosc * cena
            operacja = (wartosc, opis)
            baza_kasowa.append(operacja)
            wpis_do_logu(skladnik[0])
            wpis_do_logu(skladnik[1])
            wpis_do_logu(skladnik[2])
    tresc_danych.close()

def test_kasowy():
    saldo = 0
    uwagi = 0
    for line in baza_kasowa:
        saldo += line[0]
        if saldo <0:
            print("Ujemne saldo konta bankowego po operacji {}!"\
                  .format(line))
            uwagi += 1
    print("Wykonano test ujemnego salda konta bankowego, liczba uwag: {}.\n"\
          .format(uwagi))

def test_handlowy():
    uwagi = 0
    for line in baza_handlowa:
        towar = line[0]
        ilosc = line[1]
        if ilosc > 0:
            if towar not in baza_magazynowa.keys():
                baza_magazynowa[towar] = ilosc
            else:
                stan_przed = baza_magazynowa.get(towar)
                baza_magazynowa[towar] = stan_przed + ilosc
        else:
            if towar not in baza_magazynowa.keys():
                print("Błąd w wyborze towaru dla sprzedaży {}"
                      .format(line))
                uwagi += 1
                stan_przed = 0
            else:
                stan_przed = baza_magazynowa.get(towar)
                if stan_przed < -ilosc:
                    print("Przekroczono dostępną ilość towaru dla sprzedaży {}."\
                          .format(line))
                    uwagi += 1
                baza_magazynowa[towar] = stan_przed + ilosc
    print("Wykonano test ujemnych stanów towarów w magazynie, liczba uwag: {}.\n"\
          .format(uwagi))