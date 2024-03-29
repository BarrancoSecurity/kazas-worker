
import bs4 as bs
import requests
import math
from datetime import date

from datetime import datetime as dt
from halo import Halo
import time
import requests

from multiprocessing import Pool


# departamentos-en-venta - offset 200
# inmuebles-en-alquiler - offset 150

urls_list = [
    "https://tuvivienda.pe/busqueda/inmuebles?slug=inmuebles-en-alquiler&offset=0&limit=25&",
    "https://tuvivienda.pe/busqueda/inmuebles?slug=inmuebles-en-alquiler&offset=25&limit=25&",
    "https://tuvivienda.pe/busqueda/inmuebles?slug=inmuebles-en-alquiler&offset=50&limit=25&",
    "https://tuvivienda.pe/busqueda/inmuebles?slug=inmuebles-en-alquiler&offset=75&limit=25&",
    "https://tuvivienda.pe/busqueda/inmuebles?slug=inmuebles-en-alquiler&offset=100&limit=25&",
    "https://tuvivienda.pe/busqueda/inmuebles?slug=inmuebles-en-alquiler&offset=125&limit=25&",
    "https://tuvivienda.pe/busqueda/inmuebles?slug=inmuebles-en-alquiler&offset=150&limit=25&",
]

url = "http://localhost:1337/v2/kazas"


def laraIndex(item):
    req = requests.post(url, json=item)
    print(req.text)


max_items = 13000
urls = [
    "https://tuvivienda.pe/se-alquila-amplio-terreno-en-parque-porcino-ventanilla-55064.html", 
"https://tuvivienda.pe/alquilo-dpto-callao-urb-colonial-cfaucett-2do-piso-casa-fparque-54827.html", 
"https://tuvivienda.pe/alquiler-de-moderno-dpto-triplex-miraflores-50659.html", 
"https://tuvivienda.pe/alquiler-de-local-primer-piso-en-lince-ideal-para-el-sector-salud-54734.html", 
"https://tuvivienda.pe/local-comercial-santa-ana-los-olivos-54548.html", 
"https://tuvivienda.pe/alquilo-departamento-palao-54547.html", 
"https://tuvivienda.pe/ocasion-departamento-sol-de-carabayllo-50563.html", 
"https://tuvivienda.pe/local-comercial-institucional-el-pinar-comas-52906.html", 
"https://tuvivienda.pe/alquiler-departamento-pueblo-libre-55437.html", 
"https://tuvivienda.pe/alquiler-departamento-los-olivos-55436.html", 
"https://tuvivienda.pe/alquiler-departamento-lince-55435.html", 
"https://tuvivienda.pe/alquiler-departamento-brena-55434.html", 
"https://tuvivienda.pe/alquiler-departamento-la-victoria-55433.html", 
"https://tuvivienda.pe/departamento-amoblado-hermosa-vista-al-mar-malecon-cisneros-55430.html", 
"https://tuvivienda.pe/se-alquila-local-comercial-1er-piso211m2-negociable-55422.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-jesus-maria-55413.html", 
"https://tuvivienda.pe/alquiler-de-departamento-santa-clara-55412.html", 
"https://tuvivienda.pe/alquiler-de-departamento-del-segundo-piso-55411.html", 
"https://tuvivienda.pe/alquiler-dpto-semiamoblado-5to-piso-huachipa-ate-55409.html", 
"https://tuvivienda.pe/alquilo-departamento-3-habitaciones-2-banos-en-condominio-55406.html", 
"https://tuvivienda.pe/alqiuiler-habitation-en-2-o-3-er-pisso-en-casa-residencial-55405.html", 
"https://tuvivienda.pe/alquiler-minidepartamento-surquillo-aramburu-55397.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-jesus-maria-55396.html", 
"https://tuvivienda.pe/departamento-en-buena-zona-55393.html", 
"https://tuvivienda.pe/local-huandoy-los-olivos-55380.html", 
"https://tuvivienda.pe/alquiler-departamento-jesus-maria-av-brasil-quinto-piso-73m2-salacomedor3dormitorio2banococinalavanderia-balcon-vista-calle-s200000-55372.html", 
"https://tuvivienda.pe/alquiler-departamento-san-borja-3-dormitorios-3-banos-cochera-55369.html", 
"https://tuvivienda.pe/alquilo-todo-inlcuido-bonito-departamento-01-dorm-full-aequipado-cterraza-propia-miraflores-55363.html", 
"https://tuvivienda.pe/apartamento-excelente-zona-turistica-en-miraflores-55348.html", 
"https://tuvivienda.pe/alquiler-de-local-comercial-en-san-isidro-51268.html", 
"https://tuvivienda.pe/alquiler-de-local-comercial-en-pueblo-libre-53787.html", 
"https://tuvivienda.pe/oficina-en-san-isidro-50407.html", 
"https://tuvivienda.pe/amplio-local-comercial-en-alquiler-en-zona-de-alto-transito-callao-53375.html", 
"https://tuvivienda.pe/depa-2-dorm-amoblado-cerca-al-malecon-en-miraflores-55170.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-surquillo-av-la-calera-55139.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-magdalena-parque-gonzalez-prada-55138.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-salamanca-av-los-quechuas-55136.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-pueblo-libre-parque-el-carmen-55134.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-los-olivos-av-las-palmeras-55133.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-surquillo-av-la-calera-55126.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-los-olivos-av-las-palmeras-55125.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-salamanca-av-los-quechuas-55124.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-san-miguel-av-los-patriotas-55102.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-san-luis-av-la-rosa-toro-55101.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-brena-avenida-28-de-julio-55100.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-cercado-de-lima-av-elvira-garcia-55099.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-san-martin-del-porres-av-jose-granda-55098.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-jesus-maria-av-estados-unidos-55097.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-salamanca-av-los-quechuas-55096.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-magdalena-av-juan-de-aliaga-55095.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-pueblo-libre-parque-el-carmen-55094.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-los-olivos-av-las-palmeras-55093.html", 
"https://tuvivienda.pe/no-busques-mas-y-alquila-tu-oficina-en-un-excelente-lugar-55076.html", 
"https://tuvivienda.pe/alquilo-dpto-frente-a-parque-120m2-3-dorm-1-estac-urb-aurora-miraflores-55574.html", 
"https://tuvivienda.pe/alquilo-dpto-flat-125m2-3-dorm-2-estac-2do-piso-urb-higuereta-surco-55573.html", 
"https://tuvivienda.pe/acogedor-departamento-amoblado-y-equipado-cerca-al-golf-miguel-dasso-el-olivar-55541.html", 
"https://tuvivienda.pe/alquilo-oficina-en-surquillo-55540.html", 
"https://tuvivienda.pe/alquiler-de-local-industrial-en-callao-55537.html", 
"https://tuvivienda.pe/alquiler-de-casa-familiar-primer-piso-independiente-los-olivos-55556.html", 
"https://tuvivienda.pe/alquiler-edificio-bien-ubicado-55554.html", 
"https://tuvivienda.pe/alquilo-mini-departamento-55553.html", 
"https://tuvivienda.pe/alquiler-departamento-3er-piso-zona-b-san-juan-de-miraflores-55536.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-villa-el-salvador-55530.html", 
"https://tuvivienda.pe/alquiler-de-departamento-duplex-en-chiclayo-55524.html", 
"https://tuvivienda.pe/propietario-alquila-dpto-c-2-dormitorios-55523.html", 
"https://tuvivienda.pe/alquiler-oficina-san-miguel-zona-comercialbancosaeropuertoaduana-55521.html", 
"https://tuvivienda.pe/alquiler-de-habitacion-55511.html", 
"https://tuvivienda.pe/alquilo-departamento-en-ate-55510.html", 
"https://tuvivienda.pe/55505.html", 
"https://tuvivienda.pe/hermoso-duplex-amoblado-en-higuereta-surco-55498.html", 
"https://tuvivienda.pe/departamento-41-mts-55479.html", 
"https://tuvivienda.pe/alquiler-de-habitacion-en-san-martin-de-porres-urb-palao-55477.html", 
"https://tuvivienda.pe/alquiler-de-terreno-en-cajamarca-55476.html", 
"https://tuvivienda.pe/alquiler-de-minidepa-55470.html", 
"https://tuvivienda.pe/alquiler-departamento-y-habitaciones-los-olivos-55463.html", 
"https://tuvivienda.pe/alquiler-hermoso-departamento-primer-piso-lince-55456.html", 
"https://tuvivienda.pe/alquiler-departamento-amoblado-barranco-us-65000-55454.html", 
"https://tuvivienda.pe/alquiler-minidepa-miraflores-55452.html", 
"https://tuvivienda.pe/alquilo-hermoso-departamento-amoblado-2h-1b-55444.html", 
"https://tuvivienda.pe/alquiler-departamento-la-molina-la-planicie-55441.html", 
"https://tuvivienda.pe/alquilo-departamento-amoblado-2-dorm-70m2-limite-lince-san-isidro-55440.html", 
"https://tuvivienda.pe/alquiler-departamento-san-miguel-55439.html", 
"https://tuvivienda.pe/alquiler-departamento-san-borja-55438.html", 
"https://tuvivienda.pe/ocasion-terreno-huachipa-55466.html", 
"https://tuvivienda.pe/alquiler-local-comercial-san-juan-de-lurigancho-55449.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-lince-av-cesar-vallejo-55520.html", 
"https://tuvivienda.pe/alquilo-departamento-en-san-martin-del-porres-av-jose-granda-55519.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-los-olivos-av-las-palmeras-55518.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-la-victoria-av-carlos-villaran-55486.html", 
"https://tuvivienda.pe/alquiler-de-departamento-pueblo-libre-parque-el-carmen-55485.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-jesus-maria-av-estados-unidos-55484.html", 
"https://tuvivienda.pe/se-alquila-local-frente-a-parque-en-urb-cipreses-55231.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-los-olivos-av-las-palmeras-55201.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-surquillo-av-la-calera-55200.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-salamanca-av-los-quechuas-55199.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-cercado-de-lima-av-elvira-garcia-55198.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-lince-av-cesar-vallejo-55190.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-brena-avenida-28-de-julio-55189.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-la-victoria-av-carlos-villaran-55188.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-salamanca-av-los-quechuas-55187.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-jesus-maria-av-estado-unidos-55186.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-pueblo-libre-parque-el-carmen-55185.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-san-martin-del-porres-av-jose-granda-55184.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-san-miguel-av-los-patriotas-55183.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-surquillo-av-la-calera-55182.html", 
"https://tuvivienda.pe/alquiler-de-departamento-en-los-olivos-av-las-palmeras-55181.html", 
"https://tuvivienda.pe/precioso-flat-2-dorm-cbalcon-super-distribuido-zona-de-la-dalmacia-miraflores-55175.html", 
"https://tuvivienda.pe/super-inversion-1-dorm-en-esquina-con-terraza-barranco-55173.html", 
"https://tuvivienda.pe/alquilo-comodo-departamento-en-buena-zona-55502.html", 
"https://tuvivienda.pe/alquiler-casa-chalet-cerca-a-pucp-aelu-etc-4-dormit-terrazas-cocheras-55425.html", 
"https://tuvivienda.pe/alquilo-local-comercial-en-san-juan-de-lurigancho-55404.html", 
"https://tuvivienda.pe/alquilo-local-comercial-de-2-pisos-en-villa-el-salvador-55403.html", 
"https://tuvivienda.pe/alquilo-comodo-departamento-amoblado-en-surquillo-bonito-55328.html", 
"https://tuvivienda.pe/alquilo-comodo-departamento-en-surquillo-zona-tranquila-55319.html", 
"https://tuvivienda.pe/alquiler-dpto-san-borja-55314.html", 
"https://tuvivienda.pe/moderna-oficina-implementada-inlcuye-dos-cocheras-en-buena-ubicacion-55308.html", 
"https://tuvivienda.pe/alquiler-de-lindo-departamento-en-san-isidro-55304.html", 
"https://tuvivienda.pe/ocasion-se-alquila-local-venta-pollo-fresco-al-costado-del-mall-aventura-plaza-de-bellavista-55288.html", 
"https://tuvivienda.pe/se-alquila-departamento-cruce-de-las-avenidas-arequipa-y-javier-prado-en-san-isidro-55268.html", 
"https://tuvivienda.pe/se-alquila-departamento-para-vivienda-local-comercial-u-oficina-en-cercado-de-lima-55247.html", 
"https://tuvivienda.pe/alquilo-inmenso-duplex-en-paseo-la-castellana-55246.html", 
"https://tuvivienda.pe/alquilo-departamento-2dopiso-playa-pulpos-km455aps-80m2-2dorms2banos-1300-55234.html", 
"https://tuvivienda.pe/alquilo-amplio-duplex-con-una-terraza-en-avenida-paseo-la-castellana-55224.html", 
"https://tuvivienda.pe/alquilo-acogedor-departamento-en-1er-piso-con-cochera-en-avenida-paseo-de-la-republica-miraflores-55208.html", 
"https://tuvivienda.pe/alquiler-departamento-los-robles-smp-55193.html", 
"https://tuvivienda.pe/surquillo-barrio-medico-se-alquila-departamento-amoblado-55154.html", 
"https://tuvivienda.pe/alquilo-maravilloso-y-lujoso-departamento-full-amoblado-en-av-navarrete-san-isidro-altos-ejecutivos-y-viajeros-55147.html", 
"https://tuvivienda.pe/alquilo-oficina-de-419-m2-centro-financiero-de-san-isidro-55137.html", 
"https://tuvivienda.pe/alquiler-oficina-en-centro-financiero-san-isidro-55135.html", 
"https://tuvivienda.pe/se-alquila-ambiente-para-oficina-deposito-o-almacen-en-surquillo-55090.html", 
"https://tuvivienda.pe/casa-de-campo-en-pachacamac-amoblada-55345.html", 
"https://tuvivienda.pe/alquilo-comodos-departamentos-en-cercado-de-lima-1er-y-3er-piso-55564.html", 
"https://tuvivienda.pe/alquiler-de-departamento-de-estreno-en-mayorazgo-55557.html", 
"https://tuvivienda.pe/alquiler-de-local-comercial-en-san-isidro-55489.html", 
"https://tuvivienda.pe/alquiler-departamento-en-comas-55394.html", 
"https://tuvivienda.pe/se-alquila-departamento-amplio-en-2do-piso-55332.html", 
"https://tuvivienda.pe/alquilo-lindo-dpto-en-condominio-miraflores-55303.html", 
"https://tuvivienda.pe/terreno-en-alquiler-en-parque-porcino-ventanilla-55566.html", 
"https://tuvivienda.pe/alquiler-de-dpto-duplex-amoblado-miraflores-55555.html", 
"https://tuvivienda.pe/lindo-departamento-totalmente-amoblado-con-linda-vista-frente-al-mar-y-a-parque-55513.html", 
"https://tuvivienda.pe/lince-alquiler-departamento-edificio-lux-limite-con-san-isidro-55493.html", 
"https://tuvivienda.pe/alquilo-local-en-av-conquistadores-san-isidro-55446.html", 
"https://tuvivienda.pe/alquilo-impecable-oficina-en-surco-55400.html", 
"https://tuvivienda.pe/se-alquila-departamento-amoblado-en-estreno-altura-cruce-avenidas-arequipa-y-javier-prado-en-san-isidro-55385.html", 
"https://tuvivienda.pe/alquiler-de-linda-casa-de-campo-en-pachacamac-55383.html", 
"https://tuvivienda.pe/alquile-local-de-venta-de-pollo-fresco-y-no-pague-por-6-meses-en-el-colonial-market-55382.html", 
"https://tuvivienda.pe/alquilo-casa-comercial-los-quechuas-55351.html", 
"https://tuvivienda.pe/alquilo-casa-oficina-administrativa-santa-anita-55349.html", 
"https://tuvivienda.pe/se-alquila-departamento-duplex-sin-amoblar-jesus-maria-cerca-a-la-universidad-pacifico-55296.html", 
"https://tuvivienda.pe/alquilo-departamentocterraza-surco-chuaroc-93m2-2dorms1cocheradeposito-800-55255.html", 
"https://tuvivienda.pe/alquilo-departamento-playa-pulpos-s1600-90m2-4dorms-2banos-km455antpansur-55235.html", 
"https://tuvivienda.pe/alquilo-duplex-con-cochera-en-barranco-limite-con-miraflores-55206.html", 
"https://tuvivienda.pe/alquilo-departamento-amoblado-55156.html", 
"https://tuvivienda.pe/alquiler-departamento-semi-amoblado-en-miraflores-a-2-cuadras-del-parque-kennedy-55128.html", 
"https://tuvivienda.pe/se-alquila-departamento-en-tercer-piso-en-surco-frente-a-universidad-ricardo-palma-55115.html", 
"https://tuvivienda.pe/en-san-isidro-alquilo-departamento-55108.html", 
"https://tuvivienda.pe/local-comercial-de-estreno-en-1-piso-puerta-a-calle-mini-market-veterinaria-bazar-salon-de-belleza-consultorio-medico-55083.html", 
"https://tuvivienda.pe/local-comercial-san-juan-de-lurigancho-188-m2-55562.html", 

]
# Captures data for a specific page with provided url
def load_urls(pageUrl):

    print("Fetching items...")

    source = requests.get(
        url=pageUrl,
        allow_redirects=True,
        headers={
            "User-Agent": "PostmanRuntime/7.28.4",
            "X-Requested-With": "XMLHttpRequest",
        },
    )

    soup = bs.BeautifulSoup(source.json()['content'], "html.parser")

    items = soup.find_all("section", {"class": "t-bus-item-des"})



    for item in items:
        url = item.find("a")['href']
        with open("./scan-{}-tuvivienda-pe.txt".format(date.today()), "a") as scan:
            scan.writelines('"{}", \n'.format(str(url)))
            scan.close()



# Captures data for a specific entry/item with provided url
def load_item_data(item_url):
    print("loading {}".format(item_url))
    source = requests.get(
        url=item_url,
        allow_redirects=True,
        headers={"User-Agent": "PostmanRuntime/7.28.4", "X-Requested-With": "XMLHttpRequest"},
    )

    soup = bs.BeautifulSoup(source.text, "html.parser")

    items = soup.find("ul", {"class": "my-0 t-det-car"})

    data = items.find_all("li")
    parsed_dataset = {}
    
    heading = soup.find("span", {"class": "t-det-p"})



    for item in data:
        try:
            param = str(item).split("<strong>")[1].split("</strong>")[0]
            value = str(item).split("<strong>")[0].split("<li>")[1]
            
            if param == "Precio en dólares:":
                parsed_dataset["precio"] = str(item).split("<strong>")[1].split("</strong>")[1].split("</li>")[0].strip()
            if param == "área construida":
                parsed_dataset["mt2"] = value
            if param == "baños":
                parsed_dataset["baños"] = value
            if param == "dormitorios":
                parsed_dataset["dormitorios"] = value
            if param == "estacionamientos":
                parsed_dataset["estacionamientos"] = value
       
        except IndexError:
            pass

    mt2 = "none"
    sector = "none"
    precio = "none"
    habitaciones = "none"
    banos = "none"
    parqueos = "none"
    nombre_agente = "none"
    numero_agente = "latest"

    try:
        sector = str(heading).split("</i>")[1].split("</span>")[0].strip().replace(" ", "").replace(",", ", ")
    except (IndexError, AttributeError, KeyError):
        pass

    try:
        precio = parsed_dataset['precio']
    except (IndexError, AttributeError, KeyError):
        pass

    try:
        habitaciones = parsed_dataset["dormitorios"]
    except (IndexError, AttributeError, KeyError):
        pass

    try:
        banos = parsed_dataset["baños"]
    except (IndexError, AttributeError, KeyError):
        pass

    try:
        parqueos = parsed_dataset["estacionamientos"]
    except (IndexError, AttributeError, KeyError):
        pass

    try:
        mt2 = parsed_dataset["mt2"]
    except (IndexError, AttributeError, KeyError):
        pass

    item = {
        "eventType": "index_item",
        "available_timestamp": str(date.today()),
        "id": item_url,
        "url": item_url,
        "module": "tuvivienda-pe",
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

    with open("./log-{}-tuvivienda-pe.txt".format(date.today()), "a") as scan:
        scan.writelines('"{}", \n'.format(str(item_url)))
        scan.close()


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


# get()
# data()
