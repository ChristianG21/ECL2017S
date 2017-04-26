from part_three import midpoint
import matplotlib.pyplot as plt
import numpy as np
x = 1
yY = np.zeros(len(x))
for i in range(len(x)):
    yY[i] = x[i]*(12-x[i])+np.sin(np.pi*x[i])
plt.plot(x, yY, 'r-')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([0,10,0,40]) # [xmin, xmax, ymin, ymax]
plt.title('Function compared to Midpoint')
plt.show()
