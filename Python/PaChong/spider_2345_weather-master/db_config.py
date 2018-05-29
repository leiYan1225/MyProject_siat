import pymongo

client = pymongo.MongoClient('localhost',27017)
weather = client['weather']
city_id_table = weather['city_id_table']
city_weather_table = weather['city_weather_table']
hangzhou_weather_table = weather['hangzhou_weather_table']

date_list = ['201701','201702','201703','201704','201705','201706','201707','201708','201709','201710',
'201711','201712','201601','201602','201603','201604','201605','201606','201607','201608','201609','201610',
'201611','201612',]
