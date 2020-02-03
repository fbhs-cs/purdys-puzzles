# Carlos Doble
def sum_digits(num):
    total = 0
    divisor = 1
    while True:
        if num//divisor > 0:
            total += num//divisor % 10
        else:
            break
        divisor *= 10
    return total
num = 1
for i in range(1, 2021):
    if i == 2020:
        print(num)
        print(sum_digits(num))
    if sum_digits(num) % 3 == 0:
        num += sum_digits(num)
    else:
        num += 1
    
    
    
    
