def Newton(f, dfdx, x, eps=1E-7, maxit=100):
    if not callable(f): raise TypeError( 'f is %s, should be function or class with __call__' % type(f) )
    if not callable(dfdx): raise TypeError( 'dfdx is %s, should be function or class with __call__' % type(dfdx) )
    if not isinstance(maxit, int): raise TypeError( 'maxit is %s, must be int' % type(maxit) )
    if maxit <= 0: raise ValueError( 'maxit=%d <= 0, must be > 0' % maxit )
    n = 0 # iteration counter
    while abs(f(x)) > eps and n < maxit:
        try:
            x = x - f(x)/float(dfdx(x))
        except ZeroDivisionError:
            break
        n += 1
    return x, f(x), n

def test_Newton_div_by_zero():
    from math import sin, cos, pi
    def f(x):
        return cos(x)
    
    def dfdx(x):
        return -sin(x)

    x, f_x, n = Newton(f, dfdx, x = 0, eps=1E-2)
    success = False
    if n > 0:
        success = True
    print("success is {}" .format(success))
    assert n > 0, "The test for ZeroDivisionError failed."

test_Newton_div_by_zero()