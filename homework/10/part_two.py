import matplotlib.pyplot as plt
import numpy as np
import random as rnd

# function to solve for y
def function(x):
	fans = ((x+1)/12)*np.exp(-1*((np.power(x-1,2))/(2*x)))
	return fans

# do a number of trials to see if points are in/outside of f(x), save data
n = 100000 # number of trails
insidef = np.zeros((2,n),dtype=np.double) # initialize arrays to save points in/outside of f(x)
outsidef = np.zeros((2,n),dtype=np.double)
for k in range(1,n):
	testpt = [rnd.uniform(0,15), rnd.uniform(0,.2)] # [x,y]
	if testpt[1] <= function(testpt[0]): # is y < f(x)
		insidef[0,k] = testpt[0] # save [x,y] that are < f(x)
		insidef[1,k] = testpt[1]
	else:
		outsidef[0,k] = testpt[0] # save [x,y] that are > f(x)
		outsidef[1,k] = testpt[1]
insidefval = insidef[:, ~np.all(insidef == 0, axis=0)] # Eliminating columns with just 0's in x & y
outsidefval = outsidef[:, ~np.all(outsidef == 0, axis=0)]

# lameplot
x = np.linspace(0.00000000000001,15,1500) # Setting X range to test
plt.figure() # Creating figure
plt.plot(x,function(x),'b-',alpha=.6,label="f(x)") # Creating function graph
plt.axis([-.5,15.5,-.01,.21]) # [xmin, xmax, ymin, ymax]
plt.legend(loc=1) 
plt.title('Plot of f(x)')

# histogram
x = np.linspace(0.00000000000001,15,1500) # Setting X range to test
plt.figure() # Creating figure
plt.hist(insidefval[0],bins=75,normed=1) # Creating histogram normed to 1
plt.plot(x,function(x),'r-',label="f(x)") # Creating function graph
plt.axis([-.5,15.5,0,.21]) # [xmin, xmax, ymin, ymax]
plt.legend(loc=1) 
plt.title('Histogram of f(x) Estimations')

# rejected/accepted plot
plt.figure() # Creating the second figure
plt.scatter(insidefval[0],insidefval[1],s=.2,color='r',alpha=.5,label='Accepted') # Creating accepted scatter plot
plt.scatter(outsidefval[0],outsidefval[1],s=.2,color='black',alpha=.5,label='Rejected') # Creating rejected scatter plot
plt.axis([-.5,15.5,-.01,.21]) # [xmin, xmax, ymin, ymax]
plt.legend(loc=1)
plt.title('Scatterplot of Accepted and Rejected Points')
plt.show()