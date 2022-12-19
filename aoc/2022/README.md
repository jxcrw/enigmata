### 2022 Recap
My first official AoC :) . I had an absolute blast. Day 12 was the second day in a row that I got smoked by stuff I just don't know yet (yesterday modular arithmetic, today pathfinding algos), so I'm done competing for this year.

It's all stuff I'm super excited to learn but just don't have time to learn *right this second*. Need some time in the kitchen to add some more recipes to my DSA cookbook.

#### Key Takeaways
- Start each part of each puzzle with a fresh attitude.
- Stay calm no matter how easy the puzzle "should be".
- If something isn't working, just try something different.
- Don't try to reuse an old solution unless the puzzle is ___exactly___ the same (or you can't proceed otherwise).
- For any significantly complex puzzle, time spent building a nice visualization of app state is time well spent.

#### Results
- Global Ranking: TBD
- OSU Ranking: Hovered around 2nd-4th up to Day 12.

| Day |    Date    | P1 Time | P2 Time  | P1 Rank | P2 Rank | P1 Score | P2 Score |
|:---:|:----------:|:-------:|:--------:|:-------:|:-------:|:--------:|:--------:|
|  1  | 2022/12/01 |  5:12   |   8:09   |  2774   |  2894   |    0     |    0     |
|  2  | 2022/12/02 |  26:10  |  59:22   |  10372  |  14098  |    0     |    0     |
|  3  | 2022/12/03 |  12:36  |  18:47   |  4020   |  3399   |    0     |    0     |
|  4  | 2022/12/04 |  33:18  |  39:50   |  12242  |  11616  |    0     |    0     |
|  5  | 2022/12/05 |  40:53  |  46:01   |  8043   |  7540   |    0     |    0     |
|  6  | 2022/12/06 |  5:01   |   6:18   |  2028   |  2012   |    0     |    0     |
|  7  | 2022/12/07 | 2:57:20 | 3:07:13  |  15315  |  14529  |    0     |    0     |
|  8  | 2022/12/08 | 1:11:52 | 1:27:05  |  11784  |  9365   |    0     |    0     |
|  9  | 2022/12/09 |  55:25  | 3:24:36  |  7860   |  12401  |    0     |    0     |
| 10  | 2022/12/10 |  15:24  |  38:51   |  2557   |  3581   |    0     |    0     |
| 11  | 2022/12/11 |  38:40  | 14:22:30 |  3087   |  30188  |    0     |    0     |


### Solution Log / Notes
#### [Day 1: Counting Calories](https://adventofcode.com/2022/day/1)
Felt so nice to let hair down a little and write some fast and dirty code :) .


#### [Day 2: RPS](https://adventofcode.com/2022/day/2)
Spent most of my time trying to reuse code from an old Rock, Paper, Scissors, Lizard, Spock game I wrote about a year ago. Its one neat feature was that it didn't use any conditional logic whatsoever - all the logic is baked into classes/data structures.

Again, like on day 1, I'm loving how out of control you can get on these AoC puzzles. I _never_ get to write code this fast/bad anywhere else :) .


#### [Day 3: Rucksack Reorg](https://adventofcode.com/2022/day/3)
Starting to achieve a little bit of composure within the chaos. This AoC thing is kind of a freaking blast.


#### [Day 4: Camp Cleanup](https://adventofcode.com/2022/day/4)
Got confused on edge cases in P1, then got super frustrated that I was confused. "This is a simple intervals problem...I should be smoking this simple intervals problem...why am I not smoking this simple intervals problem?!?!?"

Took negativity from P1 into P2, which could have been an easy score if I'd let it be, even after flubbing P1. Takeaways:

- Always stay positive and keep a clear head. It doesn't matter how easy you think the problem "should be".
- If you get stuck, don't get upset that your code "should be" working. Just try something different.
- Start each part with a fresh attitude. What happened on P1 has (almost) nothing to do with P2.

Disappointing rookie mistakes :( , but many learnings learned :) .


#### [Day 5: Supply Stacks](https://adventofcode.com/2022/day/5)
Fun puzzle. Not much to say. I was slow :) . Interesting that the top 100 solve times spanned a much wider range than on past days (almost 5 min gap between r1 and r100). I think this means that like me, most people struggled to get the initial state of the crates into a usable format.

Liked that this puzzle wasn't just straight DSA - had an element of "how good are you with your editor?" I just switched from Sublime/IntelliJ to Neovim within the past two weeks, so for me the answer is "appallingly bad" :) .


#### [Day 6: Tuning Trouble](https://adventofcode.com/2022/day/6)
Fun little puzzle. Behold the birth of the Slindow! Also, first day solving whole thing in Neovim without resorting to Sublime/IntelliJ :) .


#### [Day 7: No Space Left On Device](https://adventofcode.com/2022/day/7)
Ssststrugglebusss. Tried naive string parsing. Nope. Spent a bunch of time thinking about tree structures and how to convert input data into a tree representation. Too much work. Tried fancier string parsing with regex. Nope.

It only took me three hours to think of just converting the puzzle input to a shell script, running it to build out an analog of the file structure on my own machine, and then doing easy `os.walk()` stuff that I've done a thousand times before. Done :) .

This was a seriously amazing puzzle. For me, it kind of broke the "fourth wall" of coding puzzles and got me thinking outside of the puzzle code itself (which, until today, always lived strictly inside of my IDE).

Very curious to see how other people approached this one.


#### [Day 8: Treetop Treehouse](https://adventofcode.com/2022/day/8)
Okay, I officially have a bad habit - trying to reuse old code where I probably shouldn't. Here, I recognized that the problem was similar to [LeetCode 417. Pacific Atlantic](https://leetcode.com/problems/pacific-atlantic-water-flow/), and so I spent far too long trying to reuse my solution from there. This is probably the third or fourth day I've done something like that.

Today's puzzle was pretty fast and straightforward if you just actually read the description - a tree is visible if it's visible from ___any___ direction. It doesn't have to be visible from ___all___ directions (which is essentially what the Pacific Atlantic algo does).

So, moving forward I think that at least for timed/ranked solves, I should never try to reuse an old solution unless the problem is ___exactly___ the same (or the problem is so heinous that I need the old solution just to move forward at all).


#### [Day 9: Rope Bridge](https://adventofcode.com/2022/day/9)
Got part 1 despite having a sneaky bug that blew up quite impressively in part 2. Took hours to figure out what was going on.

The lesson here for me was that for any significantly complex puzzle, building a nice visualization of app state can be time well spent. Rather than going "well shoot, `knots[0][0]` should be `5` and `northwest` should be `True` and blah blah blah...", I could just go "well shoot, my rope broke".


#### [Day 10: Cathode-Ray Tube](https://adventofcode.com/2022/day/10)
Absolute blast of a puzzle. Seeing my 8 capital letters pop up on screen filled me with childlike joy.


#### [Day 11: Monkey in the Middle](https://adventofcode.com/2022/day/11)
Heinous day. Spent far too long chasing elaborate ways to work around the fact that my modular arithmetic isn't very good yet. In the end, caved and had to look up a hint for part 2, which felt gross. Hours of effort on a sweet `FactoredNum` class thrown away for two measly lines of code.

It's a real shame too because I'm just a few weeks away from the modular arithmetic stuff in discrete math.
