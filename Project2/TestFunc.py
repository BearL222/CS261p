from time import *
import numpy as np
from BinaryTree import *
from AVLTree import *
from Treap import *
from SplayTree import *


class TestFunc:
    test_size = None
    rand_range = None
    unit_size = None
    base_size = None

    dataset = None
    dataset_unit = None
    bases = None

    def __init__(self, test_size):
        self.test_size = test_size
        self.rand_range = test_size * 100
        self.base_size = test_size / 50
        self.unit_size = self.base_size / 10

        self.dataset = []
        self.dataset_unit = []
        self.bases = []
        for i in range(1, 51):
            self.bases.append(int(self.base_size * i))
        for i in range(self.test_size):
            self.dataset.append(random.randint(0, self.rand_range))
        for i in range(int(self.unit_size)):
            self.dataset_unit.append(random.randint(0, self.rand_range))

    def getBases(self):
        return self.bases

    def start_test(self, type):
        results = np.zeros((50, 4))
        for index, i in enumerate(self.bases):
            results[index, :] = self.test_tree(self.dataset[:i], type)
        return results

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
        elif type == 3:
            tree = SplayTree()
        end = time()
        times.append(end - start)

        # insert enough data first: 1,000, 2,000,..., 50,000
        for e in partSet:
            tree.insert(e)

        # insert
        start = time()
        for e in self.dataset_unit:
            tree.insert(e)
        # print("set sized ", len(self.dataset_unit), " finish")
        end = time()
        times.append(end - start)

        # search
        start = time()
        for e in self.dataset_unit:
            tree.search(e)
        end = time()
        times.append(end - start)

        # delete
        start = time()
        for e in self.dataset_unit:
            tree.delete(e)
        end = time()
        times.append(end - start)

        return times
