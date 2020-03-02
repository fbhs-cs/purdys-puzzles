#Anthony Ciardelli

def aliquot(num):
    factors = []
    for i in range(1,num-1):
        if num % i == 0:
            factors.append(i)
    Sum = sum(factors)
    return Sum

def equivalent(num1,num2):
    Sum1 = aliquot(num1)
    Sum2 = aliquot(num2)
    if Sum1 == Sum2:
        return True

def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

def main():
    largest = 0
    numberuno = 0
    numberdos = 0
    for i in range(1,2021):
        num1 = i
        for z in range(1,2021):
            num2 = z
            if equivalent(num1,num2) == True:
                if num1 != num2 and is_prime(num1) == False and is_prime(num2) == False:
                    distance = abs(num1 - num2) 
                    # print(f'{num1}, {num2}: {distance}')
                    if distance > largest:
                        largest = distance
                        numberuno = num1
                        numberdos = num2
                    else:
                        continue         
                else:
                    continue

            else:
                continue
    print(f'{numberuno} - {numberdos}, {largest}')
    


        

# equivalent(10,9)  
main()
# is_prime(6)


