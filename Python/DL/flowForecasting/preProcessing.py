
import pandas as pd
import numpy as np
import os
import re
from os import walk
from datetime import datetime

##------------------------------------------------------------------------------------------
# # 每一次读取文件为df 再concat()
# files = []
# # walk会返回3个参数，分别是路径，目录list，文件list
# for f, _, i in walk("E:\\datasets\\stationFlow\\IO201701_02"):
#     for j in i:
#         if re.match('part-',j):
#             files.append(j)
#
# frames = []
# # # read_csv() 默认设置为0，即表示第一行为列名,要添加列名的话需要设置为None,并添加names
# for i in files:
#     a = pd.read_csv("E:\\datasets\\stationFlow\\IO201701_02\\"+i,header=None,names=["time","name","inflow","outflow"],index_col=None,sep=",")
#     frames.append(a)
# df = pd.concat(frames)
# df1 = df[df["name"] == "世界之窗"]
# df1["time"] = df1["time"].str.slice(1,20)
# df1["time"] = df1["time"].str.replace("[","")
# df1["time"] =  df1["time"].str.replace("T"," ")
# df1["outflow"] = df1["outflow"].str.replace("]","")
# print(df1)


#------------------------------------------------------------------------------------------
#先合并文件 再读为df 再进行处理
# ##
# newPath = 'E:\\datasets\\stationFlow\\new\\new05_2'
# oldPath = 'E:\\datasets\\stationFlow\\IO20170507_31'
#
# filelist=os.listdir(oldPath)
# newfile=open(newPath,'w',encoding='utf-8') #保存的文件设置为utf-8
# for item in filelist:
#     if re.match('part-', item):
#         for txt in open(oldPath+'\\'+item,'r',encoding='utf-8'): #读取文件是也需要设置utf-8
#             newfile.write(txt)
#
# df = pd.read_csv(newPath,engine='python',header=None,names=['time','name','inflow','outflow'],index_col=None,sep=",",encoding='utf-8')
# df1 = df[df["name"] == "世界之窗"]
# # df1["time"] = df1["time"].str.slice(1,20)
# ## df.iloc(,) 两个参数分别表示行和列, df1["time"] 都可以用df1.iloc[:,0] 替代
# df1["time"] = df1["time"].str.replace("[","")
# df1["time"] = df1["time"].str.replace("T"," ")
# df1["outflow"] = df1["outflow"].str.replace("]","")
# # print(df1)
# # index = 0 不保存索引列，可设置 header,sep,columns 等
# df1.to_csv("E:\\datasets\\stationFlow\\new\\sjzc05_2",encoding='utf-8',index=0,header=0)

#
# newPath = 'E:\\datasets\\stationFlow\\all'
# oldPath = 'E:\\datasets\\stationFlow\\new'
#
# filelist=os.listdir(oldPath)
# newfile=open(newPath,'w',encoding='utf-8') #保存的文件设置为utf-8
# for item in filelist:
#     if re.match('new', item):
#         for txt in open(oldPath+'\\'+item,'r',encoding='utf-8'): #读取文件是也需要设置utf-8
#             newfile.write(txt)
#
# df1 = pd.read_csv(newPath,engine='python',header=None,names=['time','name','inflow','outflow'],index_col=None,sep=",",encoding='utf-8')
#
# # df1["time"] = df1["time"].str.slice(1,20)
# ## df.iloc(,) 两个参数分别表示行和列, df1["time"] 都可以用df1.iloc[:,0] 替代
# df1["time"] = df1["time"].str.replace("[","")
# df1["time"] = df1["time"].str.replace("T"," ")
# df1["outflow"] = df1["outflow"].str.replace("]","")
# # print(df1)
# # index = 0 不保存索引列，可设置 header,sep,columns 等
# df1.to_csv("E:\\datasets\\stationFlow\\all1",encoding='utf-8',index=0,header=0)
#
# # df1 = df[df["name"] == "世界之窗"]


#-----------------------------------------------------------------------------------------------------
## 过滤需要的记录---old

#---------------
# 用正则表达式 貌似不行
# path = 'E:\\datasets\\stationFlow\\sjzc'
# df = pd.read_csv(path,engine='python',header=None,names=['time','name','inflow','outflow'],encoding='utf-8', index_col=None)
# # df1 = df.loc[df["time"].str.match("2017-01-0*"), ["time", "name", "inflow","outflow"]]
# patt  ='2017-..-.. 00.*'
# df1 = df[df["time"].str.match(patt)]
# print(df1)

#--------------
# 老老实实用for 循环吧
# path = 'E:\\datasets\\stationFlow\\sjzc'
# dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
# # 将time 作为行的索引
# df = pd.read_csv(path,engine='python',header=None,names=['time','name','inflow','outflow'],encoding='utf-8',parse_dates=['time'],
#                  index_col='time',date_parser=dateparse)
# # 6月份的工作日和周末
# # workday = ['01','02','05','06','07','08','09','12','13','14','15','16','19','20','21','22','23','26','27','28','29','30'] #日期
# # weekday = ['03','04','10','11','17','18','24','25']
# # 7月份的工作日和周末
# # workday = ['03','04','05','06','07','10','11','12','13','14','17','18','19','20','21','24','25','26','27','28','31'] #日期
# # weekday = ['01','02','08','09','15','16','22','23','29','30']
# # 8月份的工作日和周末
# workday = ['03','04','05','06','07','10','11','12','13','14','17','18','19','20','21','24','25','26','27','28','31'] #日期
# weekday = ['01','02','08','09','15','16','22','23','29','30']
#
# hour = ['07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22'] # 小时
# frames = []
# for i in workday:
#     for j in hour:
#         df1 = (df['2017-07-'+i+' '+j])
#         frames.append(df1)
# df2 = pd.concat(frames)
# df2.to_csv("E:\\datasets\\stationFlow\\sjzc07",header = 0,encoding = 'utf-8')


# -----------------------------------------------------------------------------------------------
##  过滤需要的记录---new


## 提取时段，工作日/周末，节假日


# path = 'E:\\datasets\\stationFlow\\allstation'
# dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
# df = pd.read_csv(path,engine='python',header=None,names=['time','name','inflow','outflow'],encoding='utf-8',parse_dates=['time'],date_parser=dateparse)
#
# df['year'] = df['time'].apply(lambda x:x.year)
# df['month'] = df['time'].apply(lambda x: x.month)
# df['day'] = df['time'].apply(lambda x: x.day)
# df['hour'] = df['time'].apply(lambda x:x.hour)
# df['weekday'] = df['time'].apply(lambda x: x.weekday()+1) #x.weekday()返回日期的星期(0-6),周一为0
# ## 取出每天7点到22点时间段
# df = df[(df['hour']<=22) & (df['hour']>=7)]
#将中间结果保存一下
# df.to_csv("E:\\datasets\\stationFlow\\midResult",header=0,index=0,encoding='utf-8')

#---------------------------------------------------------
# df = pd.read_csv('E:\\datasets\\stationFlow\\midResult',names=['time','name','inflow','outflow','year','month','day','hour','weekday'])
#
# ## 过滤2017年的
# df = df[(df['year'] ==2017)]
#
#
# # 工作日与休息日,分别用0，1表示
# isrest = ((df['weekday'] == 6) | (df['weekday'] == 7)) # 返回bool值
# df['label'] = isrest*1
#
# # label=2表示节假日
# # holiday = [] #['06-01']
# # for h in holiday:
# #     #h = '01-01'
# #     h_month,h_day = h.split('-')
# #     h_index = ((df['month'] == int(h_month)) & (df['day'] == int(h_day)))
# #     df.loc[h_index, 'label'] = 2
#
# ## 过滤6、7月份工作日
# df = df[(((df['month']==6) | (df['month']==7)) & (df['label']==0))]
#
#
# ##站点
# station = df[df["name"] == "世界之窗"]
# # station.to_csv("E:\\datasets\\stationFlow\\bj_0607",header=0,index=0,encoding='utf-8',columns=['time','name','inflow','outflow'])
#
# ## 线路
# # 提取线路需要先将date转化成相同的区间
# #读取静态数据
# staticPath = 'E:\\datasets\\stationFlow\\subway_zdbm_station_new'
# df1 = pd.read_csv(staticPath,names=['stationID','stationName','lineID','lineName','lat','lon'],encoding='utf-8')
#
# line =df1[df1['lineName'] =='地铁一号线']
# line = line.sort_values(by='stationID')
# name = np.array(line['stationName'])
#
# sta0 = df[df['name'] == name[0]].iloc[:,[0,2]]
# sta1 = df[df['name'] == name[1]].iloc[:,2]
# # sta2 = df[df['name'] == name[2]].iloc[:,[0,2]]
# # sta0 = pd.merge(sta0,sta2,how='inner',on='time')
# # sta0 = pd.concat([sta0,sta1],axis=1,ignore_index=True)
# sta0 = sta0.join(sta1,on='time')
# for i in range(1,len(name)):
#     sta1 = df[df['name'] == name[i]].iloc[:,[0,2]]
#     sta0 = pd.merge(sta0,sta1,how='inner',on='time')
#
# sta0.to_csv("E:\\datasets\\stationFlow\\line\\line2_0607",header=0,index=0,encoding='utf-8')


#---------------------------------------------------------------------------------
# 按天统计世界之窗的客流,并结合天气数据
df = pd.read_csv('E:\\datasets\\stationFlow\\midResult',names=['time','name','inflow','outflow','year','month','day','hour','weekday'])
df = df[(df['year'] ==2017)]
df = df[df["name"] == "世界之窗"]
df = df.groupby(by=['month','day'])['outflow'].sum()
df = pd.DataFrame(df)

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
df1 = pd.read_csv('E:\MyProject_sibat\Python\PaChong\crawle_weather\shenzhen201701-201712',parse_dates=['data'],date_parser=dateparse)

df1['year'] = df1['data'].apply(lambda x:x.year)
df1['month'] = df1['data'].apply(lambda x: x.month)
df1['day'] = df1['data'].apply(lambda x: x.day)

df2 = pd.merge(df,df1,how='inner',on=['month','day'])

df2.to_csv("C:\\Users\\will\\Desktop\\weatherOutflow",header=0,index=0,columns = ['data','high','low','weather','winddirect','outflow'])