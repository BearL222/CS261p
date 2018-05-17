from time import *
import random
import numpy as np
from BinaryTree import *
from AVLTree import *
from Treap import *


class TestFunc:
    test_size = None
    rand_range = None
    base = None
    dataset = None
    bases = None

    def __init__(self, test_size):
        self.test_size = test_size
        self.rand_range = test_size * 10
        self.base = test_size / 50
        self.dataset = []
        self.bases = []
        for i in range(1, 51):
            self.bases.append(int(self.base * i))
        for i in range(0, test_size):
            self.dataset.append(random.randint(0, self.rand_range))

    def getBases(self):
        return self.bases

    def test_tree(self, partSet, type):
        times = []
        tree = None

        # create
        start = time()
        if type == 0:
            tree = BinaryTree()
        elif type == 1:
            tree = AVLTree()
        elif type == 2:
            tree = Treap()
        end = time()
        times.append(end - start)

        # insert
        start = time()
        for e in partSet:
            tree.insert(e)
        print("set sized ", len(partSet), " finish")
        end = time()
        times.append(end - start)

        # search
        start = time()
        for e in partSet:
            tree.search(e)
        end = time()
        times.append(end - start)

        # delete
        start = time()
        for e in partSet:
            tree.delete(e)
        end = time()
        times.append(end - start)

        return times

    def start_test(self, type):
        results = np.zeros((50,4))
        for index, i in enumerate(self.bases):
            results[index,:] = self.test_tree(self.dataset[:i], type)
        return results
