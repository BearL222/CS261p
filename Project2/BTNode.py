class BTNode:
    value = None
    leftChild = None
    rightChild = None
    parent = None

    def __init__(self, value, parent):
        self.value = value
        self.parent = parent