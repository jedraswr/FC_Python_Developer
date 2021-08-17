# Importy i inicjacja zmiennych:
import sys
import requests as requests
import datetime
import os
import time
import json
baza_prognoz = {}       # robocza baza danych wybranych elementów prognoz
marker_importu = 0      # znacznik zapobiegający pętleniu się importu jeśli nie można odnaleźć prognozy

# Wczytywanie założeń:
klucz_api = sys.argv[1]
dzisiaj = datetime.date.today()
data_dzisiaj = time.mktime(dzisiaj.timetuple())
czy_data = len(sys.argv[::])
if czy_data == 3:
    data = sys.argv[2]
    data_zadana = datetime.datetime.strptime(data, "%Y-%m-%d")
else:
    data_zadana = dzisiaj + datetime.timedelta(days=1)
data_zadana = time.mktime(data_zadana.timetuple())  # data oczekiwanej prognozy

# Sprawdzanie granicznego horyzontu prognozy:
ile_dni = int((data_zadana - data_dzisiaj) / (24 * 60 * 60))
if ile_dni > 15 or ile_dni < 0:                     # okres prognoz = dziś + 15 dni
    print("Nie wiem - długość prognozy to od 0 do 16 dni do przodu.")
    exit()

# Obsluga API:

def import_z_api():
    if marker_importu == 0:
        url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"
        querystring = {"q":"warsaw,pl","lat":"35","lon":"139","cnt":"16","units":"metric or imperial"}
        headers = {
            'x-rapidapi-key': klucz_api,
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        with open("prognoza.json", "w", encoding="utf-8") as file:
            json.dump(response.json(), file)

# Tworzenie bazy prognoz z pliku json:
if not os.path.isfile("prognoza.json"):
    import_z_api()
    marker_importu = 1

def tworzenie_bazy():
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
        baza_prognoz[data_prognozy] = tresc_prognozy
        continue

tworzenie_bazy()

# Wyszukiwanie prognozy z posiadanych zasobów:

def wydruk_prognozy():
    if data_zadana in baza_prognoz:
        print(baza_prognoz[data_zadana])
        exit()
    elif marker_importu == 1:
        print("Nie wiem - nie znalazłem prognozy z tej daty")
        exit()
    else:
        import_z_api()

wydruk_prognozy()

# Wyszukiwanie prognozy ze zaktualizowanych zasobów:
tworzenie_bazy()
wydruk_prognozy()

