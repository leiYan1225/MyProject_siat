import pandas as pd
import numpy as np
import matplotlib.pylab as plt
plt.rcParams['figure.figsize'] = 15, 6


#### 如果运行不了，可以考虑放到console 中跑
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')
#---其中parse_dates 表明选择数据中的哪个column作为date-time信息，
#---index_col 告诉pandas以哪个column作为 index
#--- date_parser 使用一个function(本文用lambda表达式代替)，使一个string转换为一个datetime变量
data = pd.read_csv('E:\\datasets\\stationFlow\\sjzc0607_workday',header=None,names=['time','name','inflow','outflow'],parse_dates=['time'],
                   index_col='time',date_parser=dateparse)
print (data.head)
print (data.index)


from statsmodels.tsa.stattools import adfuller
def test_stationarity(timeseries):
    # 滑动窗口，这里以一个月为一个窗口，每一个时间t的值由它前面12（包括自己）的均值代替，标准差同理。
    rolmean = pd.rolling_mean(timeseries, window=193)
    rolstd = pd.rolling_std(timeseries, window=193)

    # plot rolling statistics:
    fig = plt.figure()
    fig.add_subplot()
    orig = plt.plot(timeseries, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='rolling mean')
    std = plt.plot(rolstd, color='black', label='Rolling standard deviation')

    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)

    # Dickey-Fuller test:

    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    # dftest的输出前一项依次为检测值，p值，滞后数，使用的观测数，各个置信度下的临界值
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical value (%s)' % key] = value
    print(dfoutput)

data = data['inflow']
test_stationarity(data)