
# 1
# 3 5
# 1 2 5
# output: 4
# 零钱兑换：
#----输入
# 组数
# 零钱种类数 总钱数
# 零钱种类(比如有1 2 5 三种类型的零钱)
#----输出
# 几种兑换方式

import sys
# case situation:10%   Not meeting the requirements of time
if __name__ == "__main__":
    # t = int(sys.stdin.readline().strip())
    # if t >100 and t < 0:   #  0 <= t <=100
    #     sys.exit()
    num_kind = 3
    money = 5
    coins = [1,2,5]
    # for i in range(t):
    #     line1 = sys.stdin.readline().strip()
    #     line2 = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     line = list(map(int, line1.split()))
    #     num_kind = line[0]
    #     money = line[1]
    #     coins = list(map(int, line2.split()))

    output = [0] * (money + 1)
    output[0]=1
    if money ==0:
        print(0)
    for i in range(len(coins)):
        for j in range(coins[i],money+1):
            output[j]=output[j]+output[j-coins[i]]
    print(output[money])





