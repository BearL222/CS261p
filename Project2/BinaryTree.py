from BTNode import *


class BinaryTree:
    root = None
    empty = True

    def __init__(self):
        self.empty = True

    def search(self, k):
        if self.empty:
            return None

        node = self.root
        while node is not None:
            if k < node.value:
                node = node.leftChild
            elif k > node.value:
                node = node.rightChild
            else:
                return node
        return None

    def insert(self, k):
        if self.empty:
            self.empty = False
            self.root = BTNode(k)
        else:
            node = self.root
            parent = None
            lor = 0
            while node is not None:
                if k < node.value:
                    parent = node
                    lor = 0
                    node = node.leftChild
                elif k > node.value:
                    parent = node
                    lor = 1
                    node = node.rightChild
                else:
                    return
            if lor == 0:
                parent.leftChild = BTNode(k)
            else:
                parent.rightChild = BTNode(k)

    def delete(self, k):
        if self.search(k) is not None:
            node = None
