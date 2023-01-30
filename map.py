import json
import requests
from geopy import distance
import folium
from flask import Flask


def read_map():
    with open('map_of_coffe.html') as file:
        return file.read()


def create_map(coordinates, cafe_and_coordinates_full):
    sorted_cafes = sorted(cafe_and_coordinates_full, key=find_nearest_cafes)[:5]
    map = folium.Map(location=coordinates)
    for cafe in sorted_cafes:
        tooltip = cafe["cafe"]
        first_place = cafe['lat'], cafe['lon']
        folium.Marker(
            first_place, popup=f'{cafe["distance"]}', tooltip=tooltip
        ).add_to(map)
    map.save("map_of_coffe.html")


def fetch_coordinates(apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": apikey,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json()['response']['GeoObjectCollection']['featureMember']
    if not found_places:
        return None
    most_relevant = found_places[0]
    coordinates = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return coordinates


def read_file():
    with open("coffee.json", "r", encoding="CP1251") as maps_file:
        file_contents = maps_file.read()
        a = json.loads(file_contents)
        cafe_and_coordinates = []
        x = 0
        for el in a:
            cafe_name = a[x]['Name']
            latitude = a[x]['Latitude_WGS84']
            longitude = a[x]['Longitude_WGS84']
            cafe = {'cafe': cafe_name for el in a}
            lat = {'lat': latitude for el in a}
            lon = {'lon': longitude for el in a}
            cafe_and_coordinates.append({**cafe, **lat, **lon})
            x += 1
        return cafe_and_coordinates


def get_full_list(cafe_and_coordinates, coordinates):
    cafe_and_coordinates_full = []
    for place in cafe_and_coordinates:
        point_b = place['lon'], place['lat']
        distances = (distance.distance(coordinates, point_b).km)
        distances_ = {'distance': distances}
        cafe_and_coordinates_full.append({**distances_, **place})
    return cafe_and_coordinates_full


def find_nearest_cafes(cafe_and_coordinates_full):
    return cafe_and_coordinates_full['distance']


def main():
    apikey = '103d5e3e-7687-426c-b485-60bbb516fb73'
    address = input('Введите свой адрес: ')
    cafe_and_coordinates = read_file()
    coordinates = fetch_coordinates(apikey, address)
    cafe_and_coordinates_full = get_full_list(cafe_and_coordinates, coordinates)
    create_map(coordinates, cafe_and_coordinates_full)

    app = Flask(__name__)
    app.add_url_rule('/', 'map', read_map)
    app.run('0.0.0.0')


if __name__ == '__main__':
    main()
