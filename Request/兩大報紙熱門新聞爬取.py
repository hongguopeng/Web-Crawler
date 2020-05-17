import requests
from bs4 import BeautifulSoup

#蘋果日報----------------------------------------------熱門新聞
res = requests.get('http://www.appledaily.com.tw/appledaily/hotdaily/headline')
soup = BeautifulSoup(res.text , 'html5lib')

title_apple , href_apple = [] , []
for i in soup.select("[class='aht_title']"):
    title_apple.append(i.select("[target='_blank']")[0]['title'])
    href_apple.append(i.select("[target='_blank']")[0]['href'])
    
people_read_apple = []

for i in soup.select("[class='aht_title_pv']"):
    people_read_apple.append(i.select("[class='aht_pv_num']")[0].text)

#############################################################################
#from bs4 import BeautifulSoup
#from selenium import webdriver

#url = 'http://www.appledaily.com.tw/appledaily/hotdaily/headline'
#driver = webdriver.Chrome()
#driver.get(url)
#
#button = ['國際' , '財經' , '副刊' , '體育']
#for i in range(0 , len(button)):        
#    driver.find_element_by_link_text(button[i]).click()
#    driver.back()
#    
#driver.quit() 
#蘋果日報----------------------------------------------熱門新聞
    

#自由時報----------------------------------------------熱門新聞    
res = requests.get('http://news.ltn.com.tw/list/newspaper')
soup = BeautifulSoup(res.text , 'html5lib')

title_free , href_free = [] , []
for i in soup.select("[class='tit']"):
    title_free.append(i.select('p')[0].text)
    href_free.append(i['href'])
#自由時報----------------------------------------------熱門新聞 
















