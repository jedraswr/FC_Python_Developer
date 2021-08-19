# Importy i inicjacja zmiennych:
import json
import sys
import requests as requests
import csv
import datetime
import time
klucz_api = sys.argv[1]


# Praca wstępna z datami:
#   - poszukiwanie daty dla prognozy
dzisiaj = datetime.date.today()
data_dzisiaj = time.mktime(dzisiaj.timetuple())
czy_data = len(sys.argv[::])
if czy_data == 3:
    data = sys.argv[2]
    data_zadana = datetime.datetime.strptime(data, "%Y-%m-%d")
else:
    data_zadana = dzisiaj + datetime.timedelta(days=1)
data_zadana = time.mktime(data_zadana.timetuple())  # data oczekiwanej prognozy
#   - sprawdzanie granicznego horyzontu prognozy
ile_dni = int((data_zadana - data_dzisiaj) / (24 * 60 * 60))
if ile_dni > 15 or ile_dni < 0:                     # okres prognoz = dziś + 15 dni
    print("Nie wiem - długość prognozy to od 0 do 15 dni do przodu.")
    exit()

# Gra w klasy:


class ParametryPrognozy:
    def __init__(self, klucz_api, data_zadana):
        self.klucz_api = klucz_api
        self.data_zadana = data_zadana

pp = ParametryPrognozy(klucz_api, data_zadana)

# Szukanie prognozy w pliku cache:

def szukaj_prognozy():
    print("szukam")
    with open("plik_cache.csv", "r", encoding="utf-8", newline="") as pc:
        pcreader = csv.reader(pc)
        for line in pcreader:
            if float(line[0]) == float(pp.data_zadana): # 1630447200.0
                yield line[1]
                break
wynik = szukaj_prognozy()
for prognoza in wynik:
    if prognoza:                            # ochrona przed exit gdyby prognozy nie było (None, "")
        print(prognoza)
        exit()                              # kończy działanie z chwilą odnalezienia prognozy

# Tworzenie pliku cache:

def tworz_cache():
    print("tworze cache")
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
    print("import API")
    url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"
    querystring = {"q":"warsaw,pl","lat":"35","lon":"139","cnt":"16","units":"metric or imperial"}
    headers = {
        'x-rapidapi-key': pp.klucz_api,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    with open("prognoza.json", "w", encoding="utf-8") as file:
        json.dump(response.json(), file)

# Procedura:
szukaj_prognozy()           # odnalezienie prognozy wyłącza działalnie programu
tworz_cache()
szukaj_prognozy()
importuj_z_api()            # gdy nie odnajdzie prognozy i nie wyłączy się
tworz_cache()
szukaj_prognozy()

