
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from operator import itemgetter
from itertools import groupby
from numpy import mean, ptp, var, std,max

def percent01(a):
    return  np.percentile(a,95)#95%分位数
def calTimeDiff(path,lst,num):
    with open(path,"r",encoding='gbk', errors='ignore')  as f:
        for line in f:
            num = num+1
            if num > 1:
                s_line = line.split(',')
                number = s_line[0]
                first_time = s_line[2]
                last_time = s_line[12]
                last_time = time.mktime(time.strptime(last_time,"%Y-%m-%d %H:%M:%S\n"))
                first_time = time.mktime(time.strptime(first_time,"%Y_%m_%d_%H_%M_%S"))
                xL.append(num-2)
                lst.append(last_time-first_time)

        return lst

def calTime(time1,time2):
    first_time = time.mktime(time.strptime(time1, "%Y_%m_%d_%H_%M_%S"))
    last_time = time.mktime(time.strptime(time2, "%Y-%m-%d %H:%M:%S"))
    return (last_time-first_time)

def cal_std(df):
  for ix,row in df.iterrows():
    std = row.std()
    df.loc[ix,"std"] = std
  return df



if __name__ == '__main__':
    xL = []
    num = 0
    N = 0
    lst = np.zeros((9, 9))
    mean_list = []
    std_list = []
    names = []
    path = "20180426"
    df = pd.read_csv(path, encoding="utf-8", sep=',',
                     names=["a", "b", "time1", "d", "e", "f", "g", "h", "i", "j", "k", "l", "time2"])
    df["timeDiff"] = df.apply(lambda x: calTime(x[2], x[12]), axis=1)

    # plt.figure()
    # plt.plot(df["timeDiff"])
    # plt.show()
    # print(mean(list(df["timeDiff"])))
    for name, group in df.groupby("a"):
        list1 = list(group["timeDiff"])
        # print("编号：")
        # print(name)
        # print("均值：")
        # print(mean(list1))
        # print("标准差")
        # print(std(list1))
        names.append(name)
        mean_list.append(mean(list1))
        std_list.append(std(list1))
    for i in range(len(mean_list)):
        lst[i] = np.random.normal(loc=mean_list[i], scale=std_list[i], size=9)

    print(lst)
    plt.boxplot(lst, labels=names)
    plt.show()
