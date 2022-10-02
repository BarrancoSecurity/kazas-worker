import bs4 as bs
from datetime import date
import requests

url = "https://lara.barrancosecurity.me/v2/kazas"


def laraIndex(item):
    req = requests.post(url, json=item)
    print(req.text)

for i in range(0, 88):
    print("Querying item {}".format(i))
    with open("./items_buy_html/urbania-buy-item-{}.txt".format(i), "r") as item:
        content = item.read()

        soup = bs.BeautifulSoup(content, "html.parser")

        data = soup.find("div", {"class": "nf-container"})

        try:
            labels = data.find_all("div", {"class": "label"})

            mt2 = "none"
            sector = "none"
            precio = "none"
            habitaciones = "none"
            banos = "none"
            parqueos = "none"
            nombre_agente = "none"
            numero_agente = "latest"
            uid = soup.find("link", {"rel": "canonical"})["href"]

            params = {}

            price_container = soup.find("div", {"class": "price-items"})
            price = (
                str(price_container.find("span").get_text())
                .replace("\n", "")
                .replace("\t", "")
                .strip()
            )

            for label in labels:
                item_data = label.get_text().replace("\n", "").strip().replace(" ", "")
                if "Metros" in item_data:
                    params["mt2"] = item_data.split("Metros")[0]

                if "Dormitorios" in item_data:
                    params["habitaciones"] = item_data.split("Dormitorios")[0]

                if "Baños" in item_data:
                    params["banos"] = item_data.split("Baños")[0]

                if "Estacionamientos" in item_data:
                    params["parqueos"] = item_data.split("Estacionamientos")[0]
                

            try:
                mt2 = params["mt2"]
            except KeyError:
                mt2 = "none"

            try:
                sector_unparsed = soup.find(
                    "div", {"class": "development-title-container"}
                )
                sector_parsed = (
                    str(sector_unparsed.find("p", {"class": "subtitle"}).get_text())
                    .replace("\n", " ")
                    .replace("\t", " ")
                )
                sector = " ".join(sector_parsed.split())
            except KeyError:
                sector = "none"

            try:
                precio = price
            except KeyError:
                precio = "none"

            try:
                habitaciones = params["habitaciones"]
            except KeyError:
                habitaciones = "none"

            try:
                banos = params["banos"]
            except KeyError:
                banos = "none"

            try:
                parqueos = params["parqueos"]
            except KeyError:
                parqueos = "none"

            param_value_getter = {
                "uid": uid,
                "mt2": mt2,
                "sector": sector,
                "precio": precio,
                "habitaciones": habitaciones,
                "banos": banos,
                "parqueos": parqueos,
                "type": "buy",
                "module": "urbania-pe",
                "eventType": "index_item",
                "available_timestamp": str(date.today()),
                "id": uid,
                "url": uid,
                "nombre_agente": nombre_agente.strip(),
                "numero_agente": numero_agente.strip(),
                "extras": [{"parent": "Comodidades", "fields": [{"name": "Piscina"}]}],
            }
            laraIndex(param_value_getter)
            with open("./logs/scans/urbania-buy-items-{}.txt".format(date.today()), "a") as writeItem:
                writeItem.write('"{}", \n'.format(param_value_getter))
                writeItem.close()
            

        except AttributeError:
            with open("./logs/errored/urbania-buy-errored-{}.txt".format(date.today()), "a") as errored:
                errored.write('"{}", \n'.format(i))

        item.close()
