

def next_pattern(num):
    num = str(num)
    i = 0
    result = ''
    while i < len(num):
        curr = num[i]
        curr_count = 1
        while i + 1 < len(num) and curr == num[i+1]:
            curr_count += 1
            i += 1
        result += str(curr_count) + curr
        i+= 1
    return result

def nth_pattern(start, n):
    pattern = [start]
    curr = 0
    while curr < n-1:
        pattern.append(next_pattern(pattern[curr]))
        curr += 1
    return pattern

def num_ones_in(start, n):
    pattern = nth_pattern(start,n)
    last = pattern[-1]
    num_ones = last.count('1')
    print(f"{n}th value: {last}")
    print(f"There are {num_ones} in the {n}th value")
    

num_ones_in(3.14,10)
