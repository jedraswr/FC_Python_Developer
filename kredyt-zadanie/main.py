# Obliczanie spłaty kredytu
# Wartości zmiennych
print("*"*60)
print("WYLICZENIA ZADŁUŻENIA Z TYTUŁU KREDYTU")
print("Podaj kwotę kredytu:")
KREDYT=float(input())
print("Podaj kwotę miesięcznej spłaty:")
SPLATA=float(input())
print("Podaj stopę narzutu banku (%):")
NARZUT=float(input())
# Wartości stałych zadanych wskaźników inflacji:
INF_0101=float(1.59282448436825)
INF_0102=-0.453509101198007
INF_0103=2.32467171712441
INF_0104=1.26125440724877
INF_0105=1.78252628571251
INF_0106=2.32938454145522
INF_0107=1.50222984223283
INF_0108=1.78252628571251
INF_0109=2.32884899407637
INF_0110=0.616921348207244
INF_0111=2.35229588637833
INF_0112=0.337779545187098
INF_0201=1.57703524727525
INF_0202=-0.292781442607648
INF_0203=2.48619659017508
INF_0204=0.267110317834564
INF_0205=1.41795267229799
INF_0206=1.05424326726375
INF_0207=1.4805201044812
INF_0208=1.57703524727525
INF_0209=-0.077420690314702
INF_0210=1.16573339872354
INF_0211=-0.404186717638335
INF_0212=1.49970852083123
# Wyliczenia i wyniki:
print("*"*60)
print(" ")
KP=KREDYT
KK=round(((1+(INF_0101+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Styczeń 01: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0102+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Luty 01: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0103+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Marzec 01: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0104+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Kwiecień 01: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0105+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Maj 01: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0106+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Czerwiec 01: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0107+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Lipiec 01: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0108+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Sierpień 01: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0109+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Wrzesień 01: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0110+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Październik 01: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0111+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Listopad 01: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0112+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Grudzień 01: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0201+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Styczeń 02: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0202+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Luty 02: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0203+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Marzec 02: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0204+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Kwiecień 02: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0205+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Maj 02: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0206+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Czerwiec 02: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0207+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Lipiec 02: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0208+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Sierpień 02: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0209+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Wrzesień 02: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0210+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Październik 02: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0211+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Listopad 02: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))
KP=KK
KK=round(((1+(INF_0212+NARZUT)/1200)*KP)-SPLATA,2)
KR=round(KP-KK,2)
print("""Grudzień 02: twoja pozostała kwota kredytu to {D} zł, 
to {R} zł mniej niż w poprzednim miesiącu.
""".format(D=KK,R=KR))

