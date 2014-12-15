#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" 
Скрипт скачивает ежедневные курсы 
валют с помощью API сайта ЦБ РФ в виде XML файла. 

Затем извлекает из скачанного XML-файла 
данные о курсах валют и записывает их в отдельный файл exchange.txt с разделителем в виде точки с запятой.

Протестировано в GNU/Linux и Windows 7
"""

import urllib.request
from xml.dom import minidom

# Ежедневные курсы валют ЦБ РФ
url = "http://www.cbr.ru/scripts/XML_daily.asp"

# Чтение URL
webFile = urllib.request.urlopen(url)
data = webFile.read()
	
# Имя файла
UrlSplit = url.split("/")[-1]
ExtSplit = UrlSplit.split(".")[1]
FileName = UrlSplit.replace(ExtSplit, "xml")
			
with open(FileName, "wb") as localFile:
	localFile.write(data)

webFile.close()

# Парсинг xml и запись данных в файл
doc = minidom.parse(FileName)

# Извлечение даты
root = doc.getElementsByTagName("ValCurs")[0]
date = "Текущий курс валют ЦБ РФ на {date}г. \n".format(date=root.getAttribute('Date'))

# Заголовок CSV
head = "Идентификатор; Номинал; Название валюты; Сокращение; Курс (руб) \n"

# Извлечение данных по валютам
currency = doc.getElementsByTagName("Valute")

with open("exchange.txt","w") as out:
	out.write(date)
	out.write(head)
	for rate in currency:
		sid = rate.getAttribute("ID")
		charcode = rate.getElementsByTagName("CharCode")[0]
		name = rate.getElementsByTagName("Name")[0]
		value = rate.getElementsByTagName("Value")[0]
		nominal = rate.getElementsByTagName("Nominal")[0]
		str = "{0}; {1}; {2}; {3}; {4} \n".format(sid, nominal.firstChild.data, 
		name.firstChild.data, charcode.firstChild.data, 
		value.firstChild.data)
		out.write(str)
