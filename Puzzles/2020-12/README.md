# December 2020 Puzzle

## Santa's GPS

Santa's GPS is broken, oh no!!  And wouldn't you know it, his sleigh is on the fritz, and he can only carry one household's presents at a time!  But Bernard (Santa's chief elf) has a plan.  

When Santa gets to a city, he will setup a magic teleporter which can be used to get presents one household at a time.  Bernard will then send good ol' St. Nick instructions to get to that house.

To make things easy, Bernard will send a message consisting of combinations of the characters N, E, S, and W, each representing the four cardinal directions.  To allow for as much precision as possible, each of the characters will indicate that Santa should move 100 yds in that direction.  

For example, the message `NNNEEEE` would tell Santa to move 300 yds north, then 400 yds east, a total of 700 yds.  When he reaches a destination he will drop off the presents, then fly straight back to his teleporter.  This example would result in a total of 1200 yds (0.682 miles) travelled.  

In order to speed things up, Bernard is going to send all of the directions for a given city at once.  Each house will be separated by a `;` character.  Unfortunately, since Bernard has to communicate all the way from the North Pole, the aurora borealis causes some static interference.  This means that the instructions may sometimes come through with additional symbols or characters.  Anything that is not a direction or a ; should be ignored.

Also, Bernard isn't the best with directions, so sometimes Santa may end up doubling back on himself (ie. going back in a direction he already came).  It's even possible that there are houses directly under his teleporter!  

To test the system, Santa and Bernard decide to try it out in a small neighborhood (only 4 houses).  The directions file for the small neighborhood is [here](small.txt).  They discover that Santa travels a total of 2323.607 yds (1.3 miles) and the farthest house from his teleporter is 300 yds (0.2 miles).

After a successful trial run, Bernard and Santa decide their system seems great, and decide to go to a larger city (though not too large!)

Bernard's instructions for Corpus Christi are in the [directions](corpus.txt) file. 

For Corpus Christi, what is the **sum** of the *total* distance that Santa Clause will have travelled when he finishes delivering *all* of the presents, and the *farthest* house from Santa's teleporter, to the nearest tenth of a mile?
