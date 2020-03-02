def is_prime(n):
    '''
    returns True if a number is prime and False if it isn't
    '''
    if n == 0 or n == 1:
        return False
    count = 2
    while count < n:
        if n % count == 0:
            return False
        else:
            count += 1
    return True

def sum_aliquots(n):
    '''
    returns the sum of the aliquots of a number
    '''
    aliquot_list = []
    for i in range(1, n):
        if n % i == 0:
            aliquot_list.append(i)
    total = 0
    for i in range(len(aliquot_list)):
        total += aliquot_list[i]
    return total

def equivalent_numbers(a, b):
    '''
    returns true if 2 numbers are equivalent, and false if they aren't
    '''
    a_sum = sum_aliquots(a)
    b_sum = sum_aliquots(b)
    if a_sum == b_sum:
        return True
    else:
        return False

def difference_nums(a, b):
    '''
    returns the difference between 2 numbers
    '''
    if a > b:
        return a - b
    else:
        return b - a

def top_pair(a, b):
    '''
    returns the pair with the two numbers that are farthest apart
    '''
    if difference_nums(a[0], a[1]) > difference_nums(b[0], b[1]):
        return a
    else:
        return b
    
def main():
    not_prime_nums = []
    for i in range(1, 2020):
        if not is_prime(i):
            not_prime_nums.append(i)

    all_equivalent_pairs = []
    for i in range(len(not_prime_nums)):
        num1 = not_prime_nums[i]
        count = i + 1
        for i in range(count, len(not_prime_nums)):
            if equivalent_numbers(num1, not_prime_nums[i]):
                pair = (num1, not_prime_nums[i])
                all_equivalent_pairs.append(pair)
    farthest_pair = all_equivalent_pairs[0]
    for i in range(1, len(all_equivalent_pairs)):
        farthest_pair = top_pair(farthest_pair, all_equivalent_pairs[i])
    print(farthest_pair)
                
    



if __name__ == "__main__":
    main()