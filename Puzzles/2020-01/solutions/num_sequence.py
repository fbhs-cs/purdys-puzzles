# Purdy
'''
The first 15 numbers of a particular sequence of integers are:

1, 2, 3, 6, 12, 15, 21, 24, 30, 33, 39, 51, 57, 69, 84...

The 100th number in the sequence is 1131

The 1000th number in the sequence is 16872

What is the sum of the digits in the 2020th number in the sequence?
'''

def get_digits(num):
    return [int(n) for n in list(str(num))]

def get_seq(size):
    my_seq = [1,2]

    while len(my_seq) < size:
        next_ele = 0
        for val in my_seq:
            next_ele += sum(get_digits(val))
        my_seq.append(next_ele)
    print(next_ele)
    return my_seq

#print(get_seq(10))
get_seq(2020)


