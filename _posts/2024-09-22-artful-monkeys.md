---
layout: post
title: artful monkeys
subtitle: the story of Monkey D. Shakespeare
tags: [math, probability]
type: r
---
### Introduction
The infinite monkey theorem says that a monkey (or infinite monkeys), given some finite time $$t$$ will eventually type out all of Hamlet. 

In this short blog post, we'll prove the general case.

### Formalization
We define an alphabet, $$\mathcal{A}$$ to be a finite set of symbols. Note that this definition is literally analogous to the alphabet we use everyday, just more general. In particular, it could be a set of any symbols, as simple as the digits from 1-9, or as complex as every symbol ever written by a human. 

We can now define a string to be a sequence of symbols coming from this set. Though this string can be infinite in length, we are interested only in the finite length strings. 

Formally, a string is defined to be $$s := s_1s_2s_3s_4...s_n$$ s.t. $$c_i \in \mathcal{A}$$

Now, we would like to some definitions so that we may formalize the problem statement.

Let $$M$$ be a machine that, at some time $$t_i$$, outputs a single symbol, from an alphabet $$\mathcal{A}$$ with equal probability. 

That is: $$\forall a_i \in \mathcal{A}, \textbf{Pr}\bigl[a_i \text{ is picked}\bigr] = \frac{1}{\textbf{card}(\mathcal{A})}$$

For example, in code, it could be implemented like so: 

>(1)def M(alphabet A):
>
>(2)&emsp;&emsp;rand_int = randint(0, len(A))
>
>(3)&emsp;&emsp;return A[rand_int]

Where $$\mathcal{A}$$ is a set-like list (no duplicate elements, but ordered).

Simply for closure, we will also include a special element in our alphabet, **EOF**, such that if the machine ever produces the **EOF** symbol, it will terminate all future actions. This helps us capture the notion of finite strings.

Lastly, we say that a machine $$M$$ **produces** a string $$s$$ iff for some time $$t_i, i \in [0, n)$$, that $$M(\mathcal{A}) = s_i$$ and at time $$t_{n}$$, $$M(\mathcal{A}) = \textbf{EOF}$$. 

In code, we could define it like so:

>(1)def M(alphabet A):
>
>(2)&emsp;&emsp;global produced_eof
>
>(3)&emsp;&emsp;if **not** produced_eof:
>
>(4)&emsp;&emsp;&emsp;&emsp;A = A $$\cup \text{ } \{\textbf{EOF}\}$$
>
>(5)&emsp;&emsp;&emsp;&emsp;rand_int = randint(0, len(A)+1)
>
>(6)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if rand_int = len(A) + 1:
>
>(7)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;produced_eof = True
>
>(8)&emsp;&emsp;&emsp;&emsp;return A[rand_int]
>
>(9)&emsp;&emsp;else:
>
>(10)&emsp;&emsp;&emsp;&emsp;return

### Problem Statement and Proof
>**Infinite Monkey Theorem** 
>
>Given $$N$$ machines $$M$$ as defined above, and an alphabet $$\mathcal{A}$$, there is an $$\epsilon$$ error that some machine $$M_i$$ will not produce the desired $$s$$. 

**Proof**

See that 

$$\textbf{Pr}\bigl[M_i(\mathcal{A}) \text{ outputs } s_j \text{ at time } t_j\bigr] = \frac{1}{\textbf{card}(\mathcal{A}) + 1}$$

This simply follows from how we defined the machine $$M_i$$. Then, it follows that:

$$\textbf{Pr}\bigl[M_i(\mathcal{A}) \textbf{ produces } s \bigr] = \prod\limits_{i=0}^{n} \textbf{Pr}\bigl[M_i(\mathcal{A}) \text{ outputs } s_j \text{ at time } t_j \bigr] = \frac{1}{(\textbf{card}(\mathcal{A}) + 1)^{n+1}}$$

The complement gives us:

$$\textbf{Pr}\bigl[M_i(\mathcal{A}) \textbf{ doesn't produce } s \bigr] = \textbf{Pr}\bigl[\overline{M_i(\mathcal{A}) \textbf{ produces } s }\bigr] = 1 - \frac{1}{(\textbf{card}(\mathcal{A}))^{n+1}}$$

Given $$N$$ machines that work independently, it must then be the case that the probability that these $$N$$ machines don't produce the string $$s$$ is the product of the individual probabilities of a machine $$M_i$$ not producing $$s$$. Fortunately for our machines (monkeys), $$\textbf{Pr}\bigl[M_i(\mathcal{A}) \textbf { produces } s] > 0$$.

$$\textbf{Pr}\bigl[N \text{ machines don't} \textbf{ produce } s \bigr] = \prod\limits_{i = 0}^{N-1} \textbf{Pr}\bigl[\overline{M_i(\mathcal{A}) \textbf{ produces } s }\bigr] = \bigl[ 1 - \frac{1}{(\textbf{card}(\mathcal{A}))^{n+1}} \bigr]^{N}$$

To complete the proof, we just have to show that these $$N$$ machines will produce $$s$$ with error at most $$\epsilon$$. This is equivalent to showing that $$\textbf{Pr}\bigl[N \text{ machines don't} \textbf{ produce } s \bigr] <\epsilon$$. We use a useful inequality: $$\forall x \in \mathbb{R}, 1 + x \leq e^x$$. 

Substituting $$x = - \frac{1}{(\textbf{card}(\mathcal{A}))^{n+1}}$$:

$$1 - \frac{1}{(\textbf{card}(\mathcal{A}))^{n+1}} \leq \textbf{exp}(-\frac{1}{(\textbf{card}(\mathcal{A}))^{n+1}})$$

This gives us:

$$\textbf{Pr}\bigl[N \text{ machines don't} \textbf{ produce } s \bigr]  = \bigl[ 1 - \frac{1}{(\textbf{card}(\mathcal{A}))^{n+1}} \bigr]^{N} \leq [\textbf{exp}(-\frac{1}{(\textbf{card}(\mathcal{A}))^{n+1}})]^N$$

The final nail in the coffin comes from the fact that if we bring the limit of $$N$$ to some arbitrarily large constant, the term $$[\textbf{exp}(-\frac{1}{(\textbf{card}(\mathcal{A}))^{n+1}})]^N$$ gets closer and closer to 0 (epsilon):

$$[\textbf{exp}(-\frac{1}{(\textbf{card}(\mathcal{A}))^{n+1}})]^N = \frac{1}{\textbf{exp}{[\frac{N}{(\textbf{card}(\mathcal{A}))^{n+1}}]}}$$

This is true as we have defined our alphabet to be finite, so the size of it is also finite. 


### How Many Monkeys Do We Need To Write Hamlet?

For some testing, let's see how many monkeys, I mean machines, we need to reasonably produce the entire text of Hamlet.

Using our final equation from above:

$$\textbf{Pr}\bigl[N \text{ monkeys don't} \textbf{ produce HAMLET} \bigr] \leq \frac{1}{\textbf{exp}{[\frac{N}{(\textbf{card}(\mathcal{A}))^{n+1}}]}}$$

Where $$n$$ is the length of Hamlet in number of characters. Thankfully, someone on GitHub has posted a txt manuscript of [Hamlet](https://gist.github.com/provpup/2fc41686eab7400b796b#file-hamlet-txt) and a simple python script let me count (approximately to about plus or minus 100 in error) the number of characters in Hamlet:

**171346**

Given our alphabet is $$26$$ characters, and say there are roughly about $$10$$ symbols for punctuation, that gives us an alphabet of roughly $$36$$ symbols :O

$$26^{171,346} \approx 2^{850,000}$$ is an insanely large number. We would need at a minimum that many monkeys such that the probability we don't produce Hamlet becomes roughly $$\frac{1}{e}$$.

To put that in perspective, there are only $$10^{80}$$ atoms in the universe. That means we need several magnitudes more monkeys than there are atoms in the universe just to have a $$50\%$$ chance of producing the entirety of Hamlet!

### Bonus Experiment

The cool thing about abstraction, however, is that we can also make our alphabet consist of **words** instead of the symbols that make up our alphabet. 

There are roughly $$170,000$$ words in the English language and according to my python script, about $$8,000$$ **unique** words in Hamlet.

For the same chance of producing Hamlet as above, we would need at least $$170,000^{8,000} \approx 2^{144,000}$$ monkeys. That is significantly less monkeys! 

Now, suppose we restricted our alphabet to ONLY the words that were used in Hamlet. How many monkeys would we need to guarantee about a $$50\%$$ chance? 

$$8,000^{8,000} \approx 2^{104,000}$$

### Final Remarks
Okay, that's enough experimenting... I honestly thought that final number would be a lot less, but it's still overkill... maybe next time I can try deriving the "almost Hamlet" property for infinite monkeys. That is, how many monkeys would I need to guarantee about a $$50\%$$ chance that they produce a text that is "almost Hamlet"?

### References

>[The guy on github that gave me a hamlet txt file](https://gist.github.com/provpup/2fc41686eab7400b796b#file-hamlet-txt)
>
>[The guy on reddit discovering infinity](https://www.reddit.com/r/Existentialism/comments/16hcfi6/no_fucking_chance_would_infinite_monkeys_with/)

<div class="author-box">Chris Su - Carnegie Mellon University - AI &amp; Computer Science</div>
