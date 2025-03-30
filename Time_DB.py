def time_to_minutes(time_str):
    # Разделяем строку по двоеточиям
    hours, minutes, seconds = map(int, time_str.split(":"))

    # Переводим время в минуты
    total_minutes = hours * 60 + minutes + seconds / 60

    return total_minutes


# Определим функцию для вычисления разницы во времени
def calculate_time_attendance(minutes_value):
    if len(minutes_value) < 2:
        return 0  # Или другое значение, если количество значений некорректно

    # Если два значения, просто вычитаем
    if len(minutes_value) == 2:
        return round(minutes_value[1] - minutes_value[0],2)

    # Если три значения, вычитаем первое от второго
    elif len(minutes_value) == 3:
        return round(minutes_value[2] - minutes_value[0])

    # Если четыре значения, складываем разницы
    elif len(minutes_value) == 4:
        return round((minutes_value[1] - minutes_value[0]) + (minutes_value[3] - minutes_value[2]))

    # Если значения не соответствуют ожидаемому количеству
    return None  # Или другое значение по необходимости


def sum_of_values(my_dict):

    # Суммируем все значения
    total_sum = sum(value for value in my_dict.values() if isinstance(value, (int, float)))

    return round(total_sum,2)








