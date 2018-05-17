from SNode import *

class SplayTree:
    root = None
    empty = True

    def __init__(self):
        self.empty = True

    def rotate_right(self, parent):
        print("rotate right")
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
        print("rotate left")
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
        print("splay")
        if node is None:
            return
        while node.parent is not None:
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
        if not self.empty:
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
        if not self.empty:
            node = self.root
            last = None
            # find it
            while node is not None:
                print("try to find it, node value ", node.value, ", key is ", k)
                last = node
                if k < node.value:
                    node = node.leftChild
                elif k > node.value:
                    node = node.rightChild
                else:
                    success = True
                    break
            if success:
                # delete it
                p = node.parent
                self.true_delete(node)
                self.splay(p)
            else:
                self.splay(last)
        return success

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
        dummy = SNode(0, None)
        if node is self.root:
            is_root = True
            dummy.leftChild = node
            node.parent = dummy

        # 3 cases
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
                    if max_left.rightChild.value <= max_left.value:
                        a=1
                    max_left = max_left.rightChild
                value_to_relace = max_left.value
                self.true_delete(max_left)
                node.value = value_to_relace

        # if it is the root, remove dummy
        if is_root:
            node.parent = None
