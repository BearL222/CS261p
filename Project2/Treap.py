import random
from TNode import *


class Treap:
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

    def rotate_right(self, parent):
        # mark parent's parent
        pp = parent.parent
        if pp is not None:
            lor = parent is not pp.leftChild

        # rotate
        v = parent.leftChild
        parent.leftChild = v.rightChild
        v.rightChild = parent

        # update parent
        if pp is not None:
            v.parent = pp
            if lor:
                pp.rightChild = v
            else:
                pp.leftChild = v
        else:
            self.root = v
        parent.parent = v
        if parent.leftChild is not None:
            parent.leftChild.parent = parent

    def rotate_left(self, parent):
        # mark parent's parent
        pp = parent.parent
        if pp is not None:
            lor = parent is not pp.leftChild

        # rotate
        v = parent.rightChild
        parent.rightChild = v.leftChild
        v.leftChild = parent

        # update parent
        if pp is not None:
            v.parent = pp
            if lor:
                pp.rightChild = v
            else:
                pp.leftChild = v
        else:
            self.root = v
        parent.parent = v
        if parent.rightChild is not None:
            parent.rightChild.parent = parent

    def insert(self, k):
        new_node = TNode(k, random.random(), None)
        if self.empty:
            self.empty = False
            self.root = new_node
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
                parent.leftChild = new_node
            else:
                parent.rightChild = new_node
            new_node.parent = parent

            # do some rotation
            v = new_node
            r = 0
            while v.parent is not self.root and v.priority > v.parent.priority:
                r += 1
                print(r)
                if v is v.parent.leftChild:
                    self.rotate_right(v.parent)
                elif v is v.parent.rightChild:
                    self.rotate_left(v.parent)

    def delete(self, k):
        v = self.search(k)
        if v is None:
            node = None
        else:
            while v.leftChild is not None or v.rightChild is not None:
                if v.leftChild is None:
                    self.rotate_left(v)
                elif v.rightChild is None or v.leftChild.priority > v.rightChild.priority:
                    self.rotate_right(v)
                else:
                    self.rotate_left(v)
            v = None