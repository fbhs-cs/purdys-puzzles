# Andres Flores

def main():
    lis = []
    
    for num in range(0,2020):
        if is_prime(num) == False:
            lis.append([num,factors(num)]) # create list filled with non-prime numbers and their aliquot sums
    
    count_list = []
    count_list2 = []
    for i in range(len(lis)):
        count = 0
        for j in range(i + 1, len(lis)):
            if lis[i][1] == lis[j][1]:
                count_list.append([i,j])
                count_list2.append((j-i))
            # count += 1

    m = max(count_list2)
    print([i for i, j in enumerate(count_list2) if j == m]) # give the location of the farthest matching aliquot sums in count_list2
    print(count_list[48])
    print(count_list2[48])
    print
    print("The pair of numbers are " + str(lis[50][0]) + " and " + str(lis[1658][0]))
    # print(lis[50][0])
    # print(lis[1658][0])

def factors(x):
    temp_list = []
    sum_list = 0
    for i in range(1, x):
        if x % i == 0:
            temp_list.append(i)
    for num in temp_list:
        sum_list += num
    return sum_list

def is_prime(n):
    upper_bound = int(n ** 0.5) + 1
    for i in range(2,upper_bound):
        if n % i == 0:
            return False
    return True
    
if __name__ == "__main__":
    main()