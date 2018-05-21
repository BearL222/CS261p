from BTNode import *


class BinaryTree:
    root = None
    empty = True
    counter = None

    def __init__(self):
        self.empty = True
        self.counter = 0

    def search(self, k):
        results = [None] * 2
        self.counter = 0
        if self.empty:
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
                break
        results[1] = self.counter
        return results

    def insert(self, k):
        results = [None] * 2
        self.counter = 0
        if self.empty:
            self.counter += 1
            self.empty = False
            self.root = BTNode(k, None)
        else:
            node = self.root
            parent = None
            lor = 0
            h1 = True
            while node is not None:
                self.counter += 1
                if k < node.value:
                    parent = node
                    lor = 0
                    node = node.leftChild
                elif k > node.value:
                    parent = node
                    lor = 1
                    node = node.rightChild
                else:
                    h1 = False
                    break
            if h1:
                if lor == 0:
                    parent.leftChild = BTNode(k, parent)
                else:
                    parent.rightChild = BTNode(k, parent)
        results[1] = self.counter
        return results

    def search_internal(self, k):
        if self.empty:
            self.counter += 1
            return None

        node = self.root
        while node is not None:
            self.counter += 1
            if k < node.value:
                node = node.leftChild
            elif k > node.value:
                node = node.rightChild
            else:
                return node
        return None

    def delete(self, k):
        results = [None] * 2
        self.counter = 0
        node = self.search_internal(k)
        if node is not None:
            self.true_delete(node)
        results[1] = self.counter
        return results

    def remove_node(self, node):
        if node is not None:
            if node.parent is None:
                # it is the root
                self.root = None
                self.empty = True
            else:
                if node is node.parent.leftChild:
                    node.parent.leftChild = None
                elif node is node.parent.rightChild:
                    node.parent.rightChild = None

    def true_delete(self, node):
        # if it is the root
        is_root = False
        dummy = BTNode(0, None)
        if node is self.root:
            self.counter += 1
            is_root = True
            dummy.leftChild = node
            node.parent = dummy

        # 3 cases
        self.counter += 1
        if node.leftChild is None and node.rightChild is None:
            # if node is a leaf node
            self.remove_node(node)
        else:
            # if node is not a leaf node
            lor = node is node.parent.rightChild
            parent = node.parent
            if node.leftChild is None and node.rightChild is None:
                self.remove_node(node)
            elif node.leftChild is not None and node.rightChild is None:
                if not lor:
                    parent.leftChild = node.leftChild
                    parent.leftChild.parent = parent
                else:
                    parent.rightChild = node.leftChild
                    parent.rightChild.parent = parent
            elif node.leftChild is None and node.rightChild is not None:
                if not lor:
                    parent.leftChild = node.rightChild
                    parent.leftChild.parent = parent
                else:
                    parent.rightChild = node.rightChild
                    parent.rightChild.parent = parent
            else:
                # find the max one in left subtree
                max_left = node.leftChild
                while max_left.rightChild is not None:
                    self.counter += 1
                    max_left = max_left.rightChild
                value_to_relace = max_left.value
                self.true_delete(max_left)
                node.value = value_to_relace

        # if it is the root, remove dummy
        if is_root:
            node.parent = None
