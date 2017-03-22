#! /usr/bin/env python
def fib(n):
    if not isinstance(n,int):
        print('The input argument is not a non-negative integer!')
    if n < 0:
        print('The input argument is not a non-negative integer!')
        
    def fibo(n):
        a = 0; b = 1
        for i in range(0,n-1):
            b = a+b
            a = b-a
        return b
    return fibo(n)
    n = input('Please enter another non-negative integer or type stop:')
    fib(n)