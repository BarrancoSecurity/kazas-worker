urls = list()

for i in range(1,151):
    urls.append("https://www.citymax-gt.com/resultados-busqueda/page/{}/?status=venta".format(i))
print(urls)