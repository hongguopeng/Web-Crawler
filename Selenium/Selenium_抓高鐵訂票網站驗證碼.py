from selenium import webdriver
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import binarize
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

driver = webdriver.Chrome()
driver.get('https://irs.thsrc.com.tw/IMINT/')
driver.save_screenshot('test.jpg')

element = driver.find_element_by_id('BookingS1Form_homeCaptcha_passCode')
left = element.location['x']
right = element.location['x'] + element.size['width']
top = element.location['y']
bottom = element.location['y'] + element.size['height']

img = Image.open('test.jpg')
img = img.crop((left , top , right , bottom))

img = img.convert('RGBA')
img.save('captua.png')


ori = cv2.imread('captua.png')
dst = cv2.fastNlMeansDenoisingColored(ori , None , 30 , 10 , 7 , 21)
#plt.subplot(211)
#plt.imshow(ori)
#plt.subplot(212)
#plt.imshow(dst)

ret , thresh = cv2.threshold(dst , 127 , 255 , cv2.THRESH_BINARY_INV)
#plt.imshow(thresh)

imgarr = cv2.cvtColor(thresh , cv2.COLOR_BGR2GRAY)
imgarr[: , 10 : 130] = 0

imgdata = np.where(imgarr == 255)
plt.scatter(imgdata[1] , 49 - imgdata[0])
plt.xlim(xmax = 139)
plt.ylim(ymax = 49)
plt.show()
X = imgdata[1].reshape([-1 , 1])
Y = (49 - imgdata[0]).reshape([-1 , 1])


Poly_reg = PolynomialFeatures(2)
X_ = Poly_reg.fit_transform(X)
regr = LinearRegression()
regr.fit(X_ , Y)
X2 = np.array([i for i in range(0 , 139)]).reshape([-1 , 1])
X2_ = Poly_reg.fit_transform(X2)
plt.scatter(X , Y)
plt.xlim(xmax = 139)
plt.ylim(ymax = 49)
plt.plot(X2 , regr.predict(X2_) , color = 'red' , linewidth = 3)
plt.show()


newimg = cv2.cvtColor(thresh , cv2.COLOR_BGR2GRAY)
line_width = 3
for k in range(0 , 139):
    pos = int(49 - regr.predict(X2_)[k])
    newimg[pos - line_width : pos + line_width , k] = 255 - newimg[pos - line_width : pos + line_width , k]
plt.subplot(211)
plt.imshow(ori)
plt.subplot(212)
plt.imshow(newimg)    
















