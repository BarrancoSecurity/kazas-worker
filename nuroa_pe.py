import bs4 as bs
import requests
import math
from datetime import date

from datetime import datetime as dt
from halo import Halo
import time
import requests

from multiprocessing import Pool


# BUY: https://www.laencontre.com.pe/venta/t-departamentos/lima-departamento/list/p_2
# RENT: https://www.laencontre.com.pe/alquiler/t-departamentos/lima-departamento/list

urls_list = [
    "https://www.nuroa.pe/venta/departamento-lima?page=1",
    "https://www.nuroa.pe/venta/departamento-lima?page=2",
    "https://www.nuroa.pe/venta/departamento-lima?page=3",
    "https://www.nuroa.pe/venta/departamento-lima?page=4",
    "https://www.nuroa.pe/venta/departamento-lima?page=5",
    "https://www.nuroa.pe/venta/departamento-lima?page=6",
    "https://www.nuroa.pe/venta/departamento-lima?page=7",
    "https://www.nuroa.pe/venta/departamento-lima?page=8",
    "https://www.nuroa.pe/venta/departamento-lima?page=9",
    "https://www.nuroa.pe/venta/departamento-lima?page=10",
    "https://www.nuroa.pe/venta/departamento-lima?page=11",
    "https://www.nuroa.pe/venta/departamento-lima?page=12",
    "https://www.nuroa.pe/venta/departamento-lima?page=13",
    "https://www.nuroa.pe/venta/departamento-lima?page=14",
    "https://www.nuroa.pe/venta/departamento-lima?page=15",
    "https://www.nuroa.pe/venta/departamento-lima?page=16",
    "https://www.nuroa.pe/venta/departamento-lima?page=17",
    "https://www.nuroa.pe/venta/departamento-lima?page=18",
    "https://www.nuroa.pe/venta/departamento-lima?page=19",
    "https://www.nuroa.pe/venta/departamento-lima?page=20",
    "https://www.nuroa.pe/venta/departamento-lima?page=21",
    "https://www.nuroa.pe/venta/departamento-lima?page=22",
    "https://www.nuroa.pe/venta/departamento-lima?page=23",
    "https://www.nuroa.pe/venta/departamento-lima?page=24",
    "https://www.nuroa.pe/venta/departamento-lima?page=25",
    "https://www.nuroa.pe/venta/departamento-lima?page=26",
    "https://www.nuroa.pe/venta/departamento-lima?page=27",
    "https://www.nuroa.pe/venta/departamento-lima?page=28",
    "https://www.nuroa.pe/venta/departamento-lima?page=29",
    "https://www.nuroa.pe/venta/departamento-lima?page=30",
    "https://www.nuroa.pe/venta/departamento-lima?page=31",
    "https://www.nuroa.pe/venta/departamento-lima?page=32",
    "https://www.nuroa.pe/venta/departamento-lima?page=33",
    "https://www.nuroa.pe/venta/departamento-lima?page=34",
    "https://www.nuroa.pe/venta/departamento-lima?page=35",
    "https://www.nuroa.pe/venta/departamento-lima?page=36",
    "https://www.nuroa.pe/venta/departamento-lima?page=37",
    "https://www.nuroa.pe/venta/departamento-lima?page=38",
    "https://www.nuroa.pe/venta/departamento-lima?page=39",
    "https://www.nuroa.pe/venta/departamento-lima?page=40",
    "https://www.nuroa.pe/venta/departamento-lima?page=41",
    "https://www.nuroa.pe/venta/departamento-lima?page=42",
    "https://www.nuroa.pe/venta/departamento-lima?page=43",
    "https://www.nuroa.pe/venta/departamento-lima?page=44",
    "https://www.nuroa.pe/venta/departamento-lima?page=45",
    "https://www.nuroa.pe/venta/departamento-lima?page=46",
    "https://www.nuroa.pe/venta/departamento-lima?page=47",
    "https://www.nuroa.pe/venta/departamento-lima?page=48",
    "https://www.nuroa.pe/venta/departamento-lima?page=49",
    "https://www.nuroa.pe/venta/departamento-lima?page=50",
    "https://www.nuroa.pe/venta/departamento-lima?page=51",
    "https://www.nuroa.pe/venta/departamento-lima?page=52",
    "https://www.nuroa.pe/venta/departamento-lima?page=53",
    "https://www.nuroa.pe/venta/departamento-lima?page=54",
    "https://www.nuroa.pe/venta/departamento-lima?page=55",
    "https://www.nuroa.pe/venta/departamento-lima?page=56",
    "https://www.nuroa.pe/venta/departamento-lima?page=57",
    "https://www.nuroa.pe/venta/departamento-lima?page=58",
    "https://www.nuroa.pe/venta/departamento-lima?page=59",
    "https://www.nuroa.pe/venta/departamento-lima?page=60",
    "https://www.nuroa.pe/venta/departamento-lima?page=61",
    "https://www.nuroa.pe/venta/departamento-lima?page=62",
    "https://www.nuroa.pe/venta/departamento-lima?page=63",
    "https://www.nuroa.pe/venta/departamento-lima?page=64",
    "https://www.nuroa.pe/venta/departamento-lima?page=65",
    "https://www.nuroa.pe/venta/departamento-lima?page=66",
    "https://www.nuroa.pe/venta/departamento-lima?page=67",
    "https://www.nuroa.pe/venta/departamento-lima?page=68",
    "https://www.nuroa.pe/venta/departamento-lima?page=69",
    "https://www.nuroa.pe/venta/departamento-lima?page=70",
    "https://www.nuroa.pe/venta/departamento-lima?page=71",
    "https://www.nuroa.pe/venta/departamento-lima?page=72",
    "https://www.nuroa.pe/venta/departamento-lima?page=73",
    "https://www.nuroa.pe/venta/departamento-lima?page=74",
    "https://www.nuroa.pe/venta/departamento-lima?page=75",
    "https://www.nuroa.pe/venta/departamento-lima?page=76",
    "https://www.nuroa.pe/venta/departamento-lima?page=77",
    "https://www.nuroa.pe/venta/departamento-lima?page=78",
    "https://www.nuroa.pe/venta/departamento-lima?page=79",
    "https://www.nuroa.pe/venta/departamento-lima?page=80",
    "https://www.nuroa.pe/venta/departamento-lima?page=81",
    "https://www.nuroa.pe/venta/departamento-lima?page=82",
    "https://www.nuroa.pe/venta/departamento-lima?page=83",
    "https://www.nuroa.pe/venta/departamento-lima?page=84",
    "https://www.nuroa.pe/venta/departamento-lima?page=85",
    "https://www.nuroa.pe/venta/departamento-lima?page=86",
    "https://www.nuroa.pe/venta/departamento-lima?page=87",
    "https://www.nuroa.pe/venta/departamento-lima?page=88",
    "https://www.nuroa.pe/venta/departamento-lima?page=89",
    "https://www.nuroa.pe/venta/departamento-lima?page=90",
    "https://www.nuroa.pe/venta/departamento-lima?page=91",
    "https://www.nuroa.pe/venta/departamento-lima?page=92",
    "https://www.nuroa.pe/venta/departamento-lima?page=93",
    "https://www.nuroa.pe/venta/departamento-lima?page=94",
    "https://www.nuroa.pe/venta/departamento-lima?page=95",
    "https://www.nuroa.pe/venta/departamento-lima?page=96",
    "https://www.nuroa.pe/venta/departamento-lima?page=97",
    "https://www.nuroa.pe/venta/departamento-lima?page=98",
    "https://www.nuroa.pe/venta/departamento-lima?page=99",
    "https://www.nuroa.pe/venta/departamento-lima?page=100",
]


url = "http://localhost:1337/v2/kazas"


def laraIndex(item):
    req = requests.post(url, json=item)
    print(req.text)


max_items = 13000
urls = []

# Captures data for a specific page with provided url
def load_urls(pageUrl):

    print("Fetching items...")

    source = requests.get(
        url=pageUrl,
        allow_redirects=True,
        headers={"User-Agent": "PostmanRuntime/7.28.4"},
    )

    soup = bs.BeautifulSoup(source.text, "html.parser")

    items = soup.find_all("a", {"class": "nu_blue_links"})


    for item in items:
        url = item["href"]
        if url != "https://www.lifullconnect.com/aviso-legal/" and url != "https://www.lifullconnect.com/global-privacy-policy-region6/" and url != "https://www.lifullconnect.com/aviso-legal/" and url != "https://www.nuroa.pe/venta/departamento-lima" and url != "https://www.nuroa.pe/venta/":
            with open("./scan-{}-nuroa-pe.txt".format(date.today()), "a") as scan:
                scan.writelines('"{}", \n'.format(str(url)))
                scan.close()




# Captures data for a specific entry/item with provided url
def load_item_data(item_url):
    print("loading {}".format(item_url))
    source = requests.get(
        url=item_url,
        allow_redirects=True,
        headers={"User-Agent": "PostmanRuntime/7.28.4"},
    )

    soup = bs.BeautifulSoup(source.text, "html.parser")

    price = soup.find("div", {"class": "price"})



# load_item_data("https://www.laencontre.com.pe/inmueble/446192")

    mt2 = "none"
    sector = "none"
    precio = "none"
    habitaciones = "none"
    banos = "none"
    parqueos = "none"
    nombre_agente = "none"
    numero_agente = "latest"

    try:
        sector = soup.find("span", {"class": "location_info"}).get_text()
    except (IndexError, AttributeError):
        pass

    try:
        precio = price.find("h2").get_text()
    except (IndexError, AttributeError):
        pass

    try:
        habitaciones = soup.find("li", {"class": "bedrooms"}).get_text().split(" ")[0]
    except (IndexError, AttributeError):
        pass

    try:
        banos = soup.find("li", {"class": "bathrooms"}).get_text().split(" ")[0]
    except (IndexError, AttributeError):
        pass

    # try:
    #     parqueos = (
    #         soup.find("div", {"class": "rh_property__meta prop_garages"})
    #         .find("span", {"class": "figure"})
    #         .get_text()
    #     )
    # except (IndexError, AttributeError):
    #     pass

    try:
        mt2 = soup.find("li", {"class": "dimensions"}).get_text()
    except (IndexError, AttributeError):
        pass

    item = {
        "eventType": "index_item",
        "available_timestamp": str(date.today()),
        "id": item_url,
        "url": item_url,
        "module": "laencontre-pe",
        "mt2": mt2.strip(),
        "sector": sector.strip(),
        "precio": precio.strip(),
        "habitaciones": habitaciones.strip(),
        "banos": banos.strip(),
        "parqueos": parqueos.strip(),
        "nombre_agente": nombre_agente.strip(),
        "numero_agente": numero_agente.strip(),
        "type": "rent",
        "extras": [{"parent": "Comodidades", "fields": [{"name": "Piscina"}]}],
    }

    laraIndex(item)

    # with open("./log-{}-laencontre-pe.txt".format(date.today()), "a") as scan:
    #     scan.writelines('"{}", \n'.format(str(item_url)))
    #     scan.close()


def get():

    p = Pool(10)
    p.map(load_urls, urls_list)
    p.terminate()
    p.join()


def data():
    d = Pool(100)
    d.map(load_item_data, urls)
    d.terminate()
    d.join()



get()
# data()
