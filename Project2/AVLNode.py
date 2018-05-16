class AVLNode:
    value = None
    leftChild = None
    rightChild = None
    height = None
    parent = None

    def __init__(self, value, parent):
        self.value = value
        self.height = 0
        self.parent = parent