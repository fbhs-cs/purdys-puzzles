hex_vals = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, \
            '7':7, '8':8, '9':9, 'a':10, 'b':11, 'c':12, 'd':13, \
            'e':14, 'f':15}

def hexToDec(hex):
    ans = 0
    index = 0
    for i in range(len(hex)-1,-1,-1):
        ans += hex_vals[hex[index]]*(16**i)
    return ans

def hex_persistance(num):
    p = 0
    while len(num)>1:
        ans = hex_vals[num[0]]
        for i in num[1:]:
            ans *= hex_vals[i]
        p += 1            
        num = "%x" % ans
        print(num)
    return p

def persistance(num):
    p = 0
    while len(num)>1:
        #print(num)
        ans = int(num[0])
        for i in num[1:]:
            ans *= int(i)
        p += 1            
        num = str(ans)
        #print(num)
    return p

def smallest_persistance(p):
    num = 0
    while True:
        if hex_persistance("%x" % num) == p:
            return "%x" % num
        num += 1
            