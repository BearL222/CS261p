from time import *
from random import *
import numpy as np
from BinaryTree import *


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
        for i in range(1, 51):
            self.bases.append(int(self.base * i))
        for i in range(0, test_size):
            self.dataset.append(random.randint(0, self.rand_range))

    @staticmethod
    def getBases(self):
        # return self.bases

    def test_binary_tree(partSet):
        times = []

        # create
        start = time()
        tree = BinaryTree()
        end = time()
        times.append(end - start)

        # insert
        start = time()
        for e in self.dataset:
            tree.insert(e)
        end = time()
        times.append(end - start)

        # search
        start = time()
        for e in self.dataset:
            tree.search(e)
        end = time()
        times.append(end - start)

        # delete
        start = time()
        for e in self.dataset:
            tree.delete(e)
        end = time()
        times.append(end - start)

        return times

    def test(self):
        results = np.zeros((50,4))
        for index, i in enumerate(self.base):
            results[index,:] = self.test_binary_tree(self.dataset[:i])
        return results