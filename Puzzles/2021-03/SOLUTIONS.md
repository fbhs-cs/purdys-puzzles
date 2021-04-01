# March 2021 Puzzle Solutions

## Answer:
250969 three-leaf clovers
53 four-leaf clovers
13 five-leaf clovers


## Student solutions:
### Devin Schwartz
[Python program](https://replit.com/@DevinS73/marchpuz)


### Xander Nguyen
> I wrote a system of equations to get a general idea for the numbers. 
>
> y= x/5000
> z = x/20000
> 3x + 4y + 5z = 753184
>
> Where x is the number of 3 leafed, y is 4 leafed, z is  5 leafed. 
> The system solved for x=250973 y = 50.2 and z = 12.5. I pulled up a 
> list of prime numbers and found the one closest to 250973, rounded 
> 50 to the nearest prime, and finally rounded 12.5 to the nearest 
> prime.

### Alex Xie
> This puzzle was much easier than I thought. I had no idea what to do because I realized that the question stated "a little more than 5000" and "about 20,000". There was no way I would be able to technically get a direct answer. But I tried to do it using Algebra anyways. I first named 3-leaved clovers x, 4-leaved clovers y, and 5-leaved clovers z. The first equation I made was y = x/5000. The second equation I made was z= x/20000. Then I used some risky combination to make 3x + 4x/5000 + 5x/20000 = 753184 to convert the number of clovers to the number of leaves. I just solved it with an nSpire. Of course, this gave me a decimal number. I used a random prime checker that I found on the browser to check the number I got(without decimals). Annnnnnnnd, it was useless, as 250973 is divisible by 31. Alas, I kept it as a base number to work around. While I was at it, I estimated the number of four-leaved and five-leaved clovers. I got approximately 50 four-leaf clovers and 12 five-leaf clovers. I then found the closest prime number to the estimated number of three-leaf clovers which was 250969(by trying numbers again by using the prime numbers). I simply multiplied that by 3 and subtracted it from the total number of leaves. After a bit of trying, I used 53, the closest prime to 50 and 13, the closest prime to 12. I tried it, and it worked. Then I decided to figure out what you meant by “a little over” or “about”. I divided the number of four and five-leaf clovers by the number of three leaf-clovers and got about 0.000211 for four-leaf and 0.000052 for five-leaf clovers which means that my answer works. Three-leaf clovers = 250969; Four-leaf clovers = 53; Five-leaf clovers =13.
Sorry if we were supposed to solve this by programming. I suppose we were supposed to code it using integer division(//). But then I realized that it probably would’ve been way faster to have used algebra and some checking because I’m not that good at coding yet. Setting up the equation and checking the numbers that fit probably only took me 15 minutes.

### Samuel Zhang
> Too lazy to code. Basically, every 20,000 clovers have 4 four-leaf clovers and 1 5-leaf clover for 6 extra leaves, so there are 60,006 leaves. 753,184/60,006 gives you 12 remainder 33112.
> Current number of clovers:
> 3-leaf: 239940
> 4-leaf: 48
> 5-leaf: 12
> 
> 33112 leaves /3 is around 10,000 clovers meaning out of those, there will be 1 4 leaf and the rest 3 leaf.
> So
> 3: 242699
> 4: 49
> 5: 12
> 
> The nearest primes were 242713, 53, and 13, so I try that.
> 3: 242713
> 4: 53
> 5: 13

> This adds to 728416, 24768 off.
> So if I assume the rest (8256 clovers) are all 3s (because the power of probability).
> 3: 250969
> 4: 53
> 5: 13
> 
> Magic. I check to see if 250969 is prime and it is. I check on github it works. The number of leaves adds up to 753184.
> 
> Final Answer:
> three-leaf clovers = 250969
> four-leaf clovers = 53
> five-leaf clovers = 13
