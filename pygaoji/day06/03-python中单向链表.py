class SingleNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    def __init__(self, node=None):
        self.head = node

    def is_empty(self):
        return self.head is None

    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.head
        while cur is not None:
            print(cur.item, end=' ')
            cur = cur.next

    def add(self, item):
        new_node = SingleNode(item)
        new_node.next = self.head
        self.head = new_node

    def append(self, item):
        cur = self.head
        new_node = SingleNode(item)
        if self.is_empty():
            self.head = new_node
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node

    def insert(self, pos, item):
        new_node = SingleNode(item)
        if pos <= 0:
            self.add(new_node)
        elif pos >= self.length():
            self.append(new_node)
        else:
            cur = self.head
            count = 0
            while count < pos:
                cur = cur.next
                count += 1
            new_node.next = cur.next
            cur.next = new_node



    def remove(self, item):
        cur = self.head
        pre = None
        while cur is not None:
            if cur.item == item:
                if self.head.item == item:
                    self.head = self.head.next
                else:
                    pre.next = cur.next
                return
            pre = cur
            cur = cur.next

    def search(self, item):
        cur = self.head
        while cur is not None:
            if cur.item == item:
                print('找到')
                return True

            cur = cur.next
        print('没找到')
        return False

if __name__ == '__main__':
    single_link_list = SingleLinkList()
    print(single_link_list.is_empty())
    single_link_list.add(1)
    single_link_list.add(2)
    single_link_list.add(3)
    single_link_list.add(4)
    # single_link_list.travel()
    single_link_list.length()
    single_link_list.append(5)
    # single_link_list.travel()
    single_link_list.insert(2, 6)
    single_link_list.travel()
    single_link_list.remove(6)
    print('-----------------')
    single_link_list.travel()
    single_link_list.search(6)
    single_link_list.search(5)
