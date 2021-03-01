import math
import time

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

def is_prime(num):
    global PRIMES
    if num in PRIMES:
        return True

    for prime in PRIMES:
        if num % prime == 0:
            return False
    
    for i in range(PRIMES[-1]+1, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    # if len(PRIMES) < 200:
    #     PRIMES.append(num)
    return True


def is_horseshoe_prime(num):
    #if is_prime(num):
    #    return False

    for p in PRIMES:
        if num < p:
            return False

        if num % p == 0:
            factor1 = p
            factor2 = num // p
            if factor1 == factor2:
                return False
            if is_prime(factor1) and is_prime(factor2):
                #print(num,factor1,factor2)
                return True
            else:
                return False

    for p in range(PRIMES[-1]+1, num//2+1):
        if num % p == 0:
            factor1 = p
            factor2 = num // p
            if factor1 == factor2:
                return False
            if is_prime(factor1) and is_prime(factor2):
                #print(num,factor1,factor2)
                return True
            else:
                return False
    
    print("This shouldn't happen...",num)
    return False

start = time.time()

prime_count = 0
horseshoe_count = 0

for i in range(2,1000000):
    if is_prime(i):
        prime_count += 1
    elif is_horseshoe_prime(i):
        horseshoe_count += 1

print(horseshoe_count,prime_count,horseshoe_count/prime_count)

print(f'Finished in: {(time.time() - start):.03} seconds.')
    