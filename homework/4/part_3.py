#! /usr/bin/env python
from math import log, pi, exp
M=67;c=3.7;p=1.038;K=.0054;To=4;Tw=100;Ty=70
time4  = (((M**(2/3))*c*(p**(1/3)))/(K*(pi**2)*(((4*pi)/3)**(2/3))))*log((.76*((To - Tw)/(Ty-Tw))),exp(1))
M=67;c=3.7;p=1.038;K=.0054;To=20;Tw=100;Ty=70
time20  = (((M**(2/3))*c*(p**(1/3)))/(K*(pi**2)*(((4*pi)/3)**(2/3))))*log((.76*((To - Tw)/(Ty-Tw))),exp(1))
print("The time for a large egg to reach 70\u00b0C from\n4\u00b0C is {:.3f}s and it's {:.3f}s from 20\u00b0C.\n".format(time4,time20))