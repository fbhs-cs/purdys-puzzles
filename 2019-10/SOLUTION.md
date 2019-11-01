## Solution to October 2019 Puzzle


### Part 1 - Understanding the problem
Here is the basic algorithm:
1. Get the first digit of the number
2. Add that digit to each digit of the number, one at a time
    * If the sum is 10, count it
3. Repeat for the second, third, fourth, and so on

3575 would look like this:
```
# First number
3 + 5 = 8 (not 10)
3 + 7 = 10 (count it!)
3 + 5 = 8 (not 10)

# Second number
5 + 7 = 12 (not 10)
5 + 5 = 10 (count it!)

# Third number
7 + 5 = 12 (not 10)

So there are 2 cases where the digits add up to 10.
```

### Part 2 - Applying the understanding
This problem would be **extremely** tedious to do without a computer, though I suppose it could be done.  While, as always, there are multiple approaches (see the different [solutions](./solutions/)), the most straight-forward method would probably to use a "nested loop".  See either [my java solution](./solutions/OctoberSolution.java) or [my python solution](./solutions/solution.py) to see what I mean.