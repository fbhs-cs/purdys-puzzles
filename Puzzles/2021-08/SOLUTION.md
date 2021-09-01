# August 2021 Puzzle Solution

## WELCOMEBACKHORNETS
---
## Explanation

Start by mapping the alphabet to the numbers 1-26:
```
A B C D E F G H I J  K  L  M  N 
1 2 3 4 5 6 7 8 9 10 11 12 13 14 

O  P  Q  R  S  T  U  V  W  X  Y  Z
15 16 17 18 19 20 21 22 23 24 25 26
```
Original Message with its numeric value and the location of each letter numbered 
```
X  G O  G T  S  L  J  J  M  V  T  B  F  C  U  K  K 
24 7 15 7 20 19 12 10 10 13 22 20 2  6  3  21 11 11

1  2 3  4 5  6  7  8  9  10 11 12 13 14 15 16 17 18
```
Now, subtract the location number from each letter's numeric value.
If the result is negative, add 26 (so the letters effectively "wrap around").
Convert the resulting number back into a letter using the original mapping.

```
23 5 12 3 15 13 5 2 1 3 11 8 15 18 14 5 20 19
W  E L  C O  M  E B A C K  H O  R  N  E T  S
```

