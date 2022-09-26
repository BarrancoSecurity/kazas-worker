from concurrent.futures import ThreadPoolExecutor
import bs4 as bs
import requests
import math
from datetime import date

from datetime import datetime as dt
from halo import Halo
import time
import requests
import concurrent.futures


url = "http://localhost:1337/v2/kazas"


def laraIndex(item):
    req = requests.post(url, json=item)
    print(req.text)


class Encuentra24DoInterface:
    def __init__(self, url, max_items, items_per_page, config, usd_conversion_rate):
        self.url = url
        self.max_items = max_items
        self.items_per_page = items_per_page
        self.config = config
        self.usd_conversion_rate = usd_conversion_rate

    # Find all items on each page, based on max_items provided
    def read_items_by_page(self):
        print("Called")
        max_pages = math.floor(self.max_items / self.items_per_page)
        current_page = 1
        parsed_items = 0

        # Buy
        url1 = "https://www.encuentra24.com/dominican-en/real-estate-for-sale-houses-homes/santo-domingo.{}?q=f_currency.USD"
        url2 = "https://www.encuentra24.com/dominican-en/real-estate-for-sale-apartments-condos/santo-domingo"

        # Rent
        url3 = "https://www.encuentra24.com/dominican-en/real-estate-for-rent-apartments/santo-domingo.2"

        while current_page <= max_pages:
            source = requests.get(
                url="https://www.encuentra24.com/dominican-en/real-estate-for-sale-apartments-condos/santo-domingo.{}".format(
                    current_page
                )
            )

            soup = bs.BeautifulSoup(source.text, "html.parser")

            items = soup.find("div", {"class": "ann-subcat-listing"})

            articles = items.find_all("article", {"class": "ann-box-teaser"})

            for item in articles:
                a = item.find("div", {"class": "ann-box-details"})
                url = a.find("a", {"class": "ann-box-title"})
                url_parsed = str(url).split("href=")[1].split('"')[1]

                parsed_items += 1
                self.load_item_data(self.url, url_parsed, parsed_items)

                print(
                    "\r"
                    + "[Encuentra24 - DO]: "
                    + str(round(parsed_items / self.max_items * 100, 1))
                    + "% complete"
                    + " ({}/{}) items captured.".format(parsed_items, self.max_items),
                    end="",
                )

                # with open('./scans/scan-{}.txt'.format(date.today()), "w") as scan:
                #     scan.write("{}".format(parsed_items))
                #     scan.close()

                if parsed_items == self.max_items:
                    print("max")
                    break
            current_page += 1

    # Captures data for a specific entry/item with provided url
    def load_item_data(self, url, path, count):
        item_url = "{}{}".format(url, path)
        source = requests.get(url=item_url)

        soup = bs.BeautifulSoup(source.text, "html.parser")
        ad_info = soup.find_all("div", {"class": "ad-info"})
        ad_details = soup.find_all("div", {"class": "ad-details"})

        

        mt2 = "0"
        sector = "0"
        precio = "0"
        habitaciones = "0"
        banos = "0"
        parqueos = "0"
        nombre_agente = "0"
        numero_agente = "0"

        try:
            sector = (
                str(ad_info[0].find_all("li")[2].find_all("span")[1])
                .split(">")[1]
                .split("</")[0]
            )
            precio = (
                str(ad_info[0].find_all("li")[3].find_all("span")[1])
                .split(">")[1]
                .split("</")[0]
            )
            habitaciones = (
                str(ad_details[0].find_all("li")[0])
                .split('info-value">')[1]
                .split("</span>")[0]
            )
            banos = (
                str(ad_details[0].find_all("li")[1])
                .split('info-value">')[1]
                .split("</span>")[0]
            )
            parqueos = (
                str(ad_details[0].find_all("li")[2])
                .split('info-value">')[1]
                .split("</span>")[0]
            )
            mt2 = (
                str(ad_details[0].find_all("li")[3])
                .split('info-value">')[1]
                .split("</span>")[0]
            )
        except IndexError:
            pass

        item = {
            "eventType": "index_item",
            "available_timestamp": str(date.today()),
            "id": path,
            "url": item_url,
            "module": "encuentra24-do",
            "mt2": mt2,
            "sector": sector,
            "precio": precio,
            "habitaciones": habitaciones,
            "banos": banos,
            "parqueos": parqueos,
            "nombre_agente": nombre_agente,
            "numero_agente": numero_agente,
            "type": "buy",
            "extras": [{"parent": "Comodidades", "fields": [{"name": "Piscina"}]}],
        }

        laraIndex(item)
