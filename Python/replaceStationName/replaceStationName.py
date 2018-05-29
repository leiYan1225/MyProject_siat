
import xlrd
import pandas as pd
import csv
import re

def csv2dict(path):
    dict_club={}
    # with 语句适用于对资源进行访问时使用，不管使用过程中是否发生异常都会进行“清理”操作，释放资源，
    # 比如文件使用后自动关闭、线程中锁的自动获取和释放等
    with open(path,"r",encoding='UTF-8') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            dict_club[row[1]]=row[0]
        return dict_club

def name2id(table):
    nrows = table.nrows
    ncols = table.ncols
    for index in range(5, nrows):
        lines = table.row_values(index)
        str1 = str(lines[6])[:-3] # 最后三个字符，即去除”地铁站“
        return dict[str1]



if __name__ == '__main__':
    path_station = "F://MyProject_sibat//Python//replaceStationName//datasets//station.csv"
    path_file = "F://MyProject_sibat//Python//replaceStationName//datasets//test.xlsx"

    wb = xlrd.open_workbook(path_file)
    dict = csv2dict(path_station)
    nsheets = wb.nsheets

    for i in range(nsheets):
        sheet = wb.sheet_by_index(i)
        print(name2id(sheet))


    # if re.match("罗湖","罗湖地铁站"):
    #     print("1")

## 5号线总信息表20180425.xlsx 这个表中各个sheet数据不统一，stationName不全在第6列，
        # 以及stationName 字段有的为 "布吉站"，"香蜜湖地铁站"