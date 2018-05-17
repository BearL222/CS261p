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
            self.root = BTNode(k, None)
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
                parent.leftChild = BTNode(k, parent)
            else:
                parent.rightChild = BTNode(k, parent)

    def delete(self, k):
        node = self.search(k)
        if node is not None:
            self.true_delete(node)

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
        if node is self.root:
            # node is the root
            if node.leftChild is None and node.rightChild is None:
                self.root = None
                self.empty = True
            elif node.leftChild is not None and node.rightChild is None:
                self.root = node.leftChild
                node.leftChild.parent = None
            elif node.leftChild is None and node.rightChild is not None:
                self.root = node.rightChild
                node.rightChild.parent = None
            else:
                # find the max one in left subtree
                max_left = node.leftChild
                while max_left.rightChild is not None:
                    max_left = max_left.rightChild
                value_to_relace = max_left.value
                self.true_delete(max_left)
                node.value = value_to_relace
        else:
            # node is not the root
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
                    if ~lor:
                        parent.leftChild = node.leftChild
                        parent.leftChild.parent = parent
                    else:
                        parent.rightChild = node.leftChild
                        parent.rightChild.parent = parent
                elif node.leftChild is None and node.rightChild is not None:
                    if ~lor:
                        parent.leftChild = node.rightChild
                        parent.leftChild.parent = parent
                    else:
                        parent.rightChild = node.rightChild
                        parent.rightChild.parent = parent
                else:
                    # find the max one in left subtree
                    max_left = node.leftChild
                    while max_left.rightChild is not None:
                        max_left = max_left.rightChild
                    value_to_relace = max_left.value
                    self.true_delete(max_left)
                    node.value = value_to_relace