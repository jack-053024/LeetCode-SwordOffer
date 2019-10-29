class Node(object):
    '''二叉树节点'''
    def __init__(self, item):
        # 节点元素
        self.elem = item
        # 左子节点
        self.lchild = None
        # 右子节点
        self.rchild = None


class BinaryTree(object):
    '''二叉树'''
    def __init__(self):
        self.root = None

    def add(self, item):
        # 构造节点
        node = Node(item)
        # 特殊情况，如果根节点就是None，则直接将新节点挂载到根节点上
        if self.root is None:
            self.root = node
            return
        # 使用广度优先遍历，也叫层次遍历找到None节点以供插入
        # 1.先用列表定义一个空队列，并先将根节点加入
        queue = [self.root]
        # 2.如果节点不为None，则append入队列，如果为None，则直接将新节点挂上
        while True:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_first_traversal(self):
        '''广度优先遍历--层次遍历'''
        # 定义一个队列，把根节点先加入
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=' ')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder_traversal(self, node):
        '''深度优先遍历之先序遍历'''
        if node == None:
            return
        print(node.elem, end=' ')
        self.preorder_traversal(node.lchild)
        self.preorder_traversal(node.rchild)

    def in_order_traversal(self, node):
        '''深度遍历之中序遍历'''
        if node == None:
            return
        self.in_order_traversal(node.lchild)
        print(node.elem, end=' ')
        self.in_order_traversal(node.rchild)

    def post_order_traversal(self, node):
        '''深度遍历之后序遍历'''
        if node == None:
            return
        self.post_order_traversal(node.lchild)
        self.post_order_traversal(node.rchild)
        print(node.elem, end=' ')


if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(10):
        tree.add(i)
    tree.breadth_first_traversal()

    print()
    tree.preorder_traversal(tree.root)
    print()
    tree.in_order_traversal(tree.root)
    print()
    tree.post_order_traversal(tree.root)




















