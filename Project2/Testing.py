from TestFunc import *
import matplotlib.pyplot as plt
import numpy as np


tree_type = 0
test_size = 50000
base_size = test_size / 50
bases = []
for i in range(1, 51):
    bases.append(int(base_size * i))

# file_name = "tree_" + str(tree_type) + ".txt"
#
# # load data from disk
# results = np.genfromtxt(file_name, delimiter=',')

# calculate data
loop_times = 1
results = np.zeros((50,4))
for i in range(loop_times):
    # basic test info
    test = TestFunc(test_size)
    results += test.start_test(tree_type)
    print(i+1, " times finished")
results /= loop_times
#
# # save data
# np.savetxt(file_name,results)

# show plot
for i in range(4):
    plt.figure(i)
    plt.plot(bases, results[:, i], 'b')
    plt.show()