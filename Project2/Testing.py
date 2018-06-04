from TestFunc import *
import matplotlib.pyplot as plt
import numpy as np

# configuration
tree_type = 1
write = 1
display_type = 1
loop_times = 50

colors = ['b', 'r', 'g']
test_size = 5000
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
        # np.savetxt("dataset.txt", test.getDataset())
        # np.savetxt("dataset_unit.txt", test.getDatasetUnit())

        results += test.start_test(tree_type)
        print(i+1, " times finished")
    results /= loop_times

    # save data
    np.savetxt(file_name,results)

if display_type == 0:
    # show in 3 plots
    for i in range(3):
        plt.figure(i)
        plt.plot(bases, results[:, i], colors[i])
        plt.show()
else:
    # show in one plot
    plt.figure(1)
    for i in range(3):
        plt.plot(bases, results[:, i], colors[i])
    plt.show()