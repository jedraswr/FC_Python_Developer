Tak jak w założeniach, uruchamiamy weather.py, dodajemy klucz do API, i zadaną datę prognozy (jeśli brak - wybierze
jutrzejszą).
Posiadana prognoza zapisana jest w pliku prognoza.json. Po sprawdzeniu ewentualnego błędu w zadanej dacie prognozy
program tworzy roboczą bazę danych w której są tylko kluczowe elementy (data i pogoda), a następnie szuka wyniku.
Jeśli w bazie brak prognozy z zadanej daty, program zczytuje z API najnowszą prognozę, ponownie tworzy bazę roboczą,
i odczytuje wynik.
Na koniec program automatycznie tworzy plik requirements.txt.