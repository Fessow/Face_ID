import openpyxl
from Time_DB import time_to_minutes, calculate_time_attendance, sum_of_values
from pprint import pprint



# Открытие Excel файла
file_path = 'Daniel.xlsx'  # укажите путь к вашему файлу
wb = openpyxl.load_workbook(file_path)

# Открытие листа (если у вас несколько листов, укажите нужный лист)
sheet = wb.active  # по умолчанию будет активный лист

# Создание словаря для хранения данных
attendance_dict = {}

# Считываем данные с G6 до G35 и N6 до N35
for row in range(6, 36):  # С 6 по 35 включительно
    key = sheet[f'G{row}'].value  # Ячейка G6, G7, ..., G35
    value = sheet[f'N{row}'].value  # Ячейка N6, N7, ..., N35
    if key is not None:  # Если в ячейке G есть значение
        attendance_dict[key] = value

# Выводим полученный словарь
#print(attendance_dict)

attendance_dict_2 = {}
temporary_dict={}

for row in range(6, 36):  # С 6 по 35 включительно
    key = sheet[f'G{row}'].value  # Ячейка G6, G7, ..., G35
    value = sheet[f'T{row}'].value  # Ячейка N6, N7, ..., N35

    value_diff = value.split(' ')
    minutes_value_list = []

    if value_diff!=['-']:
        for i in value_diff:
            minutes_value_list.append(round(time_to_minutes(i), 2))


    if key is not None and minutes_value_list!=[]:  # Если в ячейке G есть значение
        temporary_dict[key] = minutes_value_list
        attendance_dict_2[key] = calculate_time_attendance(minutes_value_list)

#print(temporary_dict)
#print('skip')
pprint(attendance_dict_2)



target_count_days = len(attendance_dict_2)
target_count_hours = target_count_days * 8
target_count_minutes = target_count_hours * 60

in_fact_minutes = sum_of_values(attendance_dict_2)
in_fact_hours = in_fact_minutes / 60
in_fact_days = in_fact_hours / 8

print(f'Целевое посещение в минутах {target_count_minutes}')
print(f'Фактическое посещение в минутах {in_fact_minutes}')

percentage = round(( in_fact_minutes / target_count_minutes ) * 100,2)
print(f'По факту отработано за период {percentage}%')
