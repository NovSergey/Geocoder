import requests

server = "http://search-maps.yandex.ru/v1/"
params = {
    "apikey": "b48a845a-28bc-476a-899d-35c8fb9eb555",
    "type": "biz",
    "lang": "ru_RU",
    "format": "json"
}

def find(organiz):
    params["text"] = organiz
    response = requests.get(server, params)
    if response:
        json_response = response.json()
        toponyms = json_response["features"]
        #for top in toponyms:
            #organiz = top["geometry"]["properties"]
            #toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
            #toponym_coodrinates = toponym["Point"]["pos"]
            #print(toponym_address, "имеет координаты:", toponym_coodrinates)
        return toponyms
    else:
        print("Ошибка выполнения запроса:")
        print(server, params)
        print("Http статус:", response.status_code, "(", response.reason, ")")

def convert(geoObject):
    toponym = geoObject["properties"]
    toponym = toponym["CompanyMetaData"]
    return toponym["address"]

def getLLFor(geoObject):
    point = geoObject["geometry"]
    point = point["coordinates"]
    point = f"{point[0]} {point[1]}"
    return point.replace(" ", ",")
