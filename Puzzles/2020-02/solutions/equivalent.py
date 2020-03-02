# Mr. Purdy

import math
def find_factors(n):
    ''' 
    returns a list of all factors of n that are less than n
    '''

    factors = set()
    factors.add(1)
    for i in range(2,round(math.sqrt(n)+0.5)+1):
        if n % i == 0:
            factors.add(i)
            factors.add(n//i)

    return factors

def find_equivalent_dict(n, upper):
    '''
    returns a dictionary of all numbers less than upper
    that are "equivalent" to n

    key = number, value = list of factors

    here, equivalent means the sum of their factors
    is the same
    '''

    value = sum(find_factors(n))
    result = {n:find_factors(n)}
    for i in range(1,upper):
        if i != n:
            i_factors = find_factors(i)
            t_val = sum(i_factors)
            if value == t_val:
                result[i] = i_factors
    return result


def find_equivalent_list(n, upper):
    '''
    returns a list of all numbers less than upper
    that are "equivalent" to n

    here, equivalent means the sum of their factors
    is the same
    '''

    value = sum(find_factors(n))
    result = set()
    result.add(n)
    for i in range(1,upper):
        if i != n:
            i_factors = find_factors(i)
         
            t_val = sum(i_factors)
            if t_val == 1: # prime!
                continue
            if value == t_val and (i not in result):
                result.add(i)
    #print(result)
    return result


def find_largest_difference(upper):
    '''
    returns the pair of equivalent numbers
    less than upper with the greatest difference
    '''
    equivalents = set()
    greatest_diff = 0
    greatest_pair = (0,0)
    for i in range(1,upper):
        # if i % 100 == 0:
        #     print(i)
        if i in equivalents:
            continue
        values = find_equivalent_list(i,upper)
        
        diff = max(values) - min(values)
        if diff > greatest_diff:
            greatest_diff = diff
            greatest_pair = (min(values), max(values))

        for n in values:
            equivalents.add(n)

    return greatest_pair
        
        # add numbers in list to equivalents
        # set to avoid finding duplicates



def main():

    print(find_largest_difference(2020))


if __name__ == "__main__":
    main()

