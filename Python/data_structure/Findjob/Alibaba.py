


import sys

row = int(sys.stdin.readline().strip())
col = int(sys.stdin.readline().strip())
list1 = [[0] * col] * row
for i in range(row):
    li2 = sys.stdin.readline().strip()
    line = list(map(int, li2.split()))
    for j in range(col):
        list1[i][j] = line[j]

def find_martrix_min_value(data_matrix):
    new_data = []
    for i in range(len(data_matrix)):
        new_data.append(min(data_matrix[i]))
    print(min(new_data))


def find_martrix_max_value(data_matrix):
    new_data = []
    for i in range(len(data_matrix)):
        new_data.append(max(data_matrix[i]))
    print(max(new_data))

find_martrix_max_value(list1)
find_martrix_min_value(list1)