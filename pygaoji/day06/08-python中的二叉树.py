class Node(object):
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None


class BinaryTree(object):
    def __init__(self, node=None):
        self.root = node

    def add(self, item):
        if self.root == None:
            self.root = Node(item)
            return

        quene = []
        quene.append(self.root)
        while True:
            node = quene.pop(0)
            if node.lchild == None:
                node.lchild = Node(item)
                return
            else:
                quene.append(node.lchild)
            if node.rchild == None:
                node.rchild = Node(item)
                return
            else:
                quene.append(node.rchild)

    def breath_travel(self):
        if self.root == None:
            return
        quene = []
        quene.append(self.root)
        while len(quene) > 0:
            node = quene.pop(0)
            print(node.item, end=' ')
            if node.lchild != None:
                quene.append(node.lchild)
            if node.rchild != None:
                quene.append(node.rchild)



    def preorder_travel(self, node):
        if node is not None:
            print(node.item, end=' ')
            self.preorder_travel(node.lchild)
            self.preorder_travel(node.rchild)

    def inorder_travel(self, node):
        if node is not None:
            self.inorder_travel(node.lchild)
            print(node.item, end=' ')
            self.inorder_travel(node.rchild)

    def postorder_travel(self, node):
        if node is not None:
            self.postorder_travel(node.lchild)
            self.postorder_travel(node.rchild)
            print(node.item, end=' ')




if __name__ == '__main__':
    bt = BinaryTree()
    for i in range(10):
        bt.add(i)
    bt.breath_travel()
    print('-----------------')
    bt.preorder_travel(bt.root)
    print('-----------------')
    bt.inorder_travel(bt.root)
    print('-----------------')
    bt.postorder_travel(bt.root)
