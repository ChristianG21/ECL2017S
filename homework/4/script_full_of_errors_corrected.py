a1 = 2 # You can't have a variable start with a number, change to "a1"
a1 = b = 3 # b must have a value for a1 to be equal to, give b any value
x = 2
y = x + 4 # is it 6? No, you had a "X" not a "x," case matters
from math import tan, pi # "math" is lowercase, we also must import pi for future use
print(tan(pi)) # You must have parenthesis to print in Python 3
pi = 3.14159 # There should be no quotes, that would create str, we want double for future
print (tan(pi))
c = 4**3**2**3
_ = ((c-78564)/c + 32) # There was an extra unpaired parenthesis, delete it
discount = "12%" # This is a statement that should be a string, was attempting math
AMOUNT = 120. #.- Doesn't do anything, just the period will give you a double
amount = 120 # $ Also doesn't do anything, no period gives you an integer
# With the two above, you could have added single (or double) quotes to make strings
address = "hpl@simula.no" # Adding quotes equates address to a string, not weird math
and1 = duck = 3 # "and" is a reserved name, can't change. Also duck must have some value
class1 = "INF1100, gr 2" # "class" is a reserved name, also quotes must be consistent
continue_ = x > 0
rev = fox = True
Persian = ['a human language']
true = fox is rev in Persian
# On line 21 the script is assigning some value to "true" (not reserved due to capitalization). The value it is being assigned is "fox is rev in Persian". Now a breakdown of that. We're moving from left to right, we're saying fox is rev, is is checking whether or not rev and fox are the same, because they're both True the is function returns True. So now we have the statement, "True in Persian". The In is a function that checks if True is somewhere in Persian. Because Persian is a string and True is a boolean, the function returns False. So now "true" is equal to False, and because we're simply assigning a value to a variable there is no display. true = False.