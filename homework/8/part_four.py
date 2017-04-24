from part_three import midpoint
import matplotlib.pyplot as plt
import numpy as np

def y(x):
	return x*(12-x)+np.sin(np.pi*x)
yY = np.zeros(len(x))
for i in range(len(x)):
    yY[i] = P(x[i])
plt.plot(x, yY, 'r-')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([0,10,0,40]) # [xmin, xmax, ymin, ymax]
plt.title('Function compared to Midpoint')
plt.show()
