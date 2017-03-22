a1 = 2 # Varaibles cannot start with a number
b = a1 # B is undefined, it's value cannot be given to a1
x = 2
y = x + 4 # is it 6? No, the defined x was lowercase, case matters in variables, this will throw an error, change uppercase to lower.
from math import tan,pi # math should be lowercase
print(tan(pi)) # print statements need parenthesis in Python 3
pi = 3.14159 # You want an int, not a string or anything, no quotes.
print (tan(pi))
c = 4**3**2**3
_ = ((c-78564)/c + 32) # Too many parenthesis, eliminate 1
discount = '12%' # This needs to be a string or needs to be .12 if you want to use it in calculations.
AMOUNT = -120 # Negative numbers would just have a negative out front
amount = '120$' # If you want to show the money sign then you need to make this a string with quotes.
address = 'hpl@simula.no' # The email is a string, add quotes
And = 'duck' # and is a protected word in Python, change it a bit, duck is also not defined, And cannot equal it, make it a string
class1 = "INF1100, gr 2" # class is protected as well, use same quotes at beginning and end
continue_ = x > 0
rev = fox = True
Persian = ['a human language']
true = fox is rev in Persian
# The last line of the code moves from right to left. First Python checks if rev is in Persian. Asking if True is in 'a human language'. It is not and so it returns False. Then fox is False ask if True is equal to False, not true, returns False, and so true is equated to False.