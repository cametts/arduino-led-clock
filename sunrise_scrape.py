# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 10:20:52 2020

@author: metts
"""
# -*- Web scraping to pull the time of sunrise and sunset -*-
#TODO: compile and export times into Arduino-readable format 

import requests
from bs4 import BeautifulSoup as bsoup
import re

#specify US zip code, month, year
zipcode = ' '
month = '9'
year = '2020'

template_url = 'https://www.timeanddate.com/sun/@z-us-%s?month=%s&year=%s'
search_url = template_url % (zipcode, month, year)
htmlDoc = requests.get(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}).content
parsed_html = bsoup(htmlDoc, 'lxml')
data = parsed_html.find_all("tr", attrs={})

#pull out full-month time data 
data = data[10:len(data)-1] 

#list days of the month
days = list(range(1, len(data)+1))

for row in data:
    #pull hour, minute, am/pm for sunrise (other rows are twilight times)
    for sunrise in row.find_all('td', attrs={'class' : 'c sep'}):
        if len(sunrise) > 1:
            sunrise = sunrise.text.split(' ')
            time = sunrise[0].split(':')
            hour = int(time[0])
            minute = int(time[1])
            sunrise_am = (sunrise[1] == 'am') #True if sunrise is in the morning
           
    #pull hour, minute, am/pm for sunset (other rows are twilight times)
    for sunset in row.find_all('td', attrs={'class' : 'sep c'}):
        if len(sunset) > 1:
            sunset = sunset.text.split(' ')
            time = sunset[0].split(':')
            hour = int(time[0])
            minute = int(time[1])
            sunset_am = (sunset[1] == 'am') #False if sunset is in the evening
       
            
    
    