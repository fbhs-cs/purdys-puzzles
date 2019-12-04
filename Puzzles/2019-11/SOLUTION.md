## Solution to October 2019 Puzzle


### Part 1 - Understanding the problem & looking for a pattern
If you take a look at a calendar, it's pretty easy to see what the dates of Black Fridays in recent past and futures will be:
```
...
11/29/13
11/28/14
11/27/15
11/25/16
11/24/17
11/23/18
11/29/19
11/27/20
11/26/21
11/25/22
11/24/23
11/29/24
...
```

It looks like the day numbers are counting **down** from 29 to 23 then resetting back to 29.  Every once in a while it skips a year though.  Years 16, 20, and 24 all skip to the next year.  That's because they are **LEAP YEARS**.  

## Part 2: Applying the pattern

We are told that in the year 2, Black Friday was on 11/29/02.  Which means, the first few years would be:
```
11/29/02
11/23/03
11/25/04    (leap year)
11/26/05
11/27/06
11/28/07
11/23/08    (leap year)
...
```

So we need to continue increasing the year number by 1, checking if it's a leap year.  If it's a leap year, increase the day number by 2, otherwise increase the day number by 1.  If the day number is 30, reset it  back to 23, if the day number is 31, reset it back to 24.  Check if both the year number and day number are prime.

Repeat 3000 times!

[Check out some solutions](./solutions/)



