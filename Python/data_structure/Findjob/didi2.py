import sys


def findMaximumXOR(nums):
    answer = 0
    for i in range(31,-1,-1):
        answer <<= 1
        prefixes = {num >> i for num in nums}
        answer += any(answer^1 ^ p in prefixes for p in prefixes)
    return answer

# n = 4
# num = [2,3,5,7]
# n = int(input())
# line = sys.stdin.readline().split()
# num = list(map(int,line))
# result = 0
# if n <= 6:




print(findMaximumXOR([3,11,9,5]))

# for i in range(4,-1,-1):
#     print(i)
