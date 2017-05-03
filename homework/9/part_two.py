import numpy as np
import matplotlib.pyplot as plt
import random as rnd


def gamesimulation(n):
	gamedata = np.zeros((4,n),dtype=np.double)
	k = 1
	
	for i in range(1,n):
		possibledoors = [1,2,3]
		winningdoor = rnd.randint(1,3)
		selecteddoor = rnd.randint(1,3)
		losingdoor = rnd.randint(1,3)
		if losingdoor==selecteddoor or losingdoor==winningdoor:
			gamedata[2,i] = np.sum(gamedata[0]) / i
			gamedata[3,i] = np.sum(gamedata[1]) / i
			continue
		if selecteddoor==winningdoor:
			gamedata[0,i] = 1.0 # Not switching
		else:
			gamedata[1,i] = 1.0 # Switching
		gamedata[2,i] = np.sum(gamedata[0]) / i # Not switching
		gamedata[3,i] = np.sum(gamedata[1]) / i # Switching
	return gamedata

n = 10000
fig1 = plt.figure()
trial = np.linspace( 1 , n+1 , n )
lineTypes = ['r-','b-']
gamedata = gamesimulation(n)
plt.semilogx( trial[:], gamedata[2],'r-') # Not switching
plt.semilogx( trial[:], gamedata[3],'b-') # Switching
plt.xlabel('Trial Number')
plt.ylabel('Fraction of Occurance when Switching or Not')
plt.legend(['Switching','Not Switching'])
plt.axis([1, n , 0.0, 1.1]) # [xmin, xmax, ymin, ymax]
plt.title('N={} Game Simulations Played'.format(n))
plt.savefig('GameSimTrialsN{}.png'.format(n))
plt.show()
