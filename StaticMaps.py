import requests

import Geocoder
import PPO

server = "http://static-maps.yandex.ru/1.x/"
params = {
    "spn": "0.002,0.002",
    "l": "map"
}

def downloadImageSucsess(geoObject, check):
    if check == True:
        ll = Geocoder.getLLFor(geoObject)
    else:
        ll = PPO.getLLFor(geoObject)
    params["ll"] = ll
    response = requests.get(server, params)
    if not response:
        print("Ошибка выполнения запроса:")
        print(server, params)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        return False

    map_file = "images/map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return True