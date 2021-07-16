# Inicjacja:
import funkcje_ogolne
baza_kasowa = funkcje_ogolne.baza_kasowa
baza_magazynowa = funkcje_ogolne.baza_magazynowa
baza_handlowa = funkcje_ogolne.baza_handlowa
lista_akcji = []

# Funkcje:

def saldo_konta():
    saldo = 0
    for linia in baza_kasowa:
        kwota = linia[0]
        saldo += kwota
    saldo = str(saldo)
    info = "Końcowe saldo konta wynosi: "+saldo+"."
    wynik = open("data_export/saldo.txt", "w", encoding="utf-8")
    wynik.write(info)
    wynik.close()

def stany_magazynowe():
    naglowek = "Stan towarów w magazynie:\n"
    wynik = open("data_export/magazyn.txt", "w", encoding="utf-8")
    wynik.write(naglowek)
    for towar in baza_magazynowa:
        nazwa = towar
        stan = str(baza_magazynowa[nazwa])
        pozycja = towar +":   " + stan + "\n"
        wynik.write(pozycja)
    wynik.close()

def przeglad_akcji(nr_od, nr_do):
    for linia in baza_kasowa:
        lista_akcji.append(linia)
    for linia in baza_handlowa:
        lista_akcji.append(linia)
    nr_od = int(nr_od) - 1
    nr_do = int(nr_do)
    nr = nr_od
    wynik = open("data_export/akcje.txt", "w", encoding="utf-8")
    for linia in lista_akcji[nr_od:nr_do]:
        nr += 1
        numer = str(nr)
        akcja = str(linia)
        pozycja = "Nr " + numer + ":   " + akcja + "\n"
        wynik.write(pozycja)
    wynik.close()


    # for linia in lista_akcji:
    #     zapis1 = str(linia[0])
    #     zapis2 = str(linia[1])
    #     if linia[2]:
    #         zapis3 = str(linia[2])
    #     zapis = zapis1 + "   " + zapis2 + "   " + zapis3 + "\n"
    #     print(zapis)