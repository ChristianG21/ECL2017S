import numpy as np
def midpoint(f,a,b,n):
	h = (b-a)/n
	ansnoh = 0
	for k in range(0,n-1):
		ansnoh += f(a+k*h+.5*h)
	return ansnoh*h

#print(midpoint(np.exp,0,np.log(3),100))
#print(midpoint(np.cos,0,np.pi,100))
#print(midpoint(np.sin,0,np.pi,100))
#print(midpoint(np.sin,0,np.pi*.5,100))