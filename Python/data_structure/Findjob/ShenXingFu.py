import sys


def isRabbit(list1):
    flag = 'Yes'
    for i in range(len(list1) - 1):
        if list1[i] == 0 and list1[i + 1] == 0:
            flag = 'No'
    return flag

if __name__ == '__main__':
    line = sys.stdin.readline().split()  # line[0]、line[1] 分别表示洞的个数和天数
    day = sys.stdin.readline().split()

    line = list(map(int, line))
    day = list(map(int, day))

    k = line[0]
    list1 = [0] * k
    for i in day:
        list1[i - 1] = 1

    print(isRabbit(list1))




# import sys
#
#
# def isRabbit(list1):
#     flag = 'Yes'
#     for i in range(len(list1) - 1):
#         if list1[i] == 0 and list1[i + 1] == 0:
#             flag = 'No'
#     return flag
#
# if __name__ == '__main__':
#     line = sys.stdin.readline().split()  # line[0]、line[1] 分别表示洞的个数和天数
#     day = sys.stdin.readline().split()
#
#     line = list(map(int, line))
#     day = list(map(int, day))
#
#     if line[0] <= 1000 and line[1] <= 1000 and len(day) == line[1]:
#         k = line[0]
#         list1 = [0] * k
#         for i in day:
#             list1[i - 1] = 1
#
#         print(isRabbit(list1))


