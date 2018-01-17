# -*- coding: utf-8 -*-

'''
Задание 13.1a

Переделать функцию generate_cfg_from_template:
* добавить поддержку использования шаблона, который находится в текущем каталоге

Для проверки, скопируйте один из шаблонов из каталога templates,
в текущий каталог скрипта.

Можно проверить на тех же шаблоне и данных, что и в прошлом задании:
* шаблоне templates/for.txt (но скопировать его в текущий каталог) и данных data_files/for.yml

'''

#Решение

def config(path, yamlfile):
    if '/' in path:
        TEMPLATE_DIR, template_file = path.split('/')
    else:
        TEMPLATE_DIR = '.'
        template_file = path
    #TEMPLATE_DIR, template_file = path.split('/')
    VARS_FILE = yamlfile
    env = Environment(loader = FileSystemLoader(TEMPLATE_DIR),
                      trim_blocks=True, lstrip_blocks=True)
    template = env.get_template(template_file)

    vars_dict = yaml.load(open(VARS_FILE))

    print(template.render(vars_dict))


config(sys.argv[1], sys.argv[2])
