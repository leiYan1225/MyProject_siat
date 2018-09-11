import os
da = '20180715'

path = 'F:\\20180709_15\\'
filelist=os.listdir(path+da)


newfile=open('F:\\data\\'+da,'w',encoding='utf-8')
for item in filelist:
    for txt in open(path+da+'\\'+item,'r',encoding='utf-8'):
        newfile.write(txt)

newfile.close()