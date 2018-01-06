# -*- coding: utf-8 -*-

'''
Задание 11.1

add_data.py
* с помощью этого скрипта, выполняется добавление данных в БД
* добавлять надо не только данные из вывода sh ip dhcp snooping binding, но и информацию о коммутаторах


В файле add_data.py должны быть две части:
* информация о коммутаторах добавляется в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* информация на основании вывода sh ip dhcp snooping binding добавляется в таблицу dhcp
 * вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch, его нужно также заполнять. Имя коммутатора определяется по имени файла с данными

Код должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.
'''

import glob

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
#print(dhcp_snoop_files)


# 11 и 11а сразу вставлю сюда. =) 


import sqlite3
import os
import re
import glob

dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')

regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

dbname = input('please enter DB name: ')

db_exists = os.path.exists(dbname)

result = []

for i in dhcp_snoop_files:
    with open(i) as data:
        for line in data:
            match = regex.search(line)
            if match:
                result.append(match.groups())


def adddata(datalist):
    if not db_exists:
        print('No database {0}. Need to create DB first'.format(dbname))
    else:
        for row in datalist:
            conn = sqlite3.connect(dbname)
            try:
                with conn:
                    query = '''insert into dhcp (mac, ip, vlan, interface)
                                       values (?, ?, ?, ?)'''
                    conn.execute(query, row)
            except sqlite3.IntegrityError as e:
                print('Error occured: ', e)
            conn.close()
