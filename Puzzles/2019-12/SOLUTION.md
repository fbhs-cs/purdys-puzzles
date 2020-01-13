## Solution to December 2019 Puzzle

## Answer: 28300 

### Part 1 Understanding the problem and developing an algorithm

According to the problem, we are looking for **all** 5 colors grouped together.  One way to approach this would be:

1. Start from the left side
2. Check the next 5 bulbs to see if they are each of the 5 colors.
    * If they are, count it and skip to the 6th bulb
    * If they aren't, move over 1 bulb
3. Repeat step 2 until we get to the end

[Here is my solution](./solutions/my_solution.py)
[Alex Billiot's solution](./solutions/solution.java)
[Devin Schwartz's solution](./solutions/devin_schwartz_sol.py)
[Andres Flores's solution](./solutions/december.java)
[Egor Mikhaylov's solution](./solutions/ClusterCounter.java)