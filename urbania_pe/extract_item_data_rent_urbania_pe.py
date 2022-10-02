import bs4 as bs
from datetime import date
import requests

url = "https://lara.barrancosecurity.me/v2/kazas"


def laraIndex(item):
    req = requests.post(url, json=item)
    print(req.text)


for i in range(0, 36):
    print("Querying item {}".format(i))
    with open("./items_rent_html/urbania-rent-item-{}.txt".format(i), "r") as item:
        content = item.read()

        soup = bs.BeautifulSoup(content, "html.parser")

        try:
            data = soup.find("ul", {"class": "section-icon-features"})

            labels = data.find_all("li", {"class": "icon-feature"})

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
            price_unparsed = (
                    str(price_container.find("span").get_text())
                    .replace("\n", "")
                    .replace("\t", "")
                    .strip()
                )

            if "USD" in price_unparsed:
                price =  (
                    str(price_container.find("span").get_text())
                    .replace("\n", "")
                    .replace("\t", "")
                    .strip()
                ).split("USD")[0]
            else:
                price =  (
                    str(price_container.find("span").get_text())
                    .replace("\n", "")
                    .replace("\t", "")
                    .strip()
                )

            for label in labels:
                item_data = (
                    str(label)
                    .split("</i>")[1]
                    .split("</li>")[0]
                    .strip()
                    .replace(" ", "")
                    .replace("\n", "")
                    .replace(" ", "")
                )
                parsed_data = " ".join(item_data.split())

                if "m²" in parsed_data:
                    params["mt2"] = parsed_data.split("m²")[0]

                if "Dormitorios" in parsed_data:
                    params["habitaciones"] = parsed_data.split("Dormitorios")[0]

                if "Baños" in parsed_data:
                    params["banos"] = parsed_data.split("Baños")[0]

                if "Estacionamientos" in parsed_data:
                    params["parqueos"] = parsed_data.split("Estacionamientos")[0]

            try:
                mt2 = params["mt2"]
            except KeyError:
                mt2 = "none"

            try:
                sector_unparsed = soup.find(
                    "h2", {"class": "title-location"}
                ).get_text()

                if "Ver en mapa" in str(sector_unparsed).replace("\n", "").strip():
                    sector = (
                        str(sector_unparsed)
                        .replace("\n", "")
                        .strip()
                        .split("Ver en mapa")[0]
                    )
                else:
                    sector = str(sector_unparsed).replace("\n", "").strip()
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
                "type": "rent",
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
            with open("./logs/scans/urbania-rent-items-{}.txt".format(date.today()), "a") as writeItem:
                writeItem.write('"{}", \n'.format(param_value_getter))
                writeItem.close()

        except AttributeError:
            with open(
                "./logs/errored/urbania-rent-errored-{}.txt".format(date.today()),
                "a",
            ) as errored:
                errored.write('"{}", \n'.format(i))

        item.close()
