import xlrd
import pandas as pd

data = xlrd.open_workbook('C:/Users/will/Desktop/XH_CAMERAINFO.xls')#打开Excel文件读取数据
sh = data.sheets()[0]
arr = []
for n in range(sh.nrows):
    arr.append(sh.row_values(n))

df = pd.DataFrame(arr[1:], columns=arr[0])  # 取出第一行当作字段
df.to_csv('XH_CAMERAINFO', index=None, encoding='utf-8')
