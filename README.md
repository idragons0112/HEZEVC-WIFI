# HEZEVC-WIFI
此python程序使用selenium进行爬虫控制登陆菏泽职业学院校园网站，需要与之相对应的浏览器驱动，从而实现一键登录菏泽职业学院校园网
与其他高校校园网不同的是，菏职校园网网站登陆界面登陆之后并没post返回值，抓包程序也获取不到username和userpwd
所以只能通过最简单的selenium函数进行爬虫
此方法适合所有获取不到post值和get值的校园网网站

需要安装selenium和pyinstaller

需要下载对应的edge驱动

https://user-images.githubusercontent.com/108582074/202393931-286ac0a8-6d74-4720-913b-c386a77534e3.mp4

edge浏览器驱动下载地址自行百度
![QQ截图20221117161449](https://user-images.githubusercontent.com/108582074/202392614-bed605bb-d6a8-4b91-a070-01b5d9d87a08.png)
在driver = webdriver.Edge('这里面放浏览器驱动程序所在位置')
![5}$ CLE~9B 6HRS}Z~APRQY](https://user-images.githubusercontent.com/108582074/202392671-4e87e31e-d16d-42b8-86e4-30568115b397.png)

在文件UserNK.txt中，第一行输入校园网账号，第二行输入校园网密码

![QQ截图20221117161629](https://user-images.githubusercontent.com/108582074/202392810-d5cd8cce-3943-4328-84cc-5e93326533b5.png)

python编译完成后，使用pyinstaller进行封包，并加入开机自启动项
