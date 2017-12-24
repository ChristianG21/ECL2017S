Homework 6  
1) Done, look at code.  
  
2) Done, look at code.  
  
3) The function is creating a for loop, running from 1 to 59 (n). 2.0 then goes through the first  
interior for statement, this takes the sqrt of r, sets that equal to r and reiterates however many  
times t get to n at that point. Then this is again happening, however now it's the square of the  
now far from sqrt(2) after all the iterations in the first loop. This square is equal to r and gets  
reiterated over and over till it hits n and that times. The final solution so off from getting 2  
because of how computers operate, computers only have an ability to store data to a certain point.  
Computers can only store information to 16 decimals. That means that when we get into really complicated  
square roots the computer is losing data with rounding errors here and there. Thus when you square  
the already messed up numbers the end result is not the correct answer. Basically, computers aren't  
100% precise and information is lost when dealing with little numbers, in cases like this, those  
little numbers matter.
    
4) The code is going and dividing eps over and over by 2 and then the result is finally shown.  
1 != 1 + eps because 1 is actually equivalent to False in Python while 0 is equivalent to True.  
This means that this statement is actually True != 1 + eps, and because the right side is an int compared  
to a boolean we get that the statement is false.  
    
5) n jumps from 3 to 8 when going throughout the range. However that's because we're deleting parts  
the range, and because of that, after we get rid of 3 we jump straight to n = 8, because there are  
no numbers between 3 and 8.  
    
6) A) Done, look at code.  
  
B) get\_primes(n), the recursive was much faster, recording at 36.6 microseconds per loop compared  
to to 1.73 milliseconds per loop using for loops in get\_primes\_for(n).  
