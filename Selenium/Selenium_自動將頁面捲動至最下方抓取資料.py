from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

driver = webdriver.Chrome()
driver.implicitly_wait(3)
kind = '牛排'
driver.get('https://tw.eztable.com/search?country=tw&date=2018-07-10&people=2&q=' + kind)

for i in range(0 , 10):
      driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
      time.sleep(1)
soup = BeautifulSoup(driver.page_source) 

title = []  
for i in soup.select("[class='sc-dEoRIm bNFseq']"):
      title.append(i.text)
title = pd.DataFrame(title)
      
price = []       
for j in soup.select("[class='sc-LKuAh ctVoYT']"):   
      price.append( int(j.text.split(' ')[1].replace(',' , '')) )
price = pd.DataFrame(price)      
      
rate ,population = [] , []
for k in soup.select("[class='sc-kkGfuU eyGEhS']"):   
      rate.append(float(k.text.split('(')[0]))
      population.append(int(k.text.split('(')[1].replace(')' , '')))
rate , population = pd.DataFrame(price)  , pd.DataFrame(population)     

data = (pd.concat([title , price , rate , population] , axis = 1)).T 
      
