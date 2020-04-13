import re, os


def re_subs(from_string, to_string, source, destination='results', file_zones='zones'):
    """ Функция замены текста в файлах из списка "l":
        source  - папка где расположены файлы в которых нужно заменять текст
        destination  - папка куда сохранять файлы в которых текст изменен
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
        print("Directory created. New files saved in folder '" + destination + "'", sep='')
    except FileExistsError:
        pass

    for i in list_:
        try:
            data = open(source + '/' + i).read()
            o = open(destination + '/' + i, 'w')
            o.write(re.sub(from_string, to_string, data))
            o.close()
        except FileNotFoundError as error:
            print('Error:', error)


def main():
    source = 'data.db'
    re_subs('IN SOA	ispm.ukrtel.net. root.ispm.ukrtel.net.', 'IN SOA	dispm.ukrtel.net. root.dispm.ukrtel.net.', source)
    re_subs('IN SOA	ispm.ukrtel.net. support-dc.ukrtelecom.ua.', 'IN SOA	dispm.ukrtel.net. root.dispm.ukrtel.net.', source)
    re_subs('NS	isp1.ukrtel.net.', '; NS	isp1.ukrtel.net.', source)
    re_subs('NS	isp2.ukrtel.net.', 'NS	dispm.ukrtel.net.', source)


if __name__ == '__main__':
    main()
