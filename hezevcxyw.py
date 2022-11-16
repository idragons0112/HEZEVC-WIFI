import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from selenium.webdriver.common.by import By
resp=urlopen("http://10.1.0.1:8080/byod/templatePage/20190620143747626/guestRegister.jsf")
code=resp.getcode()
if code==200:
    driver=webdriver.Edge("C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")
    driver.get("http://10.1.0.1:8080/byod/templatePage/20190620143747626/guestRegister.jsf")
    driver.maximize_window()
    time.sleep(1)
    driver.find_element(By.ID,"id_userName").click()
    driver.find_element(By.ID,"id_userName").send_keys('19713041150')
    driver.find_element(By.ID,"id_userName").send_keys(Keys.TAB)
    driver.find_element(By.ID,"id_userPwd").send_keys('lwg15000')
    driver.find_element(By.ID,"id_userPwd").send_keys(Keys.ENTER)
    driver.quit()
else:
    sys.exit()