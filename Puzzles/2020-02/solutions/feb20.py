# Aaron Vera

llist = []

### adds all aliquot parts to a lst ###
for i in range(0,2020): 
    temp = 0
    for j in range(i-1,1,-1):
        if ( i % j == 0):
            temp += j
    llist.append(temp)
    temp = 0

#checks for equal AP's starting at the front and end of list and finds which ones have the greatest distances
max_diff = 0   
final_pair = [] 
for i in range(len(llist)): 
    for j in range(len(llist)-1,-1,-1):
        if llist[j] == llist[i] and llist[j] !=0 : #finds first and last instance of AQ thats non prime
            differance = abs(i - j)

            if  differance > max_diff: # sets new max distance
                max_diff = differance
                final_pair = []
                final_pair.append(i)
                final_pair.append(j)
                break

print(final_pair)


        


