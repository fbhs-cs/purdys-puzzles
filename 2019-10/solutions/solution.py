## Author - Chad Purdy
## Date: 10-1-2019

example_number = str(2**2203-1)
#print(example_number)
count = 0
for i, v in enumerate(example_number):
    for j, w in enumerate(example_number[i+1:]):
        if int(v) + int(w) == 10:
            #print(v, w)
            count += 1

print(count)