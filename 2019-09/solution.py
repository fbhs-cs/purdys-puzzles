with open('2019_08_09_puzzle.txt') as file:
    lines = file.readlines()
    code = ""
    for line in lines:
        code = code + line.strip()
    
    # loop solution (traditional)
    for i in range(len(code)):
        if i % 28 == 0:
            print(code[i],end='')
    print()
    
    # one-liner
    print(code[::28])    