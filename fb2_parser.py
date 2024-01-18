from chardet.universaldetector import UniversalDetector  # Определим кодировку файла
import re  # Подключаем библиотеку для парсинга
import glob  # Подключаем библиотеку для работы с файлами определенного расширения
import os  # Подключаем библиотеку для работы с файловой системой


path = str(input('Введите путь к файлу: \n'))
regxp = '[\w-]+[\w:]'
result = re.findall(regxp, path)  # Разбиваем введенный адрес на составляющие без обратного слеша
path = '\\\\'.join(result)  # Добавляем двойной слеш после каждой папки (под формат Python)

os.chdir(path)

for file in glob.glob('*.fb2'):
    detector = UniversalDetector()
    with open(file, 'rb') as file_encoding:
        for line in file_encoding:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    file_encoding = str(detector.result['encoding'])

    if file_encoding == False:
        continue
    else:
        with open(file, 'r', encoding=file_encoding) as file_name:
            stroke = file_name.read()
            stroke = str(stroke)
            reg_year = '<year>(.+)</year>'
            reg_title = '<book-title>(.+)</book-title>'
            reg_last_name = '<last-name>(.+)</last-name>'
            reg_first_name = 'first-name>(.+)</first-name>'

            year = str(re.findall(reg_year, stroke))
            year = year.replace('\'', '').replace('\"', '').replace(':', '').replace('#', '').replace('(', ''). \
                replace(')', '').replace('[', '').replace(']', '').replace('!', '').replace('?', '').replace('\\', ''). \
                replace('/', '').replace('.', '').replace('«', '').replace('»', '').replace(',', '').replace('-', '')

            title = re.findall(reg_title, stroke)
            title = str(title)
            title = title.replace('\'', '').replace('\"', '').replace(':', '').replace('#', '').replace('(', ''). \
                replace(')', '').replace('[', '').replace(']', '').replace('!', '').replace('?', '').replace('\\', ''). \
                replace('/', '').replace('.', '').replace('«', '').replace('»', '').replace(',', '').replace('-', '')

            last_name = re.findall(reg_last_name, stroke)
            print('Фамилия после поиска первой регуляркой: ', last_name)
            print('Тип фамилии:', type(last_name))
            if len(last_name) > 0:
                last_name = last_name[0]
                last_name = ''.join(last_name)
                last_name = str(last_name)
            else:
                last_name = str('БезФамилии')
            print('Фамилия после уборки лишних знаков: ', last_name)
            print('Тип фамилии:', type(last_name))
            reg_last_names = '^\w*'
            last_name = re.findall(reg_last_names, last_name)
            print('Фамилия после поиска второй регуляркой: ', last_name)
            print('Тип фамилии:', type(last_name))
            last_name = str(''.join(last_name))

            first_name = re.findall(reg_first_name, stroke)
            print('Результат имени после работы первой регулярки: ', first_name)
            print('Тип имени: ', type(first_name))
            if len(first_name) > 0:
                first_name = first_name[0]
                first_name = ''.join(first_name)
                first_name = str(first_name)
            else:
                first_name = str('БезИмени')
            print('Имя после уборки лишних знаков: ', first_name)
            reg_first_names = '^\w*'
            first_name = re.findall(reg_first_names, first_name)
            print('Имя после обработки второй регуляркой: ', first_name)
            print('Тип имени: ', type(first_name))
            first_name = str(''.join(first_name))

lst = [title, first_name + ' ' + last_name, year]
print(lst)
