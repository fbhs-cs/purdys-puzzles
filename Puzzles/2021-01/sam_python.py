def primes(start,end):
    numPrimes = 0
    for number in range(start,end):
        if number > 1:
            for factor in range(2,int(number**0.5)+1):
                if (number % factor == 0):
                    break
            else:
                numPrimes += 1
    return numPrimes

def hPrimes(start,end):
    numHPrimes = 0
    for number in range(start,end):
        numFactors = 0
        pFactor = 2
        while (numFactors < 2 and pFactor*pFactor <= number):
            while (number % pFactor == 0):
                number = number/pFactor
                numFactors += 1
            else:
                pFactor += 1
        if (number > 1):
            numFactors += 1
            if (numFactors == 2):
                numHPrimes += 1
    return numHPrimes

def ratio(start,end):
    p = primes(start,end)
    hp = hPrimes(start,end)
    print(round(hp/p,3))
ratio(1,1000000)
