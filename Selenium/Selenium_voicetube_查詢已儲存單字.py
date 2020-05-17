from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from bs4 import BeautifulSoup
import pandas as pd
import re

driver = webdriver.Chrome()
driver.get("https://tw.voicetube.com/")
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='中文(繁體)'])[2]/following::a[1]").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='電子信箱'])[1]/preceding::button[1]").click()
driver.find_element_by_id("email").click()
driver.find_element_by_id("email").clear()
driver.find_element_by_id("email").send_keys("tommot7852@kimo.com")
driver.find_element_by_id("pass").click()
driver.find_element_by_id("pass").clear()
driver.find_element_by_id("pass").send_keys("tom16812358132134")
driver.find_element_by_id("loginbutton").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='其它測驗單字'])[1]/following::img[1]").click()
try:
    driver.find_element_by_xpath("//button[@class='toast-close-button']").click()
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='其它測驗單字'])[1]/following::img[1]").click()
    driver.find_element_by_link_text(u"我的筆記").click()
except NoSuchElementException :
    driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='其它測驗單字'])[1]/following::img[1]").click()
    driver.find_element_by_link_text(u"我的筆記").click()
   
    
soup = BeautifulSoup(driver.page_source , 'html5lib')   
title = []
href = []
for i in soup.select("[style='text-decoration: none;']"):
    title.append(i.text)
    ptn = i['href'] + '\?note_time=+\d+'
    temp = re.findall(ptn , str(soup.select("[id='captions_block']")[0]))
    href.append(temp)
vob = []
for j in range(0 , len(title)):
    vob_sub = []
    for jj in range(0 , len(href[j])):
        input_ = '[href=' + '\'' + href[j][jj] + '\']' 
        vob_sub.append(soup.select(input_)[1].text)
    vob.append(vob_sub)    
 
       
vob_pd = pd.DataFrame(vob)
vob_pd = vob_pd.T
vob_pd = vob_pd.drop_duplicates(subset = None , keep = 'first' , inplace = False).T
vob_pd['vedio_title'] = pd.DataFrame(title)
vob_pd = vob_pd.set_index(['vedio_title'])

vob_pd.to_excel('voicetube_my_vob_note.xls')    