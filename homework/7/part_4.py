import sys
try:
	v0 = float(sys.argv[1]); g = 9.81; t = float(sys.argv[2])
	y = (v0*t-0.5*g*t**2)
except IndexError:	
	print('Both v0 and t must be supplied on the command line\nv0 = ?')
	v0 = float(input())
	print('t = ?')
	t = float(input())
	g = 9.81
	y = (v0*t-0.5*g*t**2)
if t < 0 or 2*(v0/g) < t:
	raise ValueError('t = {} is a non-physical value.\nmust be between 0 and 2v0/g = {}'.format(t,2.0*v0/g))
print('y = {}' .format(y))