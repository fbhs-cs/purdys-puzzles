# February 2020 Puzzle Solution

## Understanding the problem

By definition:

```
The aliquot parts of a number are the proper divisors of that number that are less than the number.  
```

So we need to start by finding the proper divisors of a number.  This can be done using a loop:

for each number less than n:
    if n mod number is 0, it is an aliquot part

You would then need to keep track of the aliquot parts of a number to add them up.  You might keep track of these sums in a list or maybe even a dictionary.

After getting a list of equivalent numbers, you must find the pair with the largest difference between them.  

Here is [my solution](./solutions/equivalent.py).  Interestingly, a few of the student solutions below are faster than mine, so be sure to take a look at them as well!

## Student Solutions
[Alex Billiot's Solution (Java)](./solutions/FebPuzzle.java)
[Andres Flores's Solution (Python)](./solutions/Feburary.py)
[Devin Schwartz's Solution (Python)](https://repl.it/repls/GrayQuintessentialProprietarysoftware)
[Anthony Ciardelli's Solution (Python)](./solutions/febpuzzle.py)
[Aaron Vera's Solution (Python)](./solutions/feb20.py)