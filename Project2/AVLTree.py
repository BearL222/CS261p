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
        self.inserting(self.root, k)

    def inserting(self, node, k):
        if node is None:
            node = AVLNode(k)
        elif k < node.value:
            node.leftChild = self.inserting(node.leftChild, k)
            if self.height(node.leftChild) == self.height(node.right) + 2:
                if k < node.leftChild.value:
                    node = self.ll(node)
                else:
                    node = self.lr(node)
        elif k > node.value:
            node.rightChild = self.inserting(node.right, k)
            if self.height(node.rightChild) == self.height(node.leftChild) + 2:
                if k > node.rightChild.value:
                    node = self.rr(node)
                else:
                    node = self.rl(node)
        else:
            node = node
        node.height = max(self.height(node.leftChild), self.height(node.rightChild)) + 1
        return node

    def height(self, node):
        return node.height if node is not None else 0

    def ll(self, k2):
        k1 = k2.leftChild
        k2.leftChild = k1.rightChild
        k1.rightChild = k2
        k2.height = max(self.height(k2.leftChild), self.height(k2.rightChild)) + 1
        k1.height = max(self.height(k1.leftChild), self.height(k1.rightChild)) + 1
        return k1

    def rr(self, k1):
        k2 = k1.rightChild
        k1.rightChild = k2.leftChild
        k2.leftChild = k1
        k1.height = max(self.height(k1.leftChild), self.height(k1.rightChild)) + 1
        k2.height = max(self.height(k2.leftChild), self.height(k2.rightChild)) + 1
        return k2

    def lr(self, k3):
        k3.leftChild = self.rr(k3.left)
        return self.ll(k3)

    def rl(self, k1):
        k1.rightChild = self.ll(k1.rightChild)
        return self.rr(k1)

    def delete(self, k):
        node = self.search(k)
        if node is not None:
            self.deleting(self.root, node)

    def deleting(self, root, node):
        if self.root is None or node is None:
            return None
        if node.value < root.value:
            root.leftChild = self.deleting(root.left, node)
            if self.height(root.rightChild) == self.height(root.leftChild) + 2:
                r = root.rightChild
                if self.height(r.leftChild) > self.height(r.rightChild):
                    root = self.rl(root)
                else:
                    root = self.rr(root)
        elif node.value > root.value:
            root.rightChild = self.deleting(root.rightChild, node)
            if self.height(root.leftChild) == self.height(node.rightChild) + 2:
                l = root.leftChild
                if self.height(l.rightChild) > self.height(l.leftChild):
                    root = self.lr(root)
                else:
                    root = self.ll(root)
        else:
            if root.leftChild is not None and root.rightChild is not None:
                if self.height(root.leftChild) > self.height(root.rightChild):
                    maxNode = self.findMax(root.leftChild)
                    root.value = maxNode.value
                    root.leftChild = self.deleting(root.leftChild, maxNode)
                else:
                    minNode = self.findMin(root.rightChild)
                    root.value = minNode.value
                    root.rightChild = self.deleting(root.right, minNode)
            else:
                root = root.leftChild if root.leftChild is not None else root.rightChild
        return root

    def findMax(self, node):
        if node is None:
            return None
        while node.rightChild is not None:
            node = node.rightChild
        return node

    def findMin(self, node):
        if node is None:
            return None
        while node.leftChild is not None:
            node = node.leftChild
        return node