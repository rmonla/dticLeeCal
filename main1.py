
import urllib.request
from bs4 import BeautifulSoup
	
urlOri = 'https://calendar.google.com/calendar/u/0/embed?src=ps62t3hlmljku5ogtti3sct478@group.calendar.google.com&ctz=America/Argentina/La_Rioja&mode=AGENDA'
# urlOri = 'https://calendar.google.com/calendar/embed?src=ps62t3hlmljku5ogtti3sct478%40group.calendar.google.com&ctz=America%2FArgentina%2FLa_Rioja&mode=AGENDA'
# urlOri = 'https://www.openwebinars.net'

datos = urllib.request.urlopen(urlOri).read().decode()


soup = BeautifulSoup(datos)
tags = soup('a')

for tag in tags:
	print(tag.get('href'))