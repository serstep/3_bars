import json
import math
import sys


#Расстояние между двумя точками на сфере расчитывается по формуле гаверсинусов
#Формула некорректно считает расстояние между точками антиподами.
#В данной задаче вероятность того, что точки окажутся антиподами небольшая,
#поэтому проблему можно опустить. Расстояние считается в метрах.
def get_sphere_distance(longitude1, latitude1, longitude2, latitude2):
    earth_radius = 6372795
    half_equator_length = 20037848

    latitude1 *= math.pi / 180
    latitude2 *= math.pi / 180
    longitude1 *= math.pi / 180
    longitude2 *= math.pi / 180

    longitude_haversin = pow(math.sin((longitude2 - longitude1) / 2), 2)
    latitude_haversin = pow(math.sin((latitude2 - latitude1) / 2), 2)

    angle_answer = 2 * math.asin(math.sqrt(latitude_haversin + \
        math.cos(latitude1) * math.cos(latitude2) * longitude_haversin))
    return angle_answer * earth_radius


def load_data(filepath):
    bars_list = list()
    with open(filepath) as file:
        bars_list = json.loads(file.read())
    return bars_list


def get_biggest_bar(data):
    return max(data, key=lambda b: b['SeatsCount'], default=None)


def get_smallest_bar(data):
    return min(data, key=lambda b: b['SeatsCount'], default=None)


def get_closest_bar(data, longitude, latitude):
    return min(data, key=lambda bar: get_sphere_distance(float(bar["Longitude_WGS84"]),\
     float(bar["Latitude_WGS84"]), longitude, latitude), default=None)


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Укажите путь к файлу с json записями в качестве единственного параметра")
        exit()

    bars_list = list()
    filepath = sys.argv[1]

    try:
        bars_list = load_data(filepath)
    except:
        print("Ошибка чтения" ,filepath)
        exit()


    biggest_bar = get_biggest_bar(bars_list)
    smallest_bar = get_smallest_bar(bars_list)

    if biggest_bar is None:
        print("Ошибка поиска наибольшего бара")
        exit()
    if smallest_bar is None:
        print("Ошибка поиска наименьшего бара")
        exit()


    print("Наибольший бар:" ,biggest_bar["Name"], "Количество мест:", biggest_bar["SeatsCount"])
    print("Наименьший бар:", smallest_bar["Name"], "Количество мест:", smallest_bar["SeatsCount"])


    user_latitude = 0
    user_longitude = 0

    try:
        user_latitude = float(input("Введите координату широты от -90 до +90 градусов"))
        user_longitude = float(input("Введите координату долготы от -180 до +180 градусов"))
        if user_latitude < -90 or user_latitude > 90 or\
         user_longitude < -180 or user_longitude > 180:
            raise("Coordinate range mismatch")
    except:
        print("Неправильно указаны координаты")
        exit()

    closest_bar = get_closest_bar(bars_list, user_longitude, user_latitude)

    if closest_bar is None:
        print("Ошибка поиска ближайшего бара")
        exit()

    print("Ближайший бар:", closest_bar["Name"])
    print("Удачной попойки!")