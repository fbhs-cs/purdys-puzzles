## Solution to January 2020 Puzzle

### Part 1 Understanding the problem and developing an algorithm

According to the problem, the first 15 numbers in the sequence are:

```
1, 2, 3, 6, 12, 15, 21, 24, 30, 33, 39, 51, 57, 69, 84...
```

To solve this, we first need to identify a pattern:

```
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 6 = 12
1 + 2 + 3 + 6 + 1 + 2 = 15
1 + 2 + 3 + 6 + 1 + 2 + 1 + 5 = 21
1 + 2 + 3 + 6 + 1 + 2 + 1 + 5 + 2 + 1 = 24
...
etc.
```

In other words, the next number is the sum of ALL of the previous digits in the sequence.

The 2020th number ends up being `37194`, the sum of whose digits is **24**.


### Coding a solution

There are multiple ways to get the sum of the digits from a given number.  One way might be...
``` python
digit_sum = 0
while num > 0:
   digit_sum += num % 10
   num = num // 10
```

Another might be to treat the number as a string, then sum the digits:
``` python
digit_sum = 0
for letter in str(num):
    digit_sum += int(letter)
```

The programming language Scratch treats all values as if they are numbers OR strings based on the operations.  A few people used this to their advantage:

[Sean Coggins' Solution](https://scratch.mit.edu/projects/362393422)


See the other [solutions in Java and Python here](./solutions/).
