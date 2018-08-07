
# 堆排序
# 由输入的无序数组构造一个最大堆，作为初始的无序区
# 把堆顶元素（最大值）和堆尾元素互换
# 把堆（无序区）的尺寸缩小1，并调用heapify(A, 0)从新的堆顶元素开始进行堆调整
# 重复步骤2，直到堆的尺寸为1


# 堆排序
# 大顶堆：arr[i] >= arr[2i+1] && arr[i] >= arr[2i+2]  小顶堆：arr[i] <= arr[2i+1] && arr[i] <= arr[2i+2]
# 完全二叉树、 min 堆



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