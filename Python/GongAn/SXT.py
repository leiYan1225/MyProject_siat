
import pandas as pd

df = pd.read_excel('XH_CAMERAINFO.xls')

station_name = []
banqiu = []
guding = []
qiuji = []

data = [[]]

for name, group in df.groupby("USE_PROJECT_DESC"):
    # list1 = list(group["ID"])
    print(name)
    # print(len(list1))
    for name1,group1 in group.groupby("CAMERATYPEDESC"):
        list2 = list(group1["ID"])
        print(name1)
        # print(len(list2))
        for name2,group2 in group1.groupby("LINE_STATION"):
            list3 = list(group2["ID"])
            print(name2+','+str(len(list3)))
        print('\n')



