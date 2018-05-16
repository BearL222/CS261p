from AVLNode import *


class AVLTree:
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
            self.root = AVLNode(k, None)
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
                parent.leftChild = AVLNode(k, parent)
            else:
                parent.rightChild = AVLNode(k, parent)

        # rebalance

    def ll(self, k2):
        k1 = k2.leftChild
        k2.leftChild = k1.rightChild
        k1.rightChild = k2

        k2.height = max(k2.leftChild.height, k2.rightChild.height) + 1
        k1.height = max(k1.leftChild.height, k1.rightChild.height) + 1

    def rr(self, k1):
        k2 = k1.rightChild
        k1.rightChild = k2.leftChild
        k2.leftChild = k1

        k1.height = max(k1.leftChild.height, k1.rightChild.height) + 1
        k2.height = max(k2.leftChild.height, k2.rightChild.height) + 1