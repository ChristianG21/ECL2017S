import matplotlib.pyplot as plt
import numpy as np
import random as rnd

n = 10000
incircle = 0
estimatedpi = np.zeros((n,1),dtype=np.double)

for k in range(1,n):
	testpt = [rnd.random(), rnd.random()]
	testdist = np.sqrt(np.power(testpt[0],2)+np.power(testpt[1],2))
	if testdist < 1:
		incircle +=1
	estimatedpi[k,0] = 4*(incircle/k)
	
trial = np.linspace(1,n+1,n)
plt.plot(trial,estimatedpi)
plt.semilogx(trial,estimatedpi)
plt.axis([1, n+(n*.25) , 2.3, 4.1]) # [xmin, xmax, ymin, ymax]
plt.xlabel('Number of Simulated Points')
plt.ylabel('Approximate Value of Pi')
plt.title('Estimating Pi by Monte Carlo Simulation')
plt.show()