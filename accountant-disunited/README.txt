Program inicjuje się przez wywołanie nazwy pliku głównego: konto.py, magazyn.py,
przeglad.py, saldo.py, sprzedaż.py, lub zakup.py, wraz z parametrem startowym <...>
określającym plik z danymi do zaimportowania: dane.txt. W przypadku opcji przeglad.py
trzeba też podać dwa dodatkowe parametry startowe <...>: numer_od i numer_do akcji
które mają być wybrane do przeglądu (można 1 i 999).

Funkcje zgrupowane w pliku funkcje_ogolne.py są wykorzystywane są niezależnie od
wersji inicjacji programu, funkcje potrzebne tylko przy wersjach rozbudowanych
(konto.py,magazyn.py, i przeglad.py) zgrupowane są w pliku funkcje_dodatkowe.py.

Podobnie jak w pierwotnej wersji, opcje saldo.py, zakup.py, i sprzedaż.py wykonują
identyczne funkcje - pobierają dane, sprawdzają ich poprawność (ujemne saldo konta,
brak dostatecznej ilości towarów, lub błędnie wskazany towar którego nie było),
i podają listę wprowadzonych danych w pliku log.txt.

Opcja konto.py zwraca dodatkowo saldo konta bankowego w pliku konto.txt
Opcja magazyn.py zwraca dodatkowo stany magazynowe towarów w pliku magazyn.txt.
Opcja przeglad.py zwraca dodatkowo wybraną listę przeprowadzonych akcji bankowych
i handlowych (numery od - do) w pliku akcje.txt.