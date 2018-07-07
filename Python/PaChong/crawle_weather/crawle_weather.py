import datetime
import pandas as pd
import xlsxwriter as xlw
from urllib import request
from bs4 import BeautifulSoup as bs

def dateRange(start, end):
    datelist1 = [datetime.datetime.strftime(x, '%Y%m') for x in list(pd.date_range(start=start, end=end))]
    datelist = sorted(list(set(datelist1)))
    return datelist

# 爬取“天气网”天气预报
def getCommentsById(city, start, end):  # city为字符串，year为列表，month为列表
    weather_result = []
    datelist = dateRange(start, end)
    for i in datelist:
        url = 'http://lishi.tianqi.com/' + city + '/' + i + '.html'
        opener = request.Request(url)
        opener.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
        req = request.urlopen(opener).read()
        soup = bs(req, 'html.parser')
        weather_m = soup.select('div .tqtongji2 > ul')  # .表示class; ‘#tongji’表示id等价于a[id='tongji']
        print(weather_m)
        for i in weather_m[1:]:  # 因为第一个为表头，所以筛除掉
            tt = []
            for j in range(6):
                t = i.find_all('li')[j].string
                if t is not None:  # 存在None值的进行处理，否则不能写入到excel
                    tt.append(t)
                else:
                    tt.append('None')
            weather_result.append(tt)
    return weather_result

#  list数据写入到本地excel中
def list_to_excel(weather_result, filename):
    workbook = xlw.Workbook('%s.xlsx' % filename)
    sheet = workbook.add_worksheet('weather_report')
    title = ['日期', '最高气温', '最低气温', '天气', '风向', '风力']
    for i in range(len(title)):
        sheet.write_string(0, i, title[i], workbook.add_format({'bold': True}))  # 写入表头，字体加粗
    row, col = 1, 0
    for a, b, c, d, e, f in weather_result:
        sheet.write_string(row, col, a)
        sheet.write_string(row, col + 1, b)
        sheet.write_string(row, col + 2, c)
        sheet.write_string(row, col + 3, d)
        sheet.write_string(row, col + 4, e)
        sheet.write_string(row, col + 5, f)
        row += 1
    workbook.close()

if __name__ == '__main__':
    data = getCommentsById('shenzhen', '2017-01', '2017-12')
    list_to_excel(data, '深圳天气201701-201712')
