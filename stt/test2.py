import datetime
import os
import json
#создает файлы JSON если их нет
def create_json():
    file_path = 'datacontrol.json'
    file_path_2 = 'holidays.json'
    file_path_3 = 'datalog.json'
    # Проверка наличия файла datacontrol.json
    if not os.path.isfile(file_path):
        # Создание нового файла
        data = {}
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print('Файл datacontrol.json создан')
    else:
        print('Файл datacontrol.json уже существует')

    # Проверка наличия файла holidays.json
    if not os.path.isfile(file_path_2):
        # Создание нового файла
        data = {}
        with open(file_path_2, 'w') as file:
            json.dump(data, file, indent=4)
        print('Файл holidays.json создан')
    else:
        print('Файл holidays.json уже существует')

        # Проверка наличия файла datalog.json
    if not os.path.isfile(file_path_3):
        # Создание нового файла
        data = {}
        with open(file_path_3, 'w') as file:
            json.dump(data, file, indent=4)
        print('Файл datalog.json создан')
    else:
        print('Файл datalog.json уже существует')

create_json()


# Получаем текущую дату и время
def date_time_now():
    now = datetime.datetime.now()
    # Форматируем текущую дату и время в требуемый формат
    formatted_time = now.strftime("%Y-%m-%d %A %H:%M")
    return(formatted_time)

def date_now():
    now = datetime.datetime.now()
    # Форматируем текущую дату и время в требуемый формат
    formatted_time = now.strftime("%Y-%m-%d")
    return(formatted_time)

#определяет день недели
def day_week_chek():
    now = datetime.datetime.now()
    # Форматируем текущую дату и время в требуемый формат
    formatted_time = now.strftime("%A")
    return(formatted_time)


#Запись нового объекта в datacontrol.json
def write_date_control(new_obj):
    # Чтение содержимого файла JSON
    with open('datacontrol.json', 'r') as file:
        data = json.load(file)
    # Присвоение новому ключу new_obj значения new_obj
    data[new_obj['name_obj']] = new_obj
    # Запись обновлённых данных в файл JSON
    with open('datacontrol.json', 'w') as file:
        json.dump(data, file, indent=4)

#Запись нового объекта в datalog.json
def write_datalog(new_obj):
    # Чтение содержимого файла JSON
    with open('datalog.json', 'r') as file:
        data = json.load(file)
    # Присвоение новому ключу new_obj значения new_obj
    data[new_obj['name_obj']] = new_obj
    # Запись обновлённых данных в файл JSON
    with open('datalog.json', 'w') as file:
        json.dump(data, file, indent=4)


def write_datalog_part_2():
    # Прочитайте содержимое JSON-файла в словарь
    with open('datalog.json', 'r') as file:
        data = json.load(file)

    # Обратитесь к объекту "1-save number" в словаре
    save_number = data['1-save number']

    # Добавьте новые пары ключ-значение в объект
    save_number['end_time'] = '2023-08-12 Saturday 23:40'
    save_number['total_time'] = -1218
    save_number['factor_point'] = 1
    save_number['points_left_to_get'] = 2
    save_number['points_given'] = -122

    # Запишите обновленный словарь обратно в JSON-файл
    with open('datalog.json', 'w') as file:
        json.dump(data, file)





#получение последнего номера записи в datalog.json
def number_assignment():
    # Чтение данных из файла JSON
    with open("datalog.json", "r") as file:
        data = json.load(file)

    if data:
        # Поиск максимального значения save_number
        save_number_check = max(obj['save_number'] for obj in data.values())
    else:
        # Обработка случая, когда data пустой
        save_number_check = 0  # Установите значение по умолчанию или обработайте ситуацию соответствующим образом

    return save_number_check

#записывает в файл интервалы каникул
def holidays_write_json(start_date, stop_date):
    # Чтение содержимого файла JSON
    with open('holidays.json', 'r') as file:
        data = json.load(file)
    # Присвоение новому ключу new_obj значения new_obj
    data['holidays '+str(start_date) + ' - ' + str(stop_date)] = {'start_date_holidays': str(start_date), 'stop_date_holidays': str(stop_date), 'save_number': 0}
    # Запись обновлённых данных в файл JSON
    with open('holidays.json', 'w') as file:
        json.dump(data, file, indent=4)

# holidays_write_json('nohgfnon', '11')

def calculate_time_difference(start_time, end_time):
    start_datetime = datetime.datetime.strptime(start_time, "%Y-%m-%d %A %H:%M")
    end_datetime = datetime.datetime.strptime(end_time, "%Y-%m-%d %A %H:%M")
    time_difference = end_datetime - start_datetime
    total_minutes = int(time_difference.total_seconds() / 60)
    return total_minutes

# Определяет количество необходимых points в день
# def points_to_day():
#     return points

#part1
name_obj = str(number_assignment()) + '-save number ' + str(date_time_now())
save_number = number_assignment()
week = 1
date = date_now()
day_week = day_week_chek()
start_time = date_time_now()

#part2
end_time = '2023-08-12 Saturday 23:40'
total_time = calculate_time_difference(start_time, end_time)
factor_point = 1
points_left_to_get = 2 # прибавляется на исполнение сегодня в зависимости от дня
points_given = round(total_time // 10 * factor_point)



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
           "points_given": points_given}

write_datalog(new_obj)
# write_data_to_json(new_obj)



def created_obj_date_control():
    date_w =date_now()
    day_w = day_week_chek()
    dt = "jops"
    point =100
    new_obj_date_control = {"name_obj": date_w,
                            "date": date_w,
                            "day_week": day_w,
                            "day_type": dt,
                            "set_point": point}

    write_date_control(new_obj_date_control)


created_obj_date_control()