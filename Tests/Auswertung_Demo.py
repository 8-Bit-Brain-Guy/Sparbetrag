import numpy as np
import matplotlib.pyplot as plt                     # Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

# Come up with x and y
x = np.arange(0, 5, 0.1)
y = np.sin(x)

# Just print x and y for fun
print(x)
print(y)

# Plot the x and y and you are supposed to see a sine curve
plt.plot(x, y)

# Without the line below, the figure won't show
plt.show()