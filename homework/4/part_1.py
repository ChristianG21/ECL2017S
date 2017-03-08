#! /usr/bin/env python
from math import pi, exp, sqrt
m = 0; o = 2; x = 1
mathanswer = (1/(sqrt(2*pi)*o)) * exp(-.5 *((x-m)/o)**2)
print(mathanswer)