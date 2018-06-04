from time import *
import numpy as np
from BinaryTree import *
from AVLTree import *
from Treap import *
from SplayTree import *
import random
import sys


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
        self.rand_range = sys.maxsize
        self.base_size = test_size / 50
        self.unit_size = self.base_size / 10

        self.bases = []
        for i in range(1, 51):
            self.bases.append(int(self.base_size * i))
        self.dataset = []
        for i in range(self.test_size):
            self.dataset.append(random.randint(0, self.rand_range))
        self.dataset_unit = []
        for i in range(int(self.unit_size)):
            self.dataset_unit.append(random.randint(0, self.rand_range))

    def getDataset(self):
        return self.dataset

    def getDatasetUnit(self):
        return self.dataset_unit

    def start_test(self, type):
        results = np.zeros((50, 3))
        for index, i in enumerate(self.bases):
            # create
            if type == 0:
                tree = BinaryTree()
            elif type == 1:
                tree = AVLTree()
            elif type == 2:
                tree = Treap()
            elif type == 3:
                tree = SplayTree()
            for e in self.dataset[0:i]:
                tree.insert(e)
            results[index, :] = self.test_tree(tree, type)
        return results

    def test_tree(self, tree, type):
        times = []

        # insert
        counter = 0
        for e in self.dataset_unit:
            counter += tree.insert(e)[1]
        times.append(counter / int(self.unit_size))

        # search
        counter = 0
        if type == 3:
            test_case_search = self.dataset[0:int(self.unit_size)]
            random.shuffle(test_case_search)
            for e in test_case_search:
                counter += tree.search(e)[1]
            times.append(counter / int(len(test_case_search)))
        else:
            for e in self.dataset_unit:
                counter += tree.search(e)[1]
            times.append(counter / int(self.unit_size))

        # delete
        counter = 0
        for e in self.dataset_unit:
            counter += tree.delete(e)[1]
        times.append(counter / int(self.unit_size))

        return times
