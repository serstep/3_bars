import json
import math
import sys


#Расстояние между двумя точками на сфере расчитывается по формуле гаверсинусов
#Формула некорректно считает расстояние между точками антиподами.
#В данной задаче вероятность того, что точки окажутся антиподами небольшая,
#поэтому проблему можно опустить. Расстояние считается в метрах.
def get_sphere_distance(longitude1, latitude1, longitude2, latitude2):
    earth_radius = 6372795

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
    try:
        bars_list = list()
        with open(filepath) as file:
            bars_list = json.loads(file.read())
        return bars_list
    except:
        return None


def get_biggest_bar(data):
    return max(data, key=lambda b: b['SeatsCount'], default=None)


def get_smallest_bar(data):
    return min(data, key=lambda b: b['SeatsCount'], default=None)


def get_closest_bar(data, longitude, latitude):
    return min(data, key=lambda bar: get_sphere_distance(float(bar["Longitude_WGS84"]),\
     float(bar["Latitude_WGS84"]), longitude, latitude), default=None)

def check_coordinate_input(longitude, latitude):
    if latitude < -90 or latitude > 90 or longitude < -180 or longitude > 180:
        raise("Coordinate range mismatch")


#Возвращает строку с искомыми барами
def get_string_bars(bars_list, user_longitude, user_latitude):
    biggest_bar = get_biggest_bar(bars_list)
    smallest_bar = get_smallest_bar(bars_list)
    closest_bar = get_closest_bar(bars_list, user_longitude, user_latitude)

    result = ""
    if biggest_bar is None or smallest_bar is None or closest_bar is None:
        result = "Ошибка в поиске баров"
    else:
        result = "Наибольший бар: {} Количество мест: {}\nНаименьший бар: {} Количество мест: {}\nБлижайший бар: {} \nУдачной попойки!"\
        .format(biggest_bar["Name"], biggest_bar["SeatsCount"], smallest_bar["Name"], smallest_bar["SeatsCount"], closest_bar["Name"])
    return result


if __name__ == '__main__':

    bars_list = load_data(sys.argv[1])
    if bars_list is None:
        print("Ошибка чтения")
        exit()

    user_latitude = 0
    user_longitude = 0
    
    try:
        user_latitude = float(input("Введите координату широты от -90 до +90 градусов"))
        user_longitude = float(input("Введите координату долготы от -180 до +180 градусов"))
        check_coordinate_input(user_longitude, user_latitude)
    except:
        print("Неправильно указаны координаты")
        exit()

    print(get_string_bars(bars_list, user_longitude, user_latitude))

    
    
