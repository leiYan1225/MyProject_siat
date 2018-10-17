'''
[1531324800][login],{"roleid":"1"}
[1531364400][login],{"roleid":"2"}
[1531368000][logout],{"roleid":"1"}
[1531371600][other],{"roldid":"2"}
[1531371600][logout],{"roleid":"2"}
[1531371540][login],{"roleid":"3"}
[1531375200][logout],{"roleid":"3"}

'''

import sys
data = []
while True:
    log = {}
    line = sys.stdin.readline().strip()
    if line == '':
        break
    tmp = []
    time = line[1:11]
    a = line.rfind("]")
    statue = line[13:a]
    b = line.rfind(":")
    roleid = line[b+2:-2]
    if statue == "login" or statue =="logout":
        log["id"] = roleid
        log["statue"] = statue
        log["time"] = time
        data.append(log)


data.sort(key=lambda k: (k.get('time', 0)))
diff = 0
one,two = '',''
i = 0
while i<len(data)-2:

    first = data[i]["id"]

    if data[i+1]["id"] != first:
        second = data[i+1]["id"]
        time1 = data[i+1]["time"]
        for j in range(i+2,len(data)):
            if data[j]["id"] ==first or data[j]["id"] ==second:
                tmp = int(data[j]["time"])-int(time1)
                if tmp>diff:
                    diff = tmp
                    one = first
                    two = second
    else:
        i+=1
    i+=1

print(one)
print(two)



# df = pd.DataFrame(log, columns=['time', 'statue', 'id'])
#
#
# for name, group in df.groupby("id"):
#     print(name)
#     df["diff"] =



