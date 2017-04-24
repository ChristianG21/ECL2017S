import matplotlib.pyplot as plt
import numpy as np
import sys
vi = int(sys.argv[1])
m = int(sys.argv[2])
g = 9.81
def y(t):
	return vi*t-.5*g*t**2
def dy(t):
	return vi-g*t
def P(t):
    return m*g*y(t)
def K(t):
    return .5*m*dy(t)**2
def E(t):
	return P(t)+K(t)

x = np.linspace(0, (2*vi)/g,50) # 51 points between 0 and 3
yP = np.zeros(len(x)) # allocate y with float elements
yK = np.zeros(len(x)) # allocate y with float elements
yE = np.zeros(len(x))
for i in range(len(x)):
    yP[i] = P(x[i])
    yK[i] = K(x[i])
    yE[i] = E(x[i])
plt.plot(x, yP, 'r-')   # plot with color red, as line
plt.plot(x, yK, 'b-')   # # plot with color blue, as points
plt.plot(x, yE, 'g-') 
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['m*g*y' , '.5*m*v^2', 'P(t)+K(t)'])
plt.axis([0, (2*vi)/g,0,(vi**2)*(.5*m)+.5]) # [xmin, xmax, ymin, ymax]
plt.title('Potential and Kinetic Energy over time')
plt.show()
