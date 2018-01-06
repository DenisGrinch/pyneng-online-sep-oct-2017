# -*- coding: utf-8 -*-

'''
Задание 11.2a

Дополнить скрипт get_data.py из задания 11.2

Теперь должна выполняться проверка не только по количеству аргументов,
но и по значению аргументов.
Если имя аргумента введено неправильно, надо вывести сообщение об ошибке
(пример сообщения ниже).

Файл БД можно скопировать из прошлых заданий

В итоге, вывод должен выглядеть так:

$ python get_data_ver1.py vln 10
Данный параметр не поддерживается.
Допустимые значения параметров: mac, ip, vlan, interface, switch

'''

# Решение

import sqlite3
import sys
import pprint

db_filename = 'testbase.db'

conn = sqlite3.connect(db_filename)


def getdata(*args):
    if len(args) == 0:
        with conn:
            query = "select * from dhcp"
            result = conn.execute(query)
            for row in result:
                pprint.pprint(row)
    elif len(args) == 2:
        conn.row_factory = sqlite3.Row
        key, value = args
        keys = ['mac', 'ip', 'vlan', 'interface']
        if key in keys:
            keys.remove(key)
            print("\nDetailed information for host(s) with", key, value)
            print('-' * 40)
            with conn:
                query = "select * from dhcp where {} = ?".format(key)
                result = conn.execute(query, (value,))
                for row in result:
                    for k in keys:
                        print('{:12}, {}'.format(k, row[k]))
                        print('-' * 40)
        else:
            print('Valid keys are: ' + ", ".join(keys))
    else:
        print('Two or none parameters should be used')


getdata(*sys.argv[1:])
