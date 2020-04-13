import re
import os


def re_subs(from_string, to_string, source, destination='results', file_zones='zones'):
    """ Функция замены текста в файлах из списка "l":
        source  - папка где расположены файлы в которых нужно заменять текст
        destination  - папка куда сохранять файлы в которых текст изменен (по умолчанию 'results')
        from_string  - текст который нужно заменять
        to_string  - текст на который нужно заменять
        file_zones - имя файла в котором хранится список файлов которые нужно обработать (по умолчанию 'zones')"""
    list_ = []
    try:
        with open(file_zones) as f:
            list_ = f.read().splitlines()
    except FileNotFoundError as error:
        print('Файл со списком не найден:', error)

    try:
        os.mkdir(destination)
        print("Directory created. New files have been saved in folder '" + destination + "'", sep='')
    except FileExistsError:
        pass

    for i in list_:
        try:
            data = open(source + '/' + i).read()
            o = open(destination + '/' + i, 'w', encoding="utf-8")
            o.write(re.sub(from_string, to_string, data))
            o.close()
        except FileNotFoundError as error:
            print('Error:', error)


def main():
    source = 'data.db'
    re_subs('IN SOA\tispm.ukrtel.net. root.ispm.ukrtel.net.', 'IN SOA\tdispm.ukrtel.net. root.dispm.ukrtel.net.', source)
    re_subs('IN SOA\tispm.ukrtel.net. support-dc.ukrtelecom.ua.', 'IN SOA\tdispm.ukrtel.net. root.dispm.ukrtel.net.', source)
    re_subs('NS	isp1.ukrtel.net.', '; NS\tisp1.ukrtel.net.', source)
    re_subs('NS	isp2.ukrtel.net.', 'NS\tdispm.ukrtel.net.', source)


if __name__ == '__main__':
    main()
