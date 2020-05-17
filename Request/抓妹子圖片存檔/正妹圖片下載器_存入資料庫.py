# 爬取網站抓圖片並且存檔
import requests
from bs4 import BeautifulSoup
import shutil
import sqlite3 

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36'}
res = requests.get('https://ck101.com/thread-4581034-1-1.html' , headers = headers)
soup = BeautifulSoup(res.text , 'html.parser')


fname = []
img_list = []
for i , img in enumerate(soup.select("[class='zoom']")):
    try:
        img_list.append(img['file']) 
        fname.append(img['file'].split('/')[4][0 : -7]) 
        
#        # 下載方法_1
#        # 如果想獲取來自服務器的原始套接字響應，可以取得 r.raw 
#        # 需要在初始請求中設置 stream=True
#        res_img = requests.get(img['file'] , stream = True , headers = headers) 
#        f = open(img['file'].split('/')[4][0 : -7] , 'wb')
#        shutil.copyfileobj(res_img.raw , f)
#        f.close()
        
        # 下載方法_2
        res_img = requests.get(img['file'])
        with open(img['file'].split('/')[4][0 : -7] , 'wb') as f:
            f.write(res_img.content)
            f.close()
        del res_img
        
    except KeyError:
        print('{} , no address'.format(i))


# 建立資料庫及資料表存放正妹圖片
db_name = '妹子.sqlite'
cmd = 'CREATE TABLE girl_image (id INTEGER PRIMARY KEY AUTOINCREMENT, img INTEGER)'
conn = sqlite3.connect(db_name)
c = conn.cursor()
c.execute(cmd)
conn.commit()
conn.close()      


# 將下載好的圖以byte的方式存入剛才建好的資料庫
for i , img_name in enumerate(fname):
    f = open(img_name , 'rb')
    read_image = f.read()
    f.close()
    conn = sqlite3.connect('妹子.sqlite')
    cur = conn.cursor()
    cur.execute('insert into girl_image (img) values(?)' , [sqlite3.Binary(read_image)])
    conn.commit()