def is_primes_for(n):
    divided = 0
    for k in range(2,n):
        if n%k == 0:
            divided += 1
        if divided > 0:
            return 0
    return 1
    
def get_primes_for(n):
    primes = 0
    for j in range(2,n):
        primes += is_prime_for(j)
    return primes