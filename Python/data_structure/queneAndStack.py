from collections import deque

# 栈可以用一个数组来代替实现  先进后出
stack = [3,4,5]
stack.append(6)
stack.pop()

# # 队列需要导入单独的包 先进先出，队尾进队头出
queue = deque(['a','b','c'])
queue.extend(['d'])
queue.append('d')
queue.appendleft('1')
queue.popleft()
queue.pop(0)
queue_len = len(queue)


## 两个堆栈实现一个队列：队尾插入和队头删除操作
class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self,node):
        self.stack1.append(node)

    def deleteHead(self):
        if self.stack2: # 如果stack2不为空，则弹出
            return self.stack2.pop()
        elif not self.stack1:  # 如果stack1为空
            return None
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

## 两个队列实现一个栈：
class Stack():
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
    def push(self,node):
        self.queue1.append(node)
    def pop(self):
        if not self.queue1: ## 如果quene1为空
            return None
        else:
            while len(self.queue1) !=1:
                self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1 # 至关重要的一步！ 为了pop下一个元素做准备
        return self.queue2.pop()

if __name__ == '__main__':
    testList = list(range(5))
    print(testList)
    # 测试堆栈实现队列
    testQueue = Queue()
    for i in range(5):
        testQueue.appendTail(testList[i])
    for i in range(5):
        print(testQueue.deleteHead(),'', end='')
    print('\n')

    ## 测试队列实现堆栈
    testStack = Stack()
    for i in range(5):
        testStack.push(testList[i])
    for i in range(5):
        print(testStack.pop(),'',end='')

