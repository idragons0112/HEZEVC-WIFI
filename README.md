# hezevcxyw
此python程序使用selenium进行爬虫控制登陆菏泽职业学院校园网站，需要与之相对应的浏览器驱动
与其他高校校园网不同的是，菏职校园网网站登陆界面登陆之后并没post返回值，抓包程序也获取不到username和userpwd
所以只能通过最简单的selenium函数进行爬虫
此方法适合所有获取不到post值和get值的校园网网站

edge浏览器驱动下载地址自行百度
在driver = webdriver.Edge('这里面放浏览器驱动程序所在位置')

driver.find_element(By.ID, "id_userName").send_keys('这里面输入校园网账号')

driver.find_element(By.ID, "id_userPwd").send_keys('这里面输入校园网密码')

python编译完成后，使用pyinstaller进行封包，并加入开机自启动项
