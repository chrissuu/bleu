---
layout: post
title: mechanizing creativity
subtitle: the holy grail of computer science
tags: [cs, philosophy]
---
### Introduction

Imagine a world where creativity played no role in the problems we faced. 

To reason about this, let's think about creativity and its implications. Usually when we talk about innovation, we think about how a person has innovated something: this process is creative, since otherwise, everyone else would have come up with the same or similar idea (think Mark Zuckerberg or Jeff Bezos). When we talk about problem solving, we think about how the person who has solved the problem thought about said problem: this process is creative, since insights are needed to come up with solutions, otherwise everyone would have come to the same solution (Think Albert Einstein or Leonhard Euler)! Inherently, the process of thinking is creative and it's these tiny differences in imagination and creativity that allow people to solve very different problems and go into very different fields. 

But what would happen if this creative process was separate from thinking? That is, what if thinking didn't require creativity? Then there would be no merit in problem solving or innovation. Everyone, theoretically, would have the same ability to solve a certain problem or innovate a certain solution, given the right questions to ask.

At it's core this is what the P vs. NP question asks. It is perhaps just as fundamental to our universe as atoms are. 

### P vs. NP

The P vs. NP question asks the following: does every easily verifiable problem also have an efficient algorithm that solves that problem?

Although unsuspecting, the implications of a resolution to this problem are massive. We will focus our attention to the creativity aspect!

#### Unpacking some definitions

Let's talk about what an easily verifiable problem is. 

>**Definition**
>An easily verifiable problem is a problem whose solution can be checked quickly

The canonical example is usually Sudoku:

<p align = "center">
  <img src="../assets/sudoku.png" width = "400"/>
</p>

Although solving sudoku may be pretty challenging, if you were to give me the numbers to fill in, I could tell you pretty quickly if those were the solutions to the board! This makes Sudoku an easily verifiable problem. We usually say something is "easily" verifiable if it is "efficiently" verifiable. 

On the flip side, we also have a notion of an "efficient algorithm". You can sort of think of "efficient algorithm" as being a non brute force algorithm. That is, an algorithm that DOESN'T check all possible solutions to output the right one. For example in the sudoku board above, a brute force algorithm would be an algorithm that tries every single number 1-9 in every single box in every single way possible! (P.S, that is approximately 6,670,903,752,021,072,936,960 sudoku games just for a 9 by 9 board! Imagine if the board was just 10 by 10 or 100 by 100!)

### Mechanizing creativity

The first sparks of P vs. NP perhaps came from Hilbert's program through Kurt Gödel and John von Neumann. Today, it is one of the Clay Mathematics Institute's Seven Millenium Problems. Resolving any of one of seven problems (now six, after Gregori Perelman solved the Poincare Conjecture in the 2000s) earns the prover the bounty of a million dollars! (An image of Kurt Godel)

<p align = "center">
  <img src="../assets/kurtgodel.avif" width = "400"/>
</p>

We restate the problem: 

P vs. NP implies the following. If $$P = NP$$, then EVERY easily verifiable problem also has an EFFICIENT algorithm that solves that problem. If $$P \neq NP$$, then not every easily verifiable problem also has an efficient algorithm. That is to say, if $$P \neq NP$$, then some problems can only be solved by minute optimizations or brute force!

#### Implications
Now we can start looking into the implications of this problem! If $$P = NP$$, then easily verifiable problems also have efficient algorithms that solve that problem. In other words, any problem that you can easily verify should have a way for you to also solve it quickly!

Amazingly, this removes ANY sort of creativity in the problem solving process. A $$P=NP$$ resolution would mean that anyone that can ask the right questions could also prove these questions. Why?

Recall that proofs are simply chains of logical implications.

For example, suppose we had the following set of implications:

1. Today is Thursday, then today is sunny
2. If today is sunny, then the sun is out
3. If the sun is out, then the children are happy

Now suppose we wanted to prove that if today was Thursday, then the children are happy. The "proof" I would give you, is the order of the implications (1,2,3). Following them, you can see that if today is Thursday, then the children are happy. 

Most mathematical if not all mathematical proofs occur in the same way. Given some statement you want to prove, and some initial assumptions, show that that statement is true or false!

The "creative" part of this process is showing and coming up with these implications that get you from statement S to a true or false verdict V! Notice that this verification process of proofs is pretty fast! Just follow the implications and make sure that the logic is sound in each implications. If the implications eventually lead up to a verdict V, then we can say that this proof is correct! In other words, we can say that this verification process is efficient!

Notice however, that this is the EXACT problem statement seen in P vs NP!!!!!! 

Once again, I remind you what $$P=NP$$ implies: If $$P = NP$$, then EVERY easily verifiable problem also has an EFFICIENT algorithm that solves that problem. 

So, suppose $$P=NP$$.

Let problem P be your favorite problem (this can be anything, but I'll use an equally famous problem: the Riemann Hypothesis)

P = "Is the Riemann hypothesis true?"

Then, since the process of verifying proofs is efficient, we can expect that there is an efficient algorithm that solves the problem P, "Is the Riemann hypothesis true?", efficiently! So just plug P into this algorithm and return the output! No creativity needed here!

#### Nail in the coffin

Lastly, we put the final nail in the coffin to why P vs. NP is such an important question.

Usually, when we ask a question or have a problem, we don't want to just know if something is true or false! We want to know WHY it's true or false, or WHAT the proof is that something is true or false! In the above example, our efficient algorithm only returned True/False depending on whether P = "Is the Riemann hypothesis true?" was True/False. But what if I want **the proof** that the Riemann hypothesis is True/False? Is there a way to encode this information?

The answer is yes!

If $$P=NP$$, we know that every efficiently verifiable problem also has an efficient algorithm that solves that problem.

We can use this property to our advantage. 

We know that the proof that P is True/False is a string of characters, like the strings (1,2,3) above in the weather and children example.

Amazingly, we can find parts of our proof, bit by bit using the property that $$P=NP$$!!

Let's go back to the example.

Let P = "If today is Thursday, then the children are happy"
1. Today is Thursday, then today is sunny
2. If today is sunny, then the sun is out
3. If the sun is out, then the children are happy

If we're given the first implication 1 it is pretty easy to verify if this is PART of the proof for P! Perhaps going even smaller, we can ask if the letter "T" (the first letter of "Today") is part of the proof for P! And this would also be easy to verify. Hence, our algorithm will iterate over our alphabet, slowly building up our proof:

Is "A" the first letter of our proof? No? Is "B" the first letter of our proof? No? ... Is "T" the first letter of our proof? Yes! (Go to second letter) Is "A" the first letter of our proof? No? ... Is "o" the second letter of our proof? Yes! (Go to third letter) AND ETC!!!

In other words, given any problem whose truth or falseness can be verified efficiently, we can also output a PROOF that that problem is True/False EFFICIENTLY!!! Note that this is inherently different from a brute force solution, since in a brute force solution, we would have to try every single word and every single string. Here, we are basically only checking if a word is part of the solution, rather than finding the word that is the solution. 

In any case, we have completely removed creativity from problem solving!

### Overview

As we have seen, the P vs. NP problem is a fundamental question that has impacts in all aspects of our life! Though this overview of this problem was very specific to creativity, it only touches on the very tip (but perhaps a large tip) of a gigantic iceberg. A $$P=NP$$ resolution would most likely change our lives in drastic ways! Most problems we have would be efficiently solvable without much creativity as part of the process. Perhaps the most creative part about problem solving, then, would be posing the right questions. In fact, it is without a doubt that asking the right questions is perhaps just as important and insightful than answering them. 

In either case, because of these perhaps utopic consequences, most computer scientists believe P to be NOT EQUAL to NP. However, this question still sits as the holy grail of computer science - whose resolution, ironically, awaits a fateful encounter with an even more creative mind!

### References

>[Further reading (Wiki)](https://en.wikipedia.org/wiki/P_versus_NP_problem)
>
>[Knowledge, Creativity, and P vs NP](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/AW09/AW09.pdf)
