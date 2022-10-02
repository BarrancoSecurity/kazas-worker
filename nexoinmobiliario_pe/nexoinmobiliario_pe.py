import requests
import bs4 as bs
from datetime import date

with open("./html/nexoinmobiliario-casas-buy.txt", "r") as data:
    content = data.read()

    soup = bs.BeautifulSoup(content, "html.parser")
    items = soup.find_all("article", {"class": "article_dkp"})

    urls = []
    duplicate_urls = 0
    loaded_urls = 0

    for item in items:
        url = item.find("a")['href']
        loaded_urls += 1
        print("[Nexoinmobiliario]: Loaded {}/{} urls.".format(loaded_urls, len(items)))
        if url in urls:
            duplicate_urls += 1
            print("Duplicate url #{}".format(duplicate_urls))
        else:
            urls.append(url)

            with open("./logs/scans/nexoinmobiliario-casas-buy-{}.txt".format(date.today()), "a") as log:
                log.write("\"{}\", \n".format(url))
                log.close()

    data.close()




