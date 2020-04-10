import re


def re_subs(source, destination, from_string, to_string, file_zones='zones'):
    """ Функция замены текста в файлах из списка "l":
        source  - папка где расположены файлы в которых нужно заменять текст
        destination  - папка куда сохранять файлы в которых текст изменен
        from_string  - текст который нужно заменять
        to_string  - текст на который нужно заменять
        file_zones - имя файла в котором хранится список файлов которые нужно обработать (по умолчанию 'zones')"""
    list = []
    with open(file_zones) as f:
        list = f.read().splitlines()
    for i in list:
        try:
            data = open(source + '/' + i).read()
            o = open(destination + '/' + i, 'w')
            o.write(re.sub(from_string, to_string, data))
            o.close()
        except FileNotFoundError as error:
            print('Error:', error)


def main():
    re_subs('data.db', 'new.data.db', 'IN SOA	ispm.ukrtel.net. root.ispm.ukrtel.net.', 'IN SOA	dispm.ukrtel.net. root.dispm.ukrtel.net.')
    re_subs('new.data.db', 'new.data.db', 'IN SOA	ispm.ukrtel.net. support-dc.ukrtelecom.ua.', 'IN SOA	dispm.ukrtel.net. root.dispm.ukrtel.net.')
    re_subs('new.data.db', 'new.data.db', 'NS	isp1.ukrtel.net.', '; NS	isp1.ukrtel.net.')
    re_subs('new.data.db', 'new.data.db', 'NS	isp2.ukrtel.net.', 'NS	dispm.ukrtel.net.')


if __name__ == '__main__':
    main()
