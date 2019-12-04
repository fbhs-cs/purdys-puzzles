## IDEAS

## Black Friday + Year = prime?

'''
26  -  99
24  -  00
23  -  01
29  -  02
28  -  03
26  -  04
25  -  05
24  -  06
23  -  07
28  -  08
27  -  09
26  -  10
25  -  11
23  -  12
29  -  13
28  -  14
27  -  15
25  -  16
24  -  17
23  -  18
29  -  19
27  -  20
'''


def is_leap(year):
    if year % 400 == 0:
        return True
    
    if year % 4 == 0 and year % 100 != 0:
        return True
    
    return False

def find_bf(year):
    curr = 2019
    bf = 29
    
    if year == curr:
        return bf
    
    elif year > curr:
        while(curr < year):
            curr += 1
            if is_leap(curr):
                bf -= 2
            else:
                bf -= 1
            if bf == 22:
                bf = 29
            elif bf == 21:
                bf = 28
    else:
        while(curr > year):
            curr -= 1
            if is_leap(curr):
                bf += 2
            else:
                bf += 1
            if bf == 30:
                bf = 23
            elif bf == 31:
                bf = 24
            
    return bf

def is_prime(num):
    import math
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2,int(math.ceil(math.sqrt(num)))+1):
        if num % i == 0:
            return False
    return True


def solve():
    num_prime = 0
    for i in range(2,2999):
        last_two = i % 100
        bf = find_bf(i)
        if is_prime(last_two) and is_prime(bf):
            num_prime += 1
            print(i,bf)
    print(num_prime)
        
    
solve()

