class TNode:
    value = None
    priority = None
    leftChild = None
    rightChild = None
    parent = None

    def __init__(self, value, priority, parent):
        self.value = value
        self.priority = priority
        self.parent = parent

