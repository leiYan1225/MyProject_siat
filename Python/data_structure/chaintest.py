class Node:
    def __init__(self, data):
        """
        node的初始化
        :param data: 节点的数据
        """
        self.data = data
        self.pnext = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        """
        Linked list 的初始化
        """
        self.length = 0
        self.head = None

    def is_empty(self):
        """
        判断该链表是否为空
        :return: boolean
        """
        return self.length == 0

    def append(self, this_node):
        """
        在链表末添加node/值,如果是node对象直接添加，否则先转换为node对象
        :param this_node: 数据或者node对象
        :return: None
        """
        if isinstance(this_node, Node):
            pass
        else:
            this_node = Node(data=this_node) #如果为数值对象则将该数值对象赋值给node 的data
        if self.is_empty():
            # 链表为空的情况将头指针指向当前node
            self.head = this_node
        else:
            node = self.head
            while node.pnext:
                node = node.pnext #遍历链表
            node.pnext = this_node
        self.length += 1 # 链表长度 +1

    def insert(self, value, index):
        """
        链表的插入操作
        :param value: 要插入的值
        :param index: 位置
        :return: None
        """
        if type(index) is int:
            if index > self.length:
                # 索引值超出范围直接提示并且退出
                print("Index value is out of range.")
                return
            else:
                # 获得当前node对象和head
                this_node = Node(data=value)
                current_node = self.head

                if index == 0:
                    # 索引值为0表示将该node 插入到链表头
                    self.head = this_node
                    this_node.pnext = current_node
                    return

                while index - 1:
                    current_node = current_node.pnext #将当前节点移到要插入位置的上一个节点
                    index -= 1

                # 这两条语句顺序很关键
                # 将当前节点与后一个节点拆开，this_node指向后一个节点，前一个节点指向this_node
                this_node.pnext = current_node.pnext
                current_node.pnext = this_node
                self.length += 1
                return

        else:
            print("Index value is not int.")
            return

    def delete(self, index):
        """
        删除链表中某个位置的节点
        :param index: 位置索引
        :return: None
        """
        if type(index) is int:
            if index > self.length:
                # 索引值超出范围直接提示并且退出
                print("Index  is out of range.")
                return
            else:
                if index == 0:
                    #如果删除的节点为表头节点，则将表头的next重新设置为表头
                    self.head = self.head.pnext
                else:
                    current_node = self.head
                    while index - 1:
                        current_node = current_node.pnext
                        index -= 1
                    current_node.pnext = current_node.pnext.pnext
                    self.length -= 1
                    return
        else:
            print("Index value is not int.")
            return

    def update(self, value, index):
        """
        为链表中某个位置的节点修改值
        :param value: 要修改的值
        :param index: 位置索引
        :return: None
        """
        if type(index) is int:
            if index > self.length:
                # 索引值超出范围直接提示并且退出
                print("Index  is out of range.")
                return
            else:
                this_node = Node(data=value)
                if index == 0:
                    this_node.pnext = self.head.pnext
                    self.head = this_node
                else:
                    current_node = self.head
                    while index - 1:
                        current_node = current_node.pnext
                        index -= 1
                    this_node.pnext = current_node.pnext.pnext
                    current_node.pnext = this_node
                    return
        else:
            print("Index value is not int.")
            return

    def get_value(self, index):
        """
        获取链表中某个位置节点的值
        :param index: 位置索引
        :return: 该节点值, int or not
        """
        if type(index) is int:
            if index > self.length:
                # 索引值超出范围直接提示并且退出
                print("Index  is out of range.")
                return
            else:
                if index == 0:
                    return self.head.data
                else:
                    current_node = self.head
                    while index - 1:
                        current_node = current_node.pnext
                        index -= 1
                    return current_node.pnext.data
        else:
            print("Index value is not int.")
            return

    def reverse(self):
        """
            反转链表 By will
            :return:
            """
        # 前三行表示将原链表的第一个节点变成了新链表的最后一个节点，同时将原链表的第二个节点保存在cur中
        pre = self.head  # 取出头节点（第一个节点）
        current_node = pre.pnext
        pre.pnext = None

        # 从第二个节点开始遍历，将所有节点都翻转一遍
        while current_node: # 直到cur 为空，跳出循环
            temp = current_node.pnext  # 将cur的下一个节点保存在temp中，即第三个节点，因为反转后节点2找不到节点3了，所以需要保存
            current_node.pnext = pre # 将节点2的下一个节点指向节点1
            pre = current_node # pre 向后移动到cur的位置
            current_node = temp # cur也向后移动一位
        self.head = pre #将头节点设置为pre
        return

    def get_length(self):
        """
        获取链表长度
        :return: int
        """
        current_node = self.head
        if current_node:
            i = 1
            while current_node.pnext:
                current_node = current_node.pnext
                i += 1
            return i
        else:
            return 0

    def clear(self):
        """
        清空链表
        :return: None
        """
        self.head = None
        self.length = 0
        print("Clear the linked list finished.")

    def print_linked_list(self):
        """
        对整个链表的打印
        :return: None
        """
        if self.is_empty():
            print("Linked list's length is 0")
        else:
            node = self.head
            print("Head -->", node.data, end=' ')
            while node.pnext:
                node = node.pnext
                print("-->", node.data, end=' ')
            print("--> None. Linked node finished")


if __name__ == '__main__':
    node1 = Node(data='node1')
    node2 = Node(data='node2')
    linked_list = LinkedList()
    linked_list.append(node1)
    linked_list.append(node2)
    linked_list.print_linked_list()
    linked_list.insert("sdf", 1)
    linked_list.print_linked_list()
    # linked_list.delete(0)
    # linked_list.print_linked_list()
    linked_list.update(value="update_test", index=2)
    linked_list.print_linked_list()
    linked_list.reverse()
    linked_list.print_linked_list()
    print(linked_list.get_value(index=2))
    print(linked_list.get_length())
