# -*- coding: utf-8 -*-

'''
Код в скрипте должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.


В примере из раздела, скрипту передавались два аргумента:
* key - имя столбца, по которому надо найти информацию
* value - значение

Теперь необходимо расширить функциональность таким образом:
* если скрипт был вызван без аргументов, вывести всё содержимое таблицы dhcp
 * отформатировать вывод в виде столбцов
* если скрипт был вызван с двумя аргументами, вывести информацию из таблицы dhcp, которая соответствует полю и значению
* если скрипт был вызван с любым другим количеством аргументов, вывести сообщение, что скрипт поддерживает только два или ноль аргументов

> Обработка некорректного ввода аргумента будет выполняться в следующем задании

Файл БД можно скопировать из прошлых заданий


Ниже копия скрипта get_data_ver1.py из раздела
'''

import sqlite3
import sys

db_filename = 'dhcp_snooping.db'


key, value = sys.argv[1:]
keys = ['mac', 'ip', 'vlan', 'interface']
keys.remove(key)

conn = sqlite3.connect(db_filename)

#Позволяет далее обращаться к данным в колонках, по имени колонки
conn.row_factory = sqlite3.Row

print("\nDetailed information for host(s) with", key, value)
print('-' * 40)

query = "select * from dhcp where {} = ?".format( key )
result = conn.execute(query, (value,))

for row in result:
    for k in keys:
        print("{:12}: {}".format(k, row[k]))
    print('-' * 40)


    
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
                pprint.pprint(row, )
    elif len(args) == 2:
        conn.row_factory = sqlite3.Row
        key, value = args
        keys = ['mac', 'ip', 'vlan', 'interface']
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
        print('Two or none parameters should be used')


getdata(*sys.argv[1:])
