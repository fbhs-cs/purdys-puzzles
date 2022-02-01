from math import ceil
def is_balanced(num):
    n = str(num)
    first = n[:ceil(len(n)/2)]
    last = n[len(n)//2:]
    #print(first,last)
    if sum([int(x) for x in first]) == sum([int(x) for x in last]):
        return True
    else:
        return False

def count_balanced(n):
    count = 0
    for i in range(1,n):
        if is_balanced(i):
            count += 1
    return count

def sum_balanced(n):
    total = 0
    for i in range(1,n):
        if is_balanced(i):
            #print(i)
            total += i
    return total

def find_balanced_dates():
    months = {1:31,2:28,3:31,4:30,5:31,6:30,
              7:31,8:31,9:30,10:31,11:30,12:31}
    count = 0
    sum = 0
    for month in range(1,13):
        for day in range(1,months[month]+1):
            day_num = str(month) + str(day) + '2022'
            if is_balanced(int(day_num)):
                count += 1
                sum += int(day_num)
                print(day_num)
                
    print(count)
    print(sum)
find_balanced_dates()
    
