class AVLNode:
    value = None
    leftChild = None
    rightChild = None
    height = None

    def __init__(self, value):
        self.value = value
        self.height = 1
