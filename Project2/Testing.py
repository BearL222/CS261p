from TestFunc import *
import matplotlib.pyplot as plt
import numpy as np


loop_times = 5
results = np.zeros((50,4))
for i in range(loop_times):
    print(i," times finished")
    # basic test info
    test = TestFunc(50000)
    results += test.start_test(0)
results /= loop_times

# show plot
for i in range(4):
    plt.figure(i)
    plt.plot(test.getBases(), results[:, i], 'r')
    plt.show()