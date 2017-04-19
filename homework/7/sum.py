import sys
sys.argv[1:] = [int(x) for x in sys.argv[1:]]
print("The sum of {} is {}." .format(sys.argv[1:],sum(sys.argv[1:])))