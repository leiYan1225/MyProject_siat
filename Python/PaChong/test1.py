import requests
from bs4 import BeautifulSoup as bs
from urllib import request
from urllib import parse
#
#以豆瓣‘编程’分类的一个连接URL为例子开始爬数据ID
# url = 'https://book.douban.com/tag/编程?start=20&type=T'
# res = requests.get(url)  #发送请求
# print(res.encoding)    #这个是用来查看网页编码的
# #res.encoding = 'utf-8'   #跟上一个结合来用，如果编码有乱码，则可以通过这个定义编码来改变
# html = res.text
# #print(html)
#
# IDs = []
# soup  = bs(html,"html.parser")     #定义一个BeautifulSoup变量
# items = soup.find_all('a',attrs={'class':'nbg'}) #查找a标签且a标签的属性是class='nbg'，我们只需要这种a标签。items得到的是一个list
# print(items)
#
# for i in items:
#     idl = i.get('href')  # dict.get 获取key 对应的value
#     print(idl)
#     id = idl.split('/')[4]
#     print(id)
#     IDs.append(id)
# print('这一页收集到书籍ID数：%d' % len(IDs))



# url = 'http://tianqi.2345.com/wea_history/72037.htm'
# res = requests.get(url)  #发送请求
# # print(res.encoding)    #这个是用来查看网页编码的
# #res.encoding = 'utf-8'   #跟上一个结合来用，如果编码有乱码，则可以通过这个定义编码来改变
# html = res.text
#
# IDs = []
# soup  = bs(html,"html.parser")     #定义一个BeautifulSoup变量
# items = soup.find_all('a',attrs={'class':'nbg'}) #查找a标签且a标签的属性是class='nbg'，我们只需要这种a标签。items得到的是一个list
# print(items)
#
# for i in items:
#     idl = i.get('href')  # dict.get 获取key 对应的value
#     print(idl)
#     id = idl.split('/')[4]
#     print(id)
#     IDs.append(id)
# print('这一页收集到书籍ID数：%d' % len(IDs))


values = {"username":"1016903103@qq.com","password":"XXXX"}
data = parse.urlencode(values)

url = "http://tianqi.2345.com/wea_history/72037.htm"
opener = request.Request(url,data)
opener.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
req = request.urlopen(opener).read()
soup = bs(req, 'html.parser')
# weather_m = soup.select('div#weather_tab.data-table')  # .表示class; ‘#tongji’表示id等价于a[id='tongji']

for tag in soup.find_all(True):
    print(tag)

# print(weather_m)
#
# url = 'http://lishi.tianqi.com/shenzhen/201706.html'
# opener = request.Request(url)
# opener.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
# req = request.urlopen(opener).read()
# soup = bs(req, 'html.parser')
# # weather_m = soup.select('.tqtongji2 > ul')  # .表示class; ‘#tongji’表示id等价于a[id='tongji']
#
# for tag in soup.find_all(True):
#     print(tag)