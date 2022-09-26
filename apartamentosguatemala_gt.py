import bs4 as bs
import requests
import math
from datetime import date

from datetime import datetime as dt
from halo import Halo
import time
import requests

from multiprocessing import Pool


# apartamentos-en-alquiler
# venta

urls_list = [
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/1",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/2",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/3",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/4",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/5",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/6",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/7",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/8",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/9",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/10",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/11",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/12",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/13",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/14",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/15",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/16",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/17",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/18",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/19",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/20",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/21",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/22",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/23",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/24",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/25",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/26",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/27",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/28",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/29",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/30",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/31",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/32",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/33",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/34",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/35",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/36",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/37",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/38",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/39",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/40",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/41",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/42",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/43",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/44",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/45",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/46",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/47",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/48",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/49",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/50",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/51",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/52",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/53",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/54",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/55",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/56",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/57",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/58",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/59",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/60",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/61",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/62",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/63",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/64",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/65",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/66",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/67",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/68",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/69",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/70",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/71",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/72",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/73",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/74",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/75",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/76",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/77",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/78",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/79",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/80",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/81",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/82",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/83",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/84",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/85",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/86",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/87",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/88",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/89",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/90",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/91",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/92",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/93",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/94",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/95",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/96",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/97",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/98",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/99",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/100",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/101",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/102",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/103",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/104",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/105",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/106",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/107",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/108",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/109",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/110",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/111",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/112",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/113",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/114",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/115",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/116",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/117",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/118",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/119",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/120",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/121",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/122",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/123",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/124",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/125",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/126",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/127",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/128",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/129",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/130",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/131",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/132",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/133",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/134",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/135",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/136",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/137",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/138",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/139",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/140",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/141",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/142",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/143",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/144",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/145",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/146",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/147",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/148",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/149",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/150",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/151",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/152",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/153",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/154",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/155",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/156",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/157",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/158",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/159",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/160",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/161",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/162",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/163",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/164",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/165",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/166",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/167",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/168",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/169",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/170",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/171",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/172",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/173",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/174",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/175",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/176",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/177",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/178",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/179",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/180",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/181",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/182",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/183",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/184",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/185",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/186",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/187",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/188",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/189",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/190",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/191",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/192",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/193",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/194",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/195",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/196",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/197",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/198",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/199",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/200",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/201",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/202",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/203",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/204",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/205",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/206",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/207",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/208",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/209",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/210",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/211",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/212",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/213",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/214",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/215",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/216",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/217",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/218",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/219",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/220",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/221",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/222",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/223",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/224",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/225",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/226",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/227",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/228",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/229",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/230",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/231",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/232",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/233",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/234",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/235",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/236",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/237",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/238",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/239",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/240",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/241",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/242",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/243",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/244",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/245",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/246",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/247",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/248",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/249",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/250",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/251",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/252",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/253",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/254",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/255",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/256",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/257",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/258",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/259",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/260",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/261",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/262",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/263",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/264",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/265",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/266",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/267",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/268",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/269",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/270",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/271",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/272",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/273",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/274",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/275",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/276",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/277",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/278",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/279",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/280",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/281",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/282",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/283",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/284",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/285",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/286",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/287",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/288",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/289",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/290",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/291",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/292",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/293",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/294",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/295",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/296",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/297",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/298",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/299",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/300",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/301",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/302",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/303",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/304",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/305",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/306",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/307",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/308",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/309",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/310",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/311",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/312",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/313",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/314",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/315",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/316",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/317",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/318",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/319",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/320",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/321",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/322",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/323",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/324",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/325",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/326",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/327",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/328",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/329",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/330",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/331",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/332",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/333",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/334",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/335",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/336",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/337",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/338",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/339",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/340",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/341",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/342",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/343",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/344",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/345",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/346",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/347",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/348",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/349",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/350",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/351",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/352",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/353",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/354",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/355",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/356",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/357",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/358",
    "https://apartamentosguatemala.com/apartamentos-en-venta/page/359",
]

url = "http://localhost:1337/v2/kazas"


def laraIndex(item):
    req = requests.post(url, json=item)
    print(req.text)


max_items = 3150
urls = []

#  Captures data for a specific page with provided url
def load_urls(pageUrl):

    print("Getting page: {} - Items: {}".format(pageUrl.split("page/")[1], len(urls)))
    print("------------------------------------------------------------------------")

    source = requests.get(
        url=pageUrl,
        allow_redirects=True,
        headers={"User-Agent": "PostmanRuntime/7.28.4"},
    )

    soup = bs.BeautifulSoup(source.text, "html.parser")

    items = soup.find("div", {"id": "listing_ajax_container"})

    data = items.find_all("div", {"class": "listing_wrapper"})

    for a in data:
        url = a.find("h4").find("a", href=True)['href']

        print(url)
        with open("./scan-{}-encuentra24-gt.txt".format(date.today()), "a") as scan:
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

    data = soup.find_all("div", {"class": "panel-body"})[1]
    details = data.find_all("div", {"class": "listing_detail"})

    metadata = soup.find_all("div", {"class": "panel-body"})[0]
    metadetails = metadata.find_all("div", {"class": "listing_detail"})

    param_index = {}
    for detail in details:
        param_index[str(detail).split("<strong>")[1].split("</strong>")[0]] = str(detail).split("</strong>")[1].split("</div>")[0].strip()

    metaparam_index = {}
    for detail in metadetails:
        metaparam_index[str(detail).split("<strong>")[1].split("</strong>")[0]] = str(detail).split("</strong>")[1].split("</div>")[0].strip()


    mt2 = "none"
    sector = "none"
    precio = "none"
    habitaciones = "none"
    banos = "none"
    parqueos = "none"
    nombre_agente = "none"
    numero_agente = "latest"


    try:
        sector = metaparam_index["Sector:"].split("tag\">")[1].split("</a>")[0].strip()
    except (IndexError, AttributeError, KeyError):
        pass

    try:
        precio = param_index["Precio:"].split("</span>")[1].split("<span")[0].strip()
    except (IndexError, AttributeError, KeyError):
        pass

    try:
        habitaciones = (
            param_index["Habitaciones:"]
        )
    except (IndexError, AttributeError, KeyError):
        pass

    try:
        banos = (
            param_index["Baños:"]
        )
    except (IndexError, AttributeError, KeyError):
        pass

    try:
        parqueos = (
           param_index["Estacionamientos:"]
        )
    except (IndexError, AttributeError, KeyError):
        pass

    try:
        mt2 = (
            param_index["Tamaño M2"]
        )
    except (IndexError, AttributeError, KeyError):
        pass


    item = {
        "eventType": "index_item",
        "available_timestamp": str(date.today()),
        "id": item_url,
        "url": item_url,
        "module": "apartamentosguatemala-gt",
        "mt2": mt2.strip(),
        "sector": sector.strip(),
        "precio": precio.strip(),
        "habitaciones": habitaciones.strip(),
        "banos": banos.strip(),
        "parqueos": parqueos.strip(),
        "nombre_agente": nombre_agente.strip(),
        "numero_agente": numero_agente.strip(),
        "type": "buy",
        "extras": [{"parent": "Comodidades", "fields": [{"name": "Piscina"}]}],
    }

    laraIndex(item)


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
