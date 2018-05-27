from TestFunc import *
import matplotlib.pyplot as plt
import numpy as np

for tree_type in range(4):
    # configuration
    write = 0
    loop_times = 5

    colors = ['b','r','g','y']
    test_size = 50000
    base_size = test_size / 50
    bases = []
    for i in range(1, 51):
        bases.append(int(base_size * i))

    file_name = "results/tree_" + str(tree_type) + ".txt"

    if write == 0:
        # load data from disk
        results = np.loadtxt(file_name, delimiter=' ')
    else:
        # calculate data
        results = np.zeros((50,3))
        for i in range(loop_times):
            # basic test info
            test = TestFunc(test_size)
            results += test.start_test(tree_type)
            print(i+1, " times finished")
        results /= loop_times

        # save data
        np.savetxt(file_name,results)

    # show plot of all trees
    for i in range(3):
        plt.figure(i)
        plt.plot(bases, results[:, i], colors[tree_type])

plt.show()