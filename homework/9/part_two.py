import numpy as np
import matplotlib.pyplot as plt
import random as rnd


def gamesimulation(n,switch):
	averagedata = np.zeros((n),dtype=np.double)
	averagedata[0] = 0.0
	
	for i in range(1,n):
		possibledoors = [1,2,3]
		winningdoor = rnd.randint(1,3)
		selecteddoor = rnd.randint(1,3)
		losingdoor = rnd.randint(1,3)
		if losingdoor==selecteddoor or losingdoor==winningdoor:
			i -= 1
			continue
		possibledoors.remove(losingdoor)
		if switch is True:
			possibledoors = list(possibledoors) # Make a copy of the list.
			possibledoors.remove(selecteddoor)
			selecteddoor = possibledoors.pop()
		won = (selecteddoor == winningdoor)
		if won:
			averagedata[i] = 1.0
		averagedata[i] += averagedata[i-1]
		averagedata[i-1] /= np.double(i)
			
	averagedata[-1:] /= np.double(n)
	return averagedata

n = 100000
fig1 = plt.figure()
trial = np.linspace( 1 , n+1 , n )
lineTypes = ['r-','b-']
plt.semilogx( trial[:], gamesimulation(n,True),'r-')
plt.semilogx( trial[:], gamesimulation(n,False),'b-')
plt.xlabel('Trial Number')
plt.ylabel('Fraction of Occurance when Switching or Not')
plt.legend(['Switching','Not Switching'])
plt.axis([1, n , 0.0, 1.0]) # [xmin, xmax, ymin, ymax]
plt.title('N={} throws of a virtual die in Python'.format(n))
plt.savefig('GameSimTrialsN{}.png'.format(n))
plt.show()