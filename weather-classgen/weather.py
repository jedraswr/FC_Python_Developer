# Importy i inicjacje:
import json
import sys
import requests as requests
import csv
import datetime
import time
klucz_api = sys.argv[1]
lista_prognoz = {}

# Ustalanie dat:
#   - poszukiwanie daty dla prognozy:
dzisiaj = datetime.date.today()
data_dzisiaj = time.mktime(dzisiaj.timetuple())
czy_data = len(sys.argv[::])
if czy_data == 3:
    data = sys.argv[2]
    data_zadana = datetime.datetime.strptime(data, "%Y-%m-%d")
else:
    data_zadana = dzisiaj + datetime.timedelta(days=1)
data_zadana = time.mktime(data_zadana.timetuple())  # data oczekiwanej prognozy
#   - sprawdzanie poprawności horyzontu prognozy:
ile_dni = int((data_zadana - data_dzisiaj) / (24 * 60 * 60))
if ile_dni > 15 or ile_dni < 0:                     # okres prognoz = dziś + 15 dni
    print("Nie wiem - długość prognozy to od 0 do 15 dni do przodu.")
    exit()

# Gra w klasy:


class KlasaPrognozy:                # samo słowo "prognozy" jest tu często odmieniane
    def __init__(self, klucz_api, data_zadana, lista_prognoz):
        self.klucz_api = klucz_api
        self.data_zadana = data_zadana
        self.lista_prognoz = lista_prognoz

    def wyszukaj_prognoze(self):
        for key, value in self.lista_prognoz.items():
            if float(key) == self.data_zadana:
                print(value)
                exit()


obiekt_kp = KlasaPrognozy(klucz_api, data_zadana, lista_prognoz)

# Szukanie prognozy w pliku cache:

def przepisz_z_cache_do_klasy():
    def przeglad_cache():
        with open("plik_cache.csv", "r", encoding="utf-8", newline="") as pc:
            pcreader = csv.reader(pc)
            for line in pcreader:
                yield line[0], line[1]
    przeglad_cache()
    wynik = przeglad_cache()
    for zapis in wynik:
        lista_prognoz[zapis[0]] = zapis[1]


# Tworzenie pliku cache:

def tworz_cache():
    czysc = open("plik_cache.csv", "w")             # czyszczenie cache
    czysc.write("")
    czysc.close()
    prognoza_pelna = open("prognoza.json", "r", encoding="utf-8")
    prognoza_reader = prognoza_pelna.read()
    prognoza_pelna.close()
    prognoza_pelna = json.loads(prognoza_reader)
    prognoza_lista = prognoza_pelna['list']
    for element in prognoza_lista:
        data_prognozy = element['dt']
        data_prognozy = datetime.date.fromtimestamp(data_prognozy)
        data_prognozy = time.mktime(data_prognozy.timetuple())
        tresc_prognozy = element['weather'][0]['main']
        if tresc_prognozy == 'Rain' or tresc_prognozy == 'Snow':
            tresc_prognozy = "Będzie padać"
        else:
            tresc_prognozy = "Nie będzie padać"
        prognoza_dnia = data_prognozy, tresc_prognozy
        with open("plik_cache.csv", "a", encoding="utf-8", newline="") as pc:
            zapiszpc = csv.writer(pc)
            zapiszpc.writerow(prognoza_dnia)
        continue

# Obsluga API:

def importuj_z_api():
    url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"
    querystring = {"q":"warsaw,pl","lat":"35","lon":"139","cnt":"16","units":"metric or imperial"}
    headers = {
        'x-rapidapi-key': obiekt_kp.klucz_api,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    with open("prognoza.json", "w", encoding="utf-8") as file:
        json.dump(response.json(), file)

# Procedura wykonania programu:
przepisz_z_cache_do_klasy()
obiekt_kp.wyszukaj_prognoze()   # odnalezienie prognozy kończy program
tworz_cache()
przepisz_z_cache_do_klasy()
obiekt_kp.wyszukaj_prognoze()
importuj_z_api()               # tylko gdy nie odnajdzie prognozy i nie wyłączy się
tworz_cache()
przepisz_z_cache_do_klasy()
obiekt_kp.wyszukaj_prognoze()
