import requests

server = "http://geocode-maps.yandex.ru/1.x/"
params = {
    "apikey": "ef7b9ab9-d96b-45b2-aab6-51fdb0d80171",
    "format": "json",
    "results": "100"
}

def find(toponym):
    params["geocode"] = toponym
    response = requests.get(server, params)
    if response:
        json_response = response.json()
        toponyms = json_response["response"]["GeoObjectCollection"]["featureMember"]
        for geoObject in toponyms:
            toponym = geoObject["GeoObject"]
            toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
            toponym_coodrinates = toponym["Point"]["pos"]
            print(toponym_address, "имеет координаты:", toponym_coodrinates)
        return toponyms
    else:
        print("Ошибка выполнения запроса:")
        print(server, params)
        print("Http статус:", response.status_code, "(", response.reason, ")")

def convert(geoObject):
    toponym = geoObject["GeoObject"]
    return toponym["metaDataProperty"]["GeocoderMetaData"]["text"]

def getLLFor(geoObject):
    print(geoObject)
    point = geoObject["GeoObject"]["Point"]["pos"]
    return point.replace(" ", ",")