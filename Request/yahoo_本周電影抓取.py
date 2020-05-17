import requests
from bs4 import BeautifulSoup
import re

Y_MOVIE_URL = 'https://tw.movies.yahoo.com/movie_thisweek.html'
resp = requests.get(Y_MOVIE_URL)
soup = BeautifulSoup(resp.text , 'html5lib')

#---------------------------------------------------------#
ch_name = []
count = 0
for i in soup.find_all('div' , 'release_movie_name'):
    for ii in i.find('a' , 'gabtn'):
        temp = ii.replace('\n' , '').lstrip()
        ch_name.append(temp)
        
en_name = []
for i in soup.find_all('div' , 'en'):
    for ii in i.find('a' , 'gabtn'):
        temp = ii.replace('\n' , '').lstrip()
        en_name.append(temp)
        
#ch_name , en_name = [] , []
#for i in soup.select("[class='release_movie_name']"):
#    ch_name.append(i.select("[class='gabtn']")[0].text.replace('\n' , '').split(' ')[-1])
#    en_name.append(i.select("[class='gabtn']")[1].text.replace('\n' , '')[20:]) 
        
#---------------------------------------------------------#

expectation = []
for i in soup.find_all('div' , 'leveltext'):
    for ii in i.find('span'):
        temp = ii
        expectation.append(temp)
        
#expectation = []
#for i in soup.select("[class='leveltext']"):
#    expectation.append(i.select('span')[0].text)
    
#---------------------------------------------------------#
        
release_date = []
for i in soup.find_all('div' , 'release_movie_time'):
    temp = i.text[6:]
    release_date.append(temp)
    
#release_date = []
#for i in soup.select("[class='release_movie_time']"):
#    release_date.append(i.text[6:])  
    
#---------------------------------------------------------#    

intro , trailer , picture , time = [] , [] , [] , []
for i in soup.find_all('div' , 'release_btn color_btnbox'):
    try:
        intro.append(i.find_all('a')[0]['href'])
    except KeyError:
        intro.append('')
    try:
        trailer.append(i.find_all('a')[1]['href'])
    except KeyError:
        trailer.append('')    
    try:
        picture.append(i.find_all('a')[2]['href'])
    except KeyError:
        picture.append('')
    try:
        time.append(i.find_all('a')[3]['href'])
    except KeyError:
        time.append('')

#intro , trailer , picture , time = [] , [] , [] , []
#for i in soup.select("[class='release_btn color_btnbox']"):
#    try:
#        intro.append(i.select('a')[0]['href'])
#    except KeyError:
#        intro.append('')
#    try:
#        trailer.append(i.select('a')[1]['href'])
#    except KeyError:
#        trailer.append('')    
#    try:
#        picture.append(i.select('a')[2]['href'])
#    except KeyError:
#        picture.append('')
#    try:
#        time.append(i.select('a')[3]['href'])
#    except KeyError:
#        time.append('')
    
#---------------------------------------------------------# 

movie_id = []
pattern = '=\d+'
for i in soup.find_all('div' , 'release_btn color_btnbox'):
    temp = i.find_all('a')[2]['href']
    temp_re = re.findall(pattern , temp)[-1].replace('=' , '')
    movie_id.append(temp_re)
    
#movie_id = []
#pattern = '=\d+'
#for i in soup.select("[class='release_btn color_btnbox']"):
#    temp = i.select('a')[2]['href']
#    temp_re = re.findall(pattern , temp)[-1].replace('=' , '')
#    movie_id.append(temp_re)







