import matplotlib.pyplot as plt
import numpy as np

plt.figure()
# subplot with 1 row, 2 columns, and current axis is 1st subplot axes
plt.subplot(1, 2, 1)
linear_data = np.array([1, 2, 3, 4, 5, 6, 7, 8])
plt.plot(linear_data, '-o')
# plt.show()

exponential_data = linear_data ** 2
plt.subplot(1, 2, 2)
plt.plot(exponential_data, '-o')
plt.show()

# plot exponential data on 1st subplot axes
plt.subplot(1, 2, 1)
plt.plot(exponential_data, '-x')
plt.show()

plt.figure()
ax1 = plt.subplot(1, 2, 1)
plt.plot(linear_data, '-o')
# pass sharey=ax1 to ensure the two subplots share the same y axis
ax2 = plt.subplot(1, 2, 2, sharey=ax1)
plt.plot(exponential_data, '-x')
plt.show()

plt.figure()
# the right hand side is equivalent shorthand syntax
plt.subplot(1, 2, 1) == plt.subplot(121)

# create a 3x3 grid of subplots
fig, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(3, 3, sharex=True, sharey=True)
# plot the linear_data on the 5th subplot axes
ax5.plot(linear_data, '-')

# set inside tick labels to visible
for ax in plt.gcf().get_axes():
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_visible(True)

# necessary on some systems to update the plot
plt.gcf().canvas.draw()
plt.show()
