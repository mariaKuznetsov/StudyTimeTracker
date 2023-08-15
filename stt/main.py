import datetime
import time
import os
import json
#создает файл если нет
def create_json():
    file_path = 'datacontrol.json'
    # Проверка наличия файла
    if not os.path.isfile(file_path):
        # Создание нового файла
        data = {}
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print('Файл datacontrol.json создан')
    else:
        print('Файл datacontrol.json уже существует')

create_json()


def points_write_json(): #не работает
    # Чтение содержимого файла JSON
    with open('datacontrol.json', 'r') as file:
        data = json.load(file)
    # Присвоение новому ключу new_obj значения new_obj
    data['points'] = {'points_day': 100, 'points_given': 0, 'save_number': 0}
    # Запись обновлённых данных в файл JSON
    with open('datacontrol.json', 'w') as file:
        json.dump(data, file, indent=4)

# Получаем текущую дату и время
def date_time_now():
    now = datetime.datetime.now()
    # Форматируем текущую дату и время в требуемый формат
    formatted_time = now.strftime("%Y-%m-%d %A %H:%M")
    return(formatted_time)



#определяет день недели
def day_week_chek():
    date = date_time_now()
    date = datetime.datetime.strptime(date, "%Y-%m-%d %A %H:%M").strftime("%A")
    return date

#Запись нового объекта
def write_data_to_json(new_obj):
    # Чтение содержимого файла JSON
    with open('datacontrol.json', 'r') as file:
        data = json.load(file)
    # Присвоение новому ключу new_obj значения new_obj
    data[new_obj['name_obj']] = new_obj
    # Запись обновлённых данных в файл JSON
    with open('datacontrol.json', 'w') as file:
        json.dump(data, file, indent=4)

#получение номера записи
# def number_assignment():
#     # Чтение данных из файла JSON
#     with open("datacontrol.json", "r") as file:
#         data = json.load(file)
#     # Поиск максимального значения save_number
#     save_number_check = max([obj['save_number'] for obj in data.values()])
#     return save_number_check + 1

def number_assignment():
    # Чтение данных из файла JSON
    with open("datacontrol.json", "r") as file:
        data = json.load(file)

    if data:
        # Поиск максимального значения save_number
        save_number_check = max(obj['save_number'] for obj in data.values())
    else:
        # Обработка случая, когда data пустой
        save_number_check = 0  # Установите значение по умолчанию или обработайте ситуацию соответствующим образом

    return save_number_check + 1

#записывает в файл интервалы каникул
def holidays_write_json(start_date, stop_date):
    # Чтение содержимого файла JSON
    with open('datacontrol.json', 'r') as file:
        data = json.load(file)
    # Присвоение новому ключу new_obj значения new_obj
    data['holidays '+str(start_date)] = {'start_date_holidays': str(start_date), 'stop_date_holidays': str(stop_date), 'save_number': 0}
    # Запись обновлённых данных в файл JSON
    with open('datacontrol.json', 'w') as file:
        json.dump(data, file, indent=4)



def calculate_time_difference(start_time, end_time):
    start_datetime = datetime.datetime.strptime(start_time, "%Y-%m-%d %A %H:%M")
    end_datetime = datetime.datetime.strptime(end_time, "%Y-%m-%d %A %H:%M")
    time_difference = end_datetime - start_datetime
    total_minutes = int(time_difference.total_seconds() / 60)
    return total_minutes



name_obj = str(number_assignment()) + '-save number ' + str(date_time_now())
save_number = number_assignment()
week = 1
date = date_time_now()
day_week = day_week_chek()
start_time = date_time_now()
end_time = '2023-08-12 Saturday 23:40'
total_time = calculate_time_difference(start_time, end_time)
factor_point = 1
points_left_to_get = 2
points_given = round(total_time // 10 * factor_point)
holiday = False
points_week=100

print(name_obj)
print('день недели', day_week)
print('номер записи', save_number)
print(date)
print('total Minut', total_time)
print('points_given', points_given)


new_obj = {"name_obj": name_obj,
           "save_number": save_number,
           "week": week,
           "date": date,
           "day_week": day_week,
           "start_time": start_time,
           "end_time": end_time,
           "total_time": total_time,
           "factor_point": factor_point,
           "points_left_to_get": points_left_to_get,
           "points_given": points_given,
           "holiday": holiday}
write_data_to_json(new_obj)
