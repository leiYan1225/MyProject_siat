'''
如果涉及到海量数据的处理，一般步骤是：

1. 分而治之/hash 映射，即将大文件中的元素根据hash 值分解到n个小文件，确保相同的元素分到一个小文件中，再统计小文件中的次数做多的值（选取合适的hash 函数是关键，尽量hash完后分布均匀）
2. 放到hash_map(即dict 中)进行统计，key 为字符串，value 为出现的次数
3. 采用排序算法排序（堆排序：升序采用max 堆，降序采用min 堆）

'''

arr1 = [1,2,3,3,5,6,2,7,4,5,6,3,3,4,5,4,5,4,5,3,2,5,8,7]  #假设有10亿条...


# 用hash_map(字典)统计出现的数字，key是元素，value是出现次数
dic1 = {}
for i in range(len(arr1)):
    if arr1[i] not in dic1.keys():  # 如果str不在keys中，则将str加入字典，并将对应value 设置为1
        dic1[arr1[i]] = 1
    else:                       #如果在keys中，将value+1
        dic1[arr1[i]]+=1

print(dic1.values())


# 通过堆排序对统计后的次数进行排序

# 堆排序
# 大顶堆：arr[i] >= arr[2i+1] && arr[i] >= arr[2i+2]  小顶堆：arr[i] <= arr[2i+1] && arr[i] <= arr[2i+2]
# 完全二叉树、 min 堆


'''
借助堆这个数据结构，找出Top K，时间复杂度为N‘logK。
即借助堆结构，我们可以在log量级的时间内查找和调整/移动。因此，维护一个K(该题目中是10)大小的小根堆，然后遍历300万的Query，分别和根元素进行对比。
所以，我们最终的时间复杂度是：O(n) + N' * O(logk），其中，N为1000万，N’为300万
'''

def MAX_Heapify(heap,HeapSize,root):#在堆中做结构调整使得父节点的值大于子节点

    left = 2*root + 1
    right = 2*root + 2
    larger = root
    if left < HeapSize and heap[larger] < heap[left]:  ## left,right < HeapSize 是递归出口
        larger = left
    if right < HeapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:#如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        heap[larger],heap[root] = heap[root],heap[larger]
        MAX_Heapify(heap, HeapSize, larger)    #对其子节点递归执行

def Build_MAX_Heap(heap):#构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)#将堆的长度当独拿出来方便
    for i in range((HeapSize//2-1),-1,-1):#从后往前出数  (HeapSize//2-1)表示取第一个非叶子节点
        MAX_Heapify(heap,HeapSize,i)

def HeapSort(heap):#将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    Build_MAX_Heap(heap)
    for i in range(len(heap)-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        MAX_Heapify(heap, i, 0)
    return heap

if __name__ == '__main__':
    a = [30,50,57,77,62,78,94,80,84]
    print(a)
    HeapSort(a)
    print(a)
    # b = [random.randint(1,1000) for i in range(1000)]
    # print(b)
    # HeapSort(b)
    # print(b)