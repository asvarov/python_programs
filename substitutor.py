import re
import os


def re_subs(from_string, to_string, source, file_zones='zones'):
    """ Функция замены текста в файлах из списка "file_zones":
        from_string  - текст который нужно заменять
        to_string  - текст на который нужно заменять
        source  - папка где расположены файлы в которых нужно заменять текст
        file_zones - имя файла в котором хранится список файлов которые нужно обработать (по умолчанию 'zones')"""
    list_, list2_ = [], []
    try:
        with open(file_zones) as f:
            list_ = f.read().splitlines()
    except FileNotFoundError as error:
        print('Файл со списком не найден:', error)

    for i in list_:
        try:
            path_read_file = os.path.join(source, i)
            with open(path_read_file) as read_data:
                list2_ = read_data.read()
                path_write_file = open(path_read_file, 'w', encoding='utf-8')
                path_write_file.write(re.sub(from_string, to_string, list2_))
        except FileNotFoundError:
            print('Error: No such file or directory:', os.path.join(source, i))
        except IsADirectoryError:
            print('Error: В файле со списком содержаться пустые строки!')
        except UnicodeDecodeError:
            print('Ошибка кодировки в файле зоны: ' + path_read_file)
        # except Exception as e:
        #     print(e)
        #     exit(1)


def main():
    source = 'data.db'
    re_subs('IN SOA\tispm.ukrtel.net. root.ispm.ukrtel.net.', 'IN SOA\tdispm.ukrtel.net. root.dispm.ukrtel.net.', source)
    re_subs('IN SOA\tispm.ukrtel.net. support-dc.ukrtelecom.ua.', 'IN SOA\tdispm.ukrtel.net. root.dispm.ukrtel.net.', source)
    re_subs('\tNS\tisp1.ukrtel.net.', '\t;NS\tisp1.ukrtel.net.', source)
    re_subs('\tNS\tisp2.ukrtel.net.', '\tNS\tdispm.ukrtel.net.', source)


if __name__ == '__main__':
    main()
