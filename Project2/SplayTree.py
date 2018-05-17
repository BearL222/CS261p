from SNode import *

class SplayTree:
    root = None
    empty = True

    def __init__(self):
        self.empty = True

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
            v.parent = None
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
            v.parent = None
        parent.parent = v
        if parent.rightChild is not None:
            parent.rightChild.parent = parent

    def splay(self, node):
        if node is None:
            return
        while node is not self.root:
            if node.parent.parent is None:
                # zig
                if node is node.parent.leftChild:
                    self.rotate_right(node.parent)
                else:
                    self.rotate_left(node.parent)
            elif node is node.parent.leftChild and node.parent is node.parent.parent.leftChild:
                # zig-zig left
                self.rotate_right(node.parent.parent)
                self.rotate_right(node.parent)
            elif node is node.parent.rightChild and node.parent is node.parent.parent.rightChild:
                # zig-zig right
                self.rotate_left(node.parent.parent)
                self.rotate_left(node.parent)
            elif node is node.parent.rightChild and node.parent is node.parent.parent.leftChild:
                # zig-zag left
                self.rotate_left(node.parent)
                self.rotate_right(node.parent)
            elif node is node.parent.leftChild and node.parent is node.parent.parent.rightChild:
                # zig-zag right
                self.rotate_right(node.parent)
                self.rotate_left(node.parent)

    def search(self, k):
        success = False
        if ~self.empty:
            node = self.root
            last = None
            while node is not None:
                last = node
                if k < node.value:
                    node = node.leftChild
                elif k > node.value:
                    node = node.rightChild
                else:
                    success = True
                    break
            if success:
                self.splay(node)
            else:
                self.splay(last)
        return success

    def insert(self, k):
        new_node = SNode(k, None)
        if self.empty:
            self.empty = False
            self.root = new_node
        else:
            # insert new node
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

            # splay
            self.splay(new_node)

    def delete(self, k):
        success = False
        if ~self.empty:
            node = self.root
            last = None
            lor = 0
            while node is not None:
                last = node
                if k < node.value:
                    node = node.leftChild
                    lor = 0
                elif k > node.value:
                    node = node.rightChild
                    lor = 1
                else:
                    success = True
                    break
            if success:
                p = node.parent
                if lor == 0:
                    p.leftChild = None
                else:
                    p.rightChild = None
                self.splay(p)
            else:
                self.splay(last)
        return success
