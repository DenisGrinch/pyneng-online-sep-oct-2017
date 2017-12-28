# -*- coding: utf-8 -*-

'''
Задание 11.1

На основе файла create_sqlite_ver3.py из раздела, необходимо создать два скрипта:
* create_db.py
 * сюда должна быть вынесена функциональность по созданию БД:
  * должна выполняться проверка наличия файла БД
  * если файла нет, согласно описанию схемы БД в файле dhcp_snooping_schema.sql, должна быть создана БД (БД отличается от примера в разделе)
* add_data.py
 * с помощью этого скрипта, выполняется добавление данных в БД
  * добавлять надо не только данные из вывода sh ip dhcp snooping binding, но и информацию о коммутаторах

Код в скриптах должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.

В БД теперь две таблицы (схема описана в файле dhcp_snooping_schema.sql):
 * switches - в ней находятся данные о коммутаторах
 * dhcp - эта таблица осталась такой же как в примере, за исключением поля switch
  * это поле ссылается на поле hostname в таблице switches

Соответственно, в файле add_data.py должны быть две части:
* информация о коммутаторах добавляется в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* информация на основании вывода sh ip dhcp snooping binding добавляется в таблицу dhcp
 * вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch, его нужно также заполнять. Имя коммутатора определяется по имени файла с данными

На данном этапе, оба скрипта вызываются без аргументов.

'''

# Решение

# Модуль создания базы

import os
import sqlite3


schema_filename = 'dhcp_snooping_schema.sql'

def createdb(dbname):
    db_exists = os.path.exists(dbname)
    if not db_exists:
        print('Creating schema...')
        conn = sqlite3.connect(dbname)
        with open(schema_filename, 'r') as f:
            schema = f.read()
        conn.executescript(schema)
        conn.close()
        print('Done')
    else:
        print('Database exists, assume dhcp table does, too.')



test = createdb('testbase.db')

# Модуль добавления данных

import sqlite3
import re
import glob

dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')

regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

result = []

for i in dhcp_snoop_files:
    with open(i) as data:
        for line in data:
            match = regex.search(line)
            if match:
                result.append(match.groups())


def adddata(datalist):
    for row in datalist:
        conn = sqlite3.connect('testbase.db')
        try:
            with conn:
                query = '''insert into dhcp (mac, ip, vlan, interface)
                           values (?, ?, ?, ?)'''
                conn.execute(query, row)
        except sqlite3.IntegrityError as e:
            print('Error occured: ', e)
    conn.close()

test = adddata(result)

