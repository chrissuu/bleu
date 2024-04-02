---
layout: post
title: the 301 aliens and 301 humans
subtitle: can you beat the aliens???
tags: [puzzle, math]
---

As a first semi-technical post, I thought I would talk about a very interesting problem/puzzle from a class I am taking this year, theoretical computer science! (Or at least a variation of it)

The question statement is as follows:

> Suppose there are 301 aliens and 301 humans. The aliens are in a room and in a single file line (they can't move from this order once in the room). Now the humans are waiting outside, and they are also in a line! One by one, a human walks inside the room, and the aliens (in their gibberish language) pick a representative amongst them to raise their hand. The human, in his infinite wisdom, gives the alien that raised their hand either a black hat or a red hat, and that alien has to wear that hat. 
>
> After telling the alien which hat to wear, the human exits the room, but can't communicate to his fellow earthlings waiting outside the room. This process goes on until 1 alien remains without a hat (if an alien has a hat already, they can't raise their hand a second time). This last alien is the **Alien Captain** who can chose what hat to put on.
>
> Finally, the last human walks in and has to pick a subset of the aliens that is guaranteed to contain the Alien Captain! The goal of this puzzle is to minimize the size of the subset the last human chooses. (Also the aliens know your strategy!!!)

### A naive solution emerges...

Let's think about the most basic solution to this problem. 

Let the humans randomly choose a hat, and then the last person picks all 301 aliens! If the last person picks all the aliens, obviously the Alien Captain would be one of them. 

Can we do better?

I'll remind you of the few restrictions we have:

1. We can't choose the order / which alien raises their hand (the aliens choose this)
2. We can't give any information outside of the initial planning phase to our fellow humans

Knowing this, what if the humans alternated assigning a red and black hat? Notice that we now have an invariant! Assigning the number $$i$$ to the ith human (for example the 1st human gets the number 1) that enters the room: # black hats - # red hats $$\equiv$$ $$i$$ mod $$2$$

Hence, after the 300th person assigns a hat to the 300th alien, # black hats - # red hats $$\equiv$$ $$300$$ mod $$2$$ which means # black hats - # red hats $$\equiv$$ $$0$$ mod $$2$$! When the Alien Captain takes his turn, he breaks this invariant! So the the last human can pick whichever of more hats there are. 

For example, after the 300th alien, there are 150 red hats and 150 black hats. Regardless of which hat the Alien Captain chooses, we get either 151 red hats and 150 black hats OR 150 red hats and 151 black hats! Then the human just chooses the 151 hats and it is guaranteed to contain the Alien Captain!

Good, we've now shown how to bring our subset size from 301 to 151! But can we do even better??

### Hats off! I've found you...

It's not immediately obvious if we can do better. After all, we can only encode so much information with just two hats at our disposal. But I will argue that that is enough hats!

Imagine if we can **"mark off"** certain aliens from being chosen at the end - as in, they are guaranteed not to be the Alien Captain. In the first example, that happened at the end when the captain chose his hat (and thus the opposite of his hat was guaranteed to not be the captain and hence all 150 of them were "marked off"). But this is sort of inefficient, don't you think? What if we can get more information dynamically instead of at the end?

Here is the strategy we came up with:

Split your aliens into n groups of k aliens (It's fine if your grouping has some stragglers). In my example below, I split it into groups of 30 so 1 will not be in a group. 

30 | 30 | 30 | ... | 30 | 1

Then, choose your favorite hat color. Mine is red. Now, as the humans walk in the room and as the aliens raise their hand, we will keep assigning red hats to them. UNTIL, there is a group (split as above) that has 29 red hats and the 30th alien in that group raised their hand. In which case, we will give that alien a black hat. We will say that the 1 straggler at the end always is assigned a black hat. By doing this, we have effectively "marked off" an entire group of 30 every time we assign a black hat! In other words, the Alien Captain will never be in a group of 30 that has an alien with a black hat!!

We will repeat this process until the Alien Captain goes. Here is where the magic happens. If the Alien Captain chose a black hat, then we know that there will be exactly 11 black hats (Since we never got to give the last group their black hat, so there were 10 black hats UNTIL the Captain goes and then makes it 11 black hats)! OR... if the Alien Captain chose a red hat, then we know that he is in the group with 30 red hats!!!

Magic!

We've brought our subset size from 301 -> 150 -> 30!!

Some careful readers might notice that we can do further optimizations. And yes this is true - but the strategy nevertheless is the same so I will leave that as an exercise :P

### The takeaway 

This is perhaps an example of a very unsuspecting generalization! If you notice carefully, the case where we assigned alternating hats is an example of our previous strategy for the case where the size of our groups is 2!

Moral of the story is to always be on the lookout for powerful generalizations you can make to simple concepts.  



### Reference: 

>[Wikipedia](https://en.wikipedia.org/wiki/Induction_puzzles#)