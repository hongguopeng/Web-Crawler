pfrom bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

url = 'http://www.bot.com.tw/house/default.aspx'
driver = webdriver.Chrome()
#driver.set_page_load_timeout(60) # 最多等待網頁開啟60秒
driver.get(url)

driver.find_element_by_id('fromdate_TextBox').send_keys('0800101')
driver.find_element_by_id('todate_TextBox').send_keys('1070101')

# 下拉式選單
purpose = driver.find_element_by_id('purpose_DDL')
purpose.click()
for option in purpose.find_elements_by_tag_name('option'):
    if option.text == '其他':
        option.click()
        
driver.find_element_by_id('Submit_Button').click()
soup = BeautifulSoup(driver.page_source , 'html5lib')

table = soup.select("[cellpadding='3']")
data = []
for row in table[0].select('tr'):
    temp = []
    for element in row.select('td'):
        temp.append(element.text)
    data.append(temp)    
    
#driver.quit()