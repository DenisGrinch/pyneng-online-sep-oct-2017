# -*- coding: utf-8 -*-

'''
Задание 11.1a

Скопировать скрипт add_data.py из задания 11.1.

Добавить в файл add_data.py проверку на наличие БД:
* если файл БД есть, записать данные
* если файла БД нет, вывести сообщение, что БД нет и её необходимо сначала создать

'''

# Решение 

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



test = adddata(result)
