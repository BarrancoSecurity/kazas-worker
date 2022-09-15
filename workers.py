from encuentra24_do import Encuentra24DoInterface
from encuentra24_gt import Encuentra24GtInterface
from concurrent.futures import ThreadPoolExecutor

from perftest import TestInterface

enabled_params = [
    {"identifier": "localizacion", "name": "localizacion", "enabled": "true"},
    {"identifier": "marca", "name": "marca", "enabled": "true"},
    {"identifier": "modelo", "name": "modelo", "enabled": "true"},
    {"identifier": "fecha_publicacion", "name": "fecha_publicacion", "enabled": "true"},
    {"identifier": "precio", "name": "precio", "enabled": "true"},
    {"identifier": "year", "name": "year", "enabled": "true"},
    {"identifier": "km", "name": "km", "enabled": "true"},
    {"identifier": "transmision", "name": "transmision", "enabled": "true"},
    {"identifier": "combustible", "name": "combustible", "enabled": "true"},
    {"identifier": "vendedor", "name": "vendedor", "enabled": "true"},
    {"identifier": "phone", "name": "phone", "enabled": "true"},
    {"identifier": "uid", "name": "uid", "enabled": "true"},
    {"identifier": "financiamiento", "name": "financiamiento", "enabled": "true"},
]


# def scanner(module):  
#     print("started") 
#     workers = {
#         # "encuentra24-gt": Encuentra24GtInterface(
#         #     "https://www.encuentra24.com/", 1543, 15, enabled_params, 55
#         # ).read_items_by_page(),
#          "encuentra24-do": Encuentra24DoInterface(
#             "https://www.encuentra24.com/", 563, 15, enabled_params, 55
#         ).read_items_by_page()
#     }

#     workers[module]


TestInterface(
            "https://www.encuentra24.com/", 931, 15, enabled_params, 55
        ).read_items_by_page()
# scanner("encuentra24-do")





