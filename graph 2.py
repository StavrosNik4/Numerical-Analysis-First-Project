# Κώδικας για το διάγραμμα της συνάρτησης της δεύτερης άσκησης

import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-2, 2, 0.1)
y = 54 * x ** 6 + 45 * x ** 5 - 102 * x ** 4 - 69 * x ** 3 + 35 * x ** 2 + 16 * x - 4

# setting the axes
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x, y, 'r')

# show the plot
plt.show()