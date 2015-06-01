#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2015, Dmitry Mazhartsev
# GNU General Public License Version 3

import os
import sys
import shutil
import re
# import magic

# =====================================================================
# Проверка наличия аргументов 
if len(sys.argv) == 1:
    file_dir = os.getcwd()
    print('{0}\nТекущий каталог: {1}'.format('='*70, file_dir))
else:
    print('Указаны несуществующие аргументы')
    sys.exit()

# =====================================================================
# Папка для обработанных файлов
out = 'out'

# Если папка out отсутствует, то создать её
if os.path.exists(out) == False:
    os.mkdir(out)

print('Папка с обработанными файлами: {0}'.format(os.path.abspath(out)))
print('='*70)

# ====================================================================
# Список замен

regexp = [
['&(?!lt;|gt;|amp;|quot;|apos;)', '&amp;'],
['<(?=[\d\>\<])', '&lt;'],
['(?<=[";])<', '&lt;'],
['(?<=[\&lt;\>\d])>','&gt;'],
['→','']
]

#['&', '&amp;'],
#['(?=[\>\d\w])','']

# ====================================================================
# Лечащая функция
def healer(file, enc):
    # Исходный файл
    src = file
    
    # Исцеленный файл
    out_file = '{0}/{1}'.format(out,src)
    #print('Файл {0} исцелен!\n'.format(out_file)) 
    print('Исцелен!\n')
    
    # Открыть исходный файл в режиме чтения и записи
    sick_file = open(src, encoding=enc)
    # Открыть конечный файл в режиме записи
    heal_file = open(out_file, 'w', encoding=enc)
    
    # Построчное чтение и запись
    for f in sick_file:
        for r in regexp:
            f = re.sub(r[0], r[1], f)
            #f = re.sub('(?<=[";])<', '&lt;', f)
            #print(f)
        heal_file.write(f)

    # Закрыть все файлы
    sick_file.close()
    heal_file.close()

# =====================================================================
# Поиск xml файлов в текущей директории

xml_list = [] # пустой список для xml
file_list = os.listdir(file_dir) # список всех файлов в папке
#print(file_list)

enc = 'windows-1251'

for file in file_list:
    print('Имя файла: {0}'.format(file))
    if file.endswith('.xml'):
        xml_list.append(file)
        healer(file, enc)
    else:
        print('Не является XML-файлом\n')
            




'''
for file in file_list:
    print('Имя файла: {0}'.format(file))
    m = magic.open(magic.MAGIC_MIME)
    m.load()
    type = m.file(file)
    type = type.split(';')
    enc = type[1].split('=')
    enc = enc[1]
    print('Кодировка: {0}'.format(enc))
    #print(a)
    if type[0] == 'application/xml':
        xml_list.append(file)
        healer(file, enc)
    else:
        print('Не является XML-файлом\n')
'''        
#print('Файлы для обработки:{0}\n{1}\n'.format(xml_list,'='*70))

#for i in xml_list:
  #  healer(i, enc)


# Определение типа файла
'''
import magic
m = magic.open(magic.MAGIC_MIME)
m.load()
m.file("/tmp/document.pdf")
In [20]: m.file('NO_NDS')
Out[20]: 'application/xml; charset=iso-8859-1'


import magic

filename = "./datasets/test"

def file_mime_type(filename):
    m = magic.open(magic.MAGIC_MIME)
    m.load()
    return(m.file(filename))

print(file_mime_type(filename))

'''


# =====================================================================
# Информация об обработанных файлах
print('{0}\nОбработаны следующие файлы:'.format('='*70))
for i in xml_list:
    print('- {0}'.format(i))

# Завершение работы скрипта
input('\nНажмите Enter')
