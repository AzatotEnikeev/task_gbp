
"""
# имеется текстовый файл file.csv, в котором разделитель полей с данными: | (верт. черта)
# пример ниже содержит небольшую часть этого файла(начальные 3 строки, включая строку заголовков полей)

lastname|name|patronymic|date_of_birth|id
Фамилия1|Имя1|Отчество1 |21.11.1998|312040348-3048
Фамилия2|Имя2|Отчество2 |11.01.1972|457865234-3431


# Задание
# 1. Реализовать сбор уникальных записей
# 2. Случается, что под одинаковым id присутствуют разные данные - собрать отдельно такие записи
"""

import csv

def get_unique_records(filename: str) -> dict:
    with open(filename, encoding="utf-8") as file:
        onstring = file.read().split("\n")[1:-1]
        record_dict = {}
        for item in onstring:
            key = item.split("|")[-1]
            value = item.split("|")[:-1]
            record_dict[key] = value
        return record_dict

def get_duplicate_records(file_name: str) -> dict:
    records_dict = {}
    with open(file_name, encoding="utf-8") as file:
        file_reader = csv.reader(file, delimiter="|")
        for count, elem in enumerate(file_reader):
            if count != 0:
                elem_id = elem[-1]
                if elem_id in records_dict:
                    if elem not in records_dict[elem_id]:
                        records_dict[elem_id].append(elem)
                else:
                    records_dict[elem_id] = [elem]
        return records_dict


if __name__ == "__main__":
    dict_unique_records = get_unique_records("test.txt")
    dict_duplicate_record = get_duplicate_records("test.txt")

    print("Уникальные записи:")
    for key, value in dict_unique_records.items():
        print('| '.join(str(num) for num in value), key, sep='|')

    print("Дубликаты:")
    list_duplicate = []
    for key, value in dict_duplicate_record.items():
        if len(value) > 1:
            for elem in value:
                print("|".join(elem))



