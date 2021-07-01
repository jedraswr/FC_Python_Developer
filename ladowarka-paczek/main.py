# Program wylicza sposób rozmieszczenia elementów o różnych wagomiarach w paczkach do 20 kg
# Założenia stałe: max waga paczki, min i max limity wagi elementów
GLWPA=20
DLWEL=1
GLWEL=10
# Początkowe stany liczby elementów, liczby i wagi paczek
NREL=1
NRPA=1
WPA=0
LPA=0
MAXWPA=0
MINWPA=0
MAXNRPA=0
MINNRPA=0
SUMWPA=0
# Pobranie założeń i wyliczenia
print("Podaj liczbę elementów:")
LE=int(input())
while NREL<=LE:
    print("Podaj wagę elementu {} (1-10 kg):".format(NREL))
    WEL=float(input())
# Sprawdzanie poprawności podanej wagi elementu
    if WEL>GLWEL or (WEL<DLWEL and WEL!=0):
        print("Waga spoza zakresu - powtórz!")
# Przerwanie wprowadzania elementów
    elif WEL==0:
        print("Przerwano wprowadzanie elementów.")
# - jeśli kolejna paczka została rozpoczęta
        if WPA!=0:
            LPA=NRPA
            if MINWPA==0 or WPA<MINWPA:
                MINWPA=WPA
                MINNRPA=NRPA
            if MAXWPA==0 or WPA>MAXWPA:
                MAXWPA=WPA
                MAXNRPA=NRPA
# - jeśli kolejna paczka nie została rozpoczęta
        elif NREL==1:
            LPA=0
            NRPA=0
        else:
            LPA-=1
        break
    else:
        NWPA=WPA+WEL
        SUMWPA+=WEL
# Jeśli limit cieżaru paczki nie zostanie przekroczony
        if NWPA<GLWPA:
            WPA+=WEL
# - i jeśli to jest ostatni element
            if NREL==LE:
                if WPA<MINWPA or MINWPA==0:
                    MINWPA=WPA
                    MINNRPA=NRPA
                if WPA>MAXWPA:
                    MAXWPA=WPA
                    MAXNRPA=NRPA
                LPA=NRPA
            NREL+=1
# Jeśli limit ciężaru paczki zostanie przekroczony
        elif NWPA>GLWPA:
# - i jeśli nie jest to ostatni element
            if NREL!=LE:
                if WPA<MINWPA or MINWPA==0:
                    MINWPA=WPA
                    MINNRPA=NRPA
                if WPA>MAXWPA or MAXWPA==0:
                    MAXWPA=WPA
                    MAXNRPA=NRPA
                WPA=WEL
                NRPA+=1
                NREL+=1
# - i jeśli jest to ostatni element
            else:
                if WPA<MINWPA or MINWPA==0:
                    MINWPA=WPA
                    MINNRPA=NRPA
                if WPA>MAXWPA or MAXWPA==0:
                    MAXWPA=WPA
                    MAXNRPA=NRPA
                NRPA+=1
                LPA=NRPA
                if WEL<MINWPA or MINWPA==0:
                    MINWPA=WEL
                    MINNRPA=NRPA
                if WEL>MAXWPA:
                    MAXWPA=WEL
                    MAXNRPA=NRPA
                NREL+=1
# Jeśli ciężar paczki zostanie zrównany z limitem
        else:
            WPA+=WEL
            if WPA<MINWPA or MINWPA==0:
                MINWPA=WPA
                MINNRPA=NRPA
            if WPA>MAXWPA:
                MAXWPA=WPA
                MAXNRPA=NRPA
            WPA=0
            NREL+=1
            NRPA+=1
# - i jeśli był to ostatni element
            if (NREL-1)==LE:
                LPA=NRPA-1
            else:
                LPA=NRPA
print("*** PODSUMOWANIE ***")
print("Liczba wysłanych paczek: {}.".format(LPA))
print("Waga wysłanych paczek: {} kg.".format(SUMWPA))
print("Suma \"pustych\" kilogramów: {}.".format((NRPA*20)-SUMWPA))
print("Pierwsza najbardziej załadowana paczka miała nr {}: {} kg."\
      .format(MAXNRPA, MAXWPA))
print("Pierwsza najmniej załadowana paczka miała nr {}: {} kg."\
      .format(MINNRPA, MINWPA))
