from AVLNode import *


class AVLTree:
    root = None
    empty = True
    counter = 0

    def __init__(self):
        self.empty = True

    def search(self, k):
        results = [None] * 2
        self.counter = 0
        if self.root is None:
            self.counter += 1
            results[1] = self.counter
            return results

        node = self.root
        while node is not None:
            self.counter += 1
            if k < node.value:
                node = node.leftChild
            elif k > node.value:
                node = node.rightChild
            else:
                results[0] = node
                break;
        results[1] = self.counter
        return results

    def insert(self, k):
        results = [None] * 2
        self.counter = 0
        node = self.inserting(self.root, k)
        if self.root is None:
            self.root = node
        results[1] = self.counter
        return results

    def inserting(self, node, k):
        self.counter += 1
        if node is None:
            node = AVLNode(k)
        elif k < node.value:
            node.leftChild = self.inserting(node.leftChild, k)
            if self.height(node.leftChild) == self.height(node.rightChild) + 2:
                if k < node.leftChild.value:
                    node = self.ll(node)
                else:
                    node = self.lr(node)
        elif k > node.value:
            node.rightChild = self.inserting(node.rightChild, k)
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
        self.counter += 1
        k1 = k2.leftChild
        k2.leftChild = k1.rightChild
        k1.rightChild = k2
        k2.height = max(self.height(k2.leftChild), self.height(k2.rightChild)) + 1
        k1.height = max(self.height(k1.leftChild), self.height(k1.rightChild)) + 1
        return k1

    def rr(self, k1):
        self.counter += 1
        k2 = k1.rightChild
        k1.rightChild = k2.leftChild
        k2.leftChild = k1
        k1.height = max(self.height(k1.leftChild), self.height(k1.rightChild)) + 1
        k2.height = max(self.height(k2.leftChild), self.height(k2.rightChild)) + 1
        return k2

    def lr(self, k3):
        self.counter += 1
        k3.leftChild = self.rr(k3.leftChild)
        return self.ll(k3)

    def rl(self, k1):
        self.counter += 1
        k1.rightChild = self.ll(k1.rightChild)
        return self.rr(k1)

    def delete(self, k):
        results = [None] * 2
        self.counter = 0
        return_node = self.search(k)
        if return_node[0] is not None:
            self.deleting(self.root, return_node[0])
        results[1] = self.counter
        return results

    def deleting(self, root, node):
        self.counter += 1
        if root is None or node is None:
            return None
        if node.value < root.value:
            root.leftChild = self.deleting(root.leftChild, node)
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
                    root.rightChild = self.deleting(root.rightChild, minNode)
            else:
                root = root.leftChild if root.leftChild is not None else root.rightChild
        return root

    def findMax(self, node):
        self.counter += 1
        if node is None:
            return None
        while node.rightChild is not None:
            self.counter += 1
            node = node.rightChild
        return node

    def findMin(self, node):
        self.counter += 1
        if node is None:
            return None
        while node.leftChild is not None:
            node = node.leftChild
            self.counter += 1
        return node