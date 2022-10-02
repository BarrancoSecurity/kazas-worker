import requests
import bs4 as bs

added_urls = []




for i in range(0, 240):
    with open("./html/urbania-rent-page-{}.txt".format(i), "r") as page:
        content = page.read()
    
        soup = bs.BeautifulSoup(content, "html.parser")

        items = soup.find_all("div", {"class": "sc-1tt2vbg-3 kGTsiT"})

        for item in items:

            url = str(item).split("data-to-posting")[1].split("><div")[0].split("=")[1]
            if url in added_urls:
                print("Duplicated url")
            else:
                added_urls.append(url)
                with open("./urbania-pe-rent.txt", "a") as rentUrls:
                    rentUrls.writelines("{}, \n".format(url))
                    rentUrls.close()

        page.close()