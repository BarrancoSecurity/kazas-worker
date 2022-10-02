import requests
import bs4 as bs

added_urls = []

for i in range(0, 462):
    with open("./buy_html/adondevivir-buy-page-{}.txt".format(i), "r") as page:
        content = page.read()
    
        soup = bs.BeautifulSoup(content, "html.parser")

        items = soup.find_all("div", {"class": "sc-1tt2vbg-3 kGTsiT"})

        for item in items:
            url = "https://adondevivir.com{}.html".format(str(item).split("data-to-posting")[1].split(".html")[0].split("=\"")[1])
            if url in added_urls:
                print("Duplicated url")
            else:
                added_urls.append(url)
                with open("./adondevivir-pe-buy.txt", "a") as rentUrls:
                    rentUrls.writelines("\"{}\", \n".format(url))
                    rentUrls.close()

        page.close()