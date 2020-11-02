# October 2020 Solution

## Understanding the problem
At first glance, the images may not give any information.  But the entire message is hidden in the COLORS of the images!

Colors in a computer are usually stored in group of 3 values representing the amount of red, green, and blue in a particular color.  These are called RGB values.  If you take the image one pixel at a time and examine the RGB values of the colors, you will find a list of values:
```
(73, 32, 98, 255)
(101, 116, 32, 255)
(121, 111, 117, 255)
(32, 100, 105, 255)
(100, 110, 39, 255)
(84, 32, 107, 255)
(110, 111, 119, 255)
(32, 116, 104, 255)
(97, 116, 32, 255)
(121, 111, 117, 255)
(32, 99, 111, 255)
(117, 108, 100, 255)
(32, 101, 110, 255)
(99, 111, 100, 255)
(101, 32, 97, 255)
(32, 109, 69, 255)
(115, 115, 97, 255)
(103, 101, 32, 255)
(117, 115, 105, 255)
(110, 103, 32, 255)
(111, 110, 76, 255)
(121, 32, 99, 255)
(111, 76, 111, 255)
(114, 115, 46, 255)
(32, 32, 85, 255)
(110, 102, 111, 255)
(114, 116, 117, 255)
(110, 97, 116, 255)
(101, 108, 121, 255)
(44, 32, 116, 255)
(104, 105, 115, 255)
(32, 77, 101, 255)
(115, 115, 97, 255)
(103, 101, 32, 255)
(105, 115, 32, 255)
(110, 111, 116, 255)
(32, 116, 104, 255)
(101, 32, 115, 255)
(111, 108, 117, 255)
(116, 105, 111, 255)
(110, 32, 116, 255)
(111, 32, 116, 255)
(104, 105, 115, 255)
(32, 112, 117, 255)
(122, 122, 108, 255)
(69, 46, 32, 255)
(32, 84, 111, 255)
(32, 105, 100, 255)
(101, 110, 116, 255)
(105, 102, 89, 255)
(32, 116, 104, 255)
(101, 32, 115, 255)
(79, 108, 117, 255)
(116, 105, 111, 255)
(110, 44, 32, 255)
(121, 111, 85, 255)
(32, 110, 101, 255)
(101, 100, 32, 255)
(116, 111, 32, 255)
(115, 99, 82, 255)
(117, 116, 105, 255)
(110, 105, 122, 255)
(101, 32, 101, 255)
(118, 101, 114, 255)
(121, 32, 108, 255)
(101, 116, 116, 255)
(101, 114, 32, 255)
(97, 78, 100, 255)
(32, 102, 105, 255)
(110, 100, 32, 255)
(65, 108, 108, 255)
(32, 111, 102, 255)
(32, 116, 104, 255)
(101, 32, 77, 255)
(97, 110, 121, 255)
(32, 112, 69, 255)
(99, 117, 108, 255)
(105, 97, 114, 255)
(105, 116, 105, 255)
(101, 115, 46, 255)
```
Notice that the last value in each is 255.  This is called the Alpha value and can be ignored (since they are all the same, it is PROBABLY safe to assume they don't affect the puzzle).

## Solving the puzzle
If look at just the RGB values, you see the first few are 73, 32, 98, 101, 116, 32.  Seeing that number 32 twice in the first few values might set off alarm bells (or maybe not).  It is at this point that you need some understanding of an encoding system called ASCII.  ASCII gives each symbol on the keyboard a numeric value.  32 coincides with a space (" ").  65 is a capital A, and so on.  You can see the ASCII table [here](http://www.asciitable.com/).  

Going through and turning these values into their ASCII counterparts results in the following message: 

`I bet you didn'T know that you could encode a mEssage using onLy coLors.  Unfortunately, this Message is not the solution to this puzzlE.  To identifY the sOlution, yoU need to scRutinize every letter aNd find All of the Many pEculiarities.`

As it says, there are some letters that are different in the message: they are capitalized incorrectly.  Those letters are:
`TELLMEYOURNAME`.  

The answer to this puzzle was just that, your name.

[Here is a link](https://repl.it/@ChadPurdy/October2020Puzzle-Solution) to a program that solves the puzzle using Python. 

[Here is Sam Zhang's explanation](./sam_zhang_sol.txt) of how he went about solving it without any programming at all!
