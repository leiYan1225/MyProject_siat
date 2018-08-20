
import requests
# python 内置的json包
import json

# r = requests.get("http://zhwnlapi.etouch.cn/Ecalender/api/v2/weather?date=20170806&citykey=101010100")
# r.encoding="utf-8"
# print(r.text)

# url统一资源定位符
# 在python中发送请求
# 下载requests包，使用requests发送请求


while True:
    print('------------欢迎使用天气查询系统------------')

    # 1.准备url地址
    city = input('请输入您要查询天气的地点(输入q退出)：')
    if city == 'q':
        break
    url = 'http://api.map.baidu.com/telematics/v3/weather?location=%s' \
          '&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?' % city

    # 2.发送一个get请求，获取url地址下的资源内容
    # get(url) 需要将url地址作为参数进行传递
    # response 接受服务器返回的相应数据
    response = requests.get(url)
    # 把json字符串转换Python中的字典或列表
    print(response.text)
    weather_dict = json.loads(response.text)
    # 根据key取出字典中对应的值
    date = weather_dict.get('date')
    print(date)

    # 取出results列表
    results = weather_dict['results']
    # 取出results中的字典
    detail_dict = results[0]
    # 取出当前城市
    current_city = detail_dict['currentCity']
    current_pm = detail_dict['pm25']
    # 把取出的pm25字符串转换为数字，在进行比较
    pm25 = int(current_pm)
    if pm25 <= 50:
        print('pm%s,优' % pm25)

    elif pm25 <= 100:
        print('pm%s,良' % pm25)

    elif pm25 <= 150:
        print('pm%s,轻度污染' % pm25)

    elif pm25 <= 150:
        print('pm%s,中度污染' % pm25)

    elif pm25 <= 150:
        print('pm%s,重度污染' % pm25)

    else:
        print('pm%s,严重污染' % pm25)

    print(u'当前城市：%s' % current_city)


    index_list = detail_dict['index']

    for index in index_list:
        title = index['title']
        zs = index['zs']
        tipt = index['tipt']
        des = index['des']
        print(u'标题：%s 指数：%s 提示：%s 建议：%s ' % (title, zs, tipt, des))

    weather_data_list = detail_dict['weather_data']
    for weather_dict in weather_data_list:
        date = weather_dict['date']
        dayPictureUrl = weather_dict['dayPictureUrl']
        nightPictureUrl = weather_dict['nightPictureUrl']
        weather = weather_dict['weather']
        wind = weather_dict['wind']
        temperature = weather_dict['temperature']
        print(u'日期：%s 天气：%s 风力：%s 温度：%s ' % (date, weather, wind, temperature))
