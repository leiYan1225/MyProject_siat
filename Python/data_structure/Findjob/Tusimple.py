# 图森未来
# 描述：
# 实现 LFU 缓存算法，可以在缓存元素数量超过最大容量的时候删除访问次数最少的数据。
#
# 具体要求：
# 设计一个类 LFUCache，实现下面三个函数：
#     + 构造函数: 传入 Cache 内最多能存储的 key 的数量
#     + get(key)：如果 Cache 中存在该 key，则返回对应的 value 值，否则，返回-1。
#     + set(key,value)：如果 Cache 中存在该 key，则重置 value 值；如果不存在该 key，则将该 key 插入到到 Cache 中，若插入后会导致 Cache 中存储的 key 个数超过最大容量，则在插入前淘汰访问次数最少的数据。
#
# 提示：
# 访问次数：每次get/set一个存在的key都算作对该key的一次访问；当某个key被淘汰的时候，访问次数清零。
# 所有 key 和 value 都是 int 类型。


## 当场写，未实现。。。
# class LFUCache():
#     flag = 1
#     dic1 = []
#
#     def __init__(self, val, dic):
#         n = val  ## 容量
#         cache = dic  ## Cache 中存的k,v
#
#     def get(self, key):
#         if self.cache.haskey(key):
#             return self.cache[key]
#         else:
#             return -1
#
#     def set(self, key, value):
#         self.cache[key] = value
#
#         @property dic1
#         dic1[key] = 1
#         m = 0
#         if get(key) != -1:
#             m += 1
#         else:
#         flag = 0
#         if len(self.cache) > self.n:
#
#
# def main():
#     dic = {1: 1, 2: 2, 3: 2}
#     cache1 = LFUCache(5, dic)