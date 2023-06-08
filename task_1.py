import re
import csv


def get_data():

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    for i in range(1, 4):
        file_obj = open(f'info_{i}.txt')
        data = file_obj.read()

        os_prod_list.append(" ".join((re.compile(
            r'Изготовитель системы:\s*\S*\s*\S*').findall(data)[0].split()[2:])))

        os_name_list.append(re.compile(
            r'Microsoft Windows\s\S*').findall(data)[0])

        os_code_list.append(re.compile(
            r'Код продукта:\s*\S*').findall(data)[0].split()[2])

        os_type_list.append(re.compile(
            r'Тип системы:\s*\S*').findall(data)[0].split()[2])

    headers = ['Изготовитель системы',
               'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(headers)

    for i in range(0, 3):
        row_data = []
        row_data.append(os_prod_list[i])
        row_data.append(os_name_list[i])
        row_data.append(os_code_list[i])
        row_data.append(os_type_list[i])
        main_data.append(row_data)

    return main_data


def write_to_csv(out_file):

    main_data = get_data()
    with open(out_file, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in main_data:
            writer.writerow(row)


write_to_csv('csv_file.csv')
