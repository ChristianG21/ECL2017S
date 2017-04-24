import numpy as np
def vectf(x):
	x = np.array(x)
	y = np.zeros(x.shape)
	y += ((x>=0) & (1>x))*(x)
	y += ((x>=1) & (2>x))*(2-x)
	return y