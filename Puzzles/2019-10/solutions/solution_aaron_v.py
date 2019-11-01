x = 1
for i in range(2203):
    x *= 2
x -= 1

one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []

for num in str(x):
    if num == '1':
        one.append(num)
    if num == '2':
        two.append(num)
    if num == '3':
        three.append(num)
    if num == '4':
        four.append(num)
    if num == '5':
        five.append(num)
    if num == '6':
        six.append(num)
    if num == '7':
        seven.append(num)
    if num == '8':
        eight.append(num)
    if num == '9':
        nine.append(num)

num_pairs = 0

num_pairs += len(one) * len(nine)
num_pairs += len(two) * len(eight)
num_pairs += len(three) * len(seven)
num_pairs += len(four) * len(six)
for i in range(len(five)):
    num_pairs += i

print(num_pairs)
