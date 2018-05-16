from TestFunc import *
import matplotlib.pyplot as plt


# basic test info
test = TestFunc(50000)
results = test.testing()

for i in range(0, 4):
    plt.figure(i)
    plt.plot(test.getBases(), results[:, i], 'r')
    plt.show()