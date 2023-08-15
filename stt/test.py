import datetime
import time

# Получаем текущую дату и время
def data_time_now():
    now = datetime.datetime.now()
    # Форматируем текущую дату и время в требуемый формат
    formatted_time = now.strftime("%Y-%m-%d %A %H:%M")
    return(formatted_time)


# Вычисляем разницу между двумя значениями времени
def timer_time(start_time, stop_time):
        # Преобразуем значения времени в объекты datetime
    time_obj_1 = datetime.datetime.strptime(start_time, "%Y-%m-%d %A %H:%M")
    time_obj_2 = datetime.datetime.strptime(stop_time, "%Y-%m-%d %A %H:%M")
    # Вычисляем разницу между двумя значениями времени
    time_difference = time_obj_2 - time_obj_1
    # Получаем разницу в часах и минутах
    hours = time_difference.seconds // 3600
    minutes = (time_difference.seconds // 60) % 60
    print(f"Разница между {start_time} и {stop_time} составляет {hours} часов и {minutes} минут.")
    return time_difference





start_time = data_time_now()
time.sleep(65)
stop_time = data_time_now()
print('Time difference =')
print(timer_time(start_time, stop_time))

