# Rozliczanie spłat kredytu metodą annuitetową na 24 miesiące
# Zmienne do wprowadzenia
print("*"*70)
print("HARMONOGRAM SPŁATY KREDYTU HIPOTECZNEGO PRZEZ 24 MIESIĄCE")
print("Podaj kwotę kredytu:")
KK=float(input())
print("Podaj stopę odsetkową (%):")
SR=float(input())/100
# Przeliczenie stopy rocznej na efektywną stopę miesięczną
SM=(SR/12)*(1+(SR/12)**24)
# Wyliczenie płatności miesięcznej
PC=(KK*(SR/12)*(1+(SR/12))**24)/(((1+(SR/12))**24-1))
print("*"*70)
print(" ")
# Ustalenie i edycja wyników miesięcznych
DP=KK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 01: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 02: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 03: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 04: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 05: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 06: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 07: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 08: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 09: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 10: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 11: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 12: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 13: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 14: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 15: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 16: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 17: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 18: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 19: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 20: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 21: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 22: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 23: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
DP=DK
PO=DP*SM
PK=PC-PO
DK=DP-PK
print("""Miesiąc 24: spłata {C} -kaptał {K} -odsetki {O} dług {D}
""".format(C=round(PC,2), K=round(PK,2), O=round(PO,2), D=round(DK,2)))
RS=PC*24
RK=KK-DK
RO=RS-RK
RZ=DK
print("""Razem: spłata {RS} -kapitał {RK} -odsetki {RO} zaokrąglenia {RZ}
""".format(RS=round(RS,2), RK=round(RK,2), RO=round(RO,2), RZ=round(RZ,2)))