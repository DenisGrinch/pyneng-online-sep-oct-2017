## Дополнительные скрипты

### submit_tasks.py

Скрипт позволяет добавлять комментарий на GitHub к последнему коммиту.
Комментарий нужен для [сдачи заданий](https://pyneng.github.io/docs/task-check/)

Лучше скопировать скрипт из репозитория курса в какой-то другой каталог, так как вы будете его менять.

Для начала использования, надо написать свои логин, пароль и имя репозитория на GitHub в начале файла. Например:
```python
#Имя пользователя GitHub:
username = 'nata'
#Пароль пользователя на GitHub
password = 'natapass'
#Название репозитория. Например online-3-natasha-samoylenko
repo_name = 'natasha-repo'
```

После этого, можно запускать скрипт таким образом:
```
$ python submit_tasks.py "Сделал задания 3.1, 3.2, 3.3"
К последнему коммиту добавлен такой комментарий:
Сделал задания 3.1, 3.2, 3.3
```

Скрипту надо передавать один аргумент - текст комментария.

> По умолчанию, скрипт ищет коммиты только за последние 14 дней.
Если вы делали последний коммит раньше, скрипт напишет сообщение, что за указанный срок  коммиты не были найдены.

