
#  最大子数组问题暴力求解
def find_key(dict):
    new_keylist=[]
    b=max(dict,key=dict.get)  # 找出dict中的值最大值所对应的关键字（这里表示最大子数组）
    # print (dict[b])
    for key in dict:
        if dict[key]== dict[b]:
            new_keylist.append(key)  # 可能存在多个最大子数组的情况
    return new_keylist

#
# # a=[100,113,110,85, 105,102,86, 63, 81, 101, 94, 106, 101 ,79, 94, 90, 97]  # 原始数据
# # b  =[]
# # for i in range(1,len(a)):
# #     b.append(a[i]-a[i-1]) # 增量数组 print (b)
# b = [6, -3, 1, -2, 7, -15, 1, 2, 2]
# new=[]
# d={}
# for i in range (0,len(b)): # 子数组长度为i
#     for j in range(0,len(b)-i):
#         key= sum(b[j:1+j+i])
#         new= tuple (b[j:1+j+i])
#         d[new] = key
# v=list(d.values())
# print(d)
# print(v)
#
# tmp = find_key(d)
# print(tmp)
# print(d[tmp[0]])


'''
思路：
最大和连续子数组一定有如下几个特点：
1、第一个不为负数
2、如果前面数的累加值加上当前数后的值会比当前数小，说明累计值对整体和是有害的；
如果前面数的累加值加上当前数后的值比当前数大或者等于，则说明累计值对整体和是有益的。

步骤：
1、定义两个变量，一个用来存储之前的累加值，一个用来存储当前的最大和。遍历数组中的每个元素，假设遍历到第i个数时：
①如果前面的累加值为负数或者等于0，那对累加值清0重新累加，把当前的第i个数的值赋给累加值。
②如果前面的累加值为整数，那么继续累加，即之前的累加值加上当前第i个数的值作为新的累加值。
2、判断累加值是否大于最大值：如果大于最大值，则最大和更新；否则，继续保留之前的最大和

'''

def function(lists):
    max_sum = lists[0]
    pre_sum = 0
    a,b = 0,len(lists)-1
    for i in range(len(lists)):
        if pre_sum > 0:
            pre_sum += lists[i]
        else:
            pre_sum = lists[i]
            a = i
        if pre_sum > max_sum:
            max_sum = pre_sum
            b = i

    return max_sum,a,b


def main():
    arr1 = [10,9,7,11,8,9,7,14,-1,0,2,4]
    lists = [-1,-2,4,-3, 1,-2,7,-15,1,2,2]
    result,begin,end= function(lists)
    print(begin,end)
    print(result)


if __name__ == "__main__":
    main()


def delLink(linkedlist):
    if node ==None or node.next ==None:
        return node
