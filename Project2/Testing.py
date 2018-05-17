from TestFunc import *
import matplotlib.pyplot as plt
from BTNode import *


# basic test info
test = TestFunc(500)
results = test.start_test(2)

for i in range(0, 4):
    plt.figure(i)
    plt.plot(test.getBases(), results[:, i], 'r')
    plt.show()