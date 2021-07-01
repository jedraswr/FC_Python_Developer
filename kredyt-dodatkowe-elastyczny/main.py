# Rozliczanie spłat kredytu metodą annuitetową na 24 miesiące
# Zmienne do wprowadzenia
print("*"*70)
print("HARMONOGRAM SPŁATY KREDYTU HIPOTECZNEGO")
print("Podaj kwotę kredytu:")
KK=float(input())
print("Podaj ilość lat spłaty:")
LS=int(input())
print("Podaj częstość spłat - M=miesięczna, K=kwartalna, R=roczna:")
CS=input()
if CS=='M':
    WS=12
elif CS=='K':
    WS=4
elif CS=='R':
    WS=1
else:
    print("Podano błędny parametr częstości spłat!")
LP=LS*WS
print("Podaj roczną stopę odsetkową banku (%):")
SR=float(input())/100
# Przeliczenie stopy rocznej na efektywną stopę miesięczną
SO=(1+SR)**(1/WS)-1
# Wyliczenie płatności miesięcznej
PC=(KK*(SR/WS)*(1+(SR/WS))**LP)/(((1+(SR/WS))**LP-1))
print("*"*70)
print(" ")
# Ustalenie paramentów początkowych
NP=1
SS=0
SC=0
SI=0
SK=0
# Wyliczanie i edycja wyników miesięcznych
for NP in range(1, LP+1, 1):
    DP=KK-SC
    PO=DP*SO
    PK=PC-PO
    SC+=PC
    SK+=PK
    SI+=PO
    DL=KK-SK
    print("Spłata {}: kwota {}, -kapitał {}, -odsetki {}, dług {}".\
          format(round(NP,0), round(PC,2), round(PK,2), round(PO,2), round(DL,2)))
RZ=KK-SK
print("Razem: spłata {}, -kapitał {}, -odsetki {}, zaokrąglenia {}".\
      format(round(SC,2), round(SK,2), round(SI,2), round(RZ,2)))
