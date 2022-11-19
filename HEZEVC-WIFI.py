import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from selenium.webdriver.common.by import By
resp = urlopen("http://10.1.0.1:8080/byod/")  # 打开校园网登陆界面
code = resp.getcode()
if code == 200:  # get值200，则正确打开
    f = open("UserNK.txt")  # 读取记事本，这里可以自己改名
    user_name, user_key = f.read().splitlines()  # 按行读取并赋值账户和密码
    f.close()
    driver = webdriver.Edge("C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")  # 调用浏览器驱动程序
    driver.get("http://10.1.0.1:8080/byod/")  # 打开校园网登陆界面
    driver.maximize_window()  # 最大化窗口
    time.sleep(1)  # 等待一秒
    driver.find_element(By.ID, "id_userName").click()  # 找到用户名输入窗口
    driver.find_element(By.ID, "id_userName").send_keys(user_name)  # 输入账号
    driver.find_element(By.ID, "id_userName").send_keys(Keys.TAB)  # 换行到账号密码窗口
    driver.find_element(By.ID, "id_userPwd").send_keys(user_key)  # 输入密码
    driver.find_element(By.ID, "id_userPwd").send_keys(Keys.ENTER)  # 登陆
    driver.quit()  # 退出selenium指令集
else:
    sys.exit()  # 如果get值不为200，则退出此程序
