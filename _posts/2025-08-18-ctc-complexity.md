---
layout: post
title: closed timelike curve complexity
subtitle: time travel as a computational resource? (pt 2)
tags: [complexity theory]
type: r
---
### Introduction
[In a previous post](https://chrissuu.com/bleu/2025-08-18-probabilistic-grandfathers/), we covered the Grandfather paradox and how it arises naturally when you allow a time machine to exist. 

We then made the claim that if we allow (your) existence to be stochastic, then we can resolve the Grandfather paradox, since the distribution is "fixed". (Note that if we had a biased existence, then it would once again create a Grandfather paradox.)

In this post, we use this idea of fixing distributions to resolve paradoxes to gain computational power when given access to a time machine that can time travel into the past!

### Closed Timelike Curves
A closed timelike curve (CTC) is a **mathematical artifact** of the theory of general relativity (GR). It is usually interpreted as one method of time travel **into the past**. Closed means that the curve is closed (or intuitively a loop), and hence if you treat time to be some "world" that you can walk in, you will eventually get back to where you started (think about how if you travel in one direction far enough on Earth, you will eventually come back to where you started).

**By mathematical**, we mean that GR permits closed timelike curves to exist (by analogy, it means that the theory of GR allows for time travel to exist).

**By artifact**, we mean that under the GR construction, CTCs are mathematically sound, but have the quality of requiring physically unnatural things (objects we don't expect to find or have yet to find in nature) such as negative mass or wormholes.

### CTC Turing Machine
David Deutsch showed that quantum mechanics could be used to resolve causality paradoxes created by the existence of CTCs and Scott Aaronson showed that CTCs could be used as a computational resource without creating causal paradoxes.

We first claim that for no causal paradoxes to occur, the computation you do must have an identical distribution to the one you started with before you executed your computation. In the Grandfather Paradox example, the computation you did was killing your grandfather. To resolve this paradox, some meta-universe flips a coin and declares your existence to be probabilistic (see more in my previous post). Therefore, regardless of whether you kill your grandfather or not, you still have a 1/2 probability of existing.

More importantly however, is the fact that the necessary distribution is not computed by you (i.e., you don't necessarily flip a coin or presuppose that you must exist with probability 1/2), but it is in fact causal consistency - that whatever you do inside a CTC must be consistent the next time you come around the loop.

In other words, there is some meta-universe turing machine (rules of nature, physics, or maybe God if you're religious) which finds this distribution for you.

In the grandfather paradox, the distribution was a uniform distribution conditioned on your existence.

We can use this idea to gain some computational advantage. 

### $$NP \subseteq P_{CTC}$$
Suppose we had access to a CTC, where we can send information back into the past.

Let $$P_{CTC}$$ be the set of languages computable in polynomial time when given access to a CTC. 

To show that $$NP \subseteq P_{CTC}$$, we can simply show that $$SAT \in P_{CTC}$$, since $$SAT$$ is NP-complete, and thus reduces all languages in the set NP.

We will construct a function, $$f$$, with the following definition. Let x be a boolean word which represents assignments to a logical formula (WLOG).

>(1)def f(x, $$\phi$$):
>
>(2)&emsp;&emsp;if x is a satisfying assignment for $$\phi$$:
>
>(3)&emsp;&emsp;&emsp;&emsp;return x
>
>(3)&emsp;&emsp;return (x + 1) mod (2 ** len(x))
>

Observe now the dynamics of causality with what our function computes.

Suppose $$\phi$$, such that $$\|\phi\| = n$$.

As before, we have two cases: one where $$\phi$$ is satisfiable, and one where $$\phi$$ is not satisfiable.

In the first, let $$W = \{w : w \in \{0,1\}^{n}\}$$ (i.e., the set of length n binary strings which represents our boolean assignments). Arbitrarily, suppose there was some distribution $$P_i(w)$$ on them. 

Now, note the following observation: when we compute $$x' = f(x, \phi)$$, $$x \neq x' \iff \phi(x)$$ is unsatisfied. Then, consider what happens to our probability distribution: $$P_{i+1}(x') = P_i(x)$$, which is not necessarily the same distribution! In fact, it will be a different distribution $$\iff P(x^{*}) < 1$$, where $$x^{*}$$ is a satisfying assignment. So the meta-universe enforces the distribution to have some dirac-like mass, where $$P(x^{*}) = 1$$ and $$P(x) = 0, x \neq x^{*}$$.

In the second case, well, it must be the case that since no satisfying assignments exist, to ensure that the probability masses don't move around when the function $$f$$ is computed and sent back in time, the meta-universe enforces that $$P(w) = \text{Uniform}(2^{n})$$.

In other words, each word is equally likely to be drawn from the distribution.

Now we can define the procedure for solving NP problems efficiently with CTC machines. 

First, for any arbitrary boolean formula of length $$n$$, $$\phi$$, pick your favorite length $$n$$ binary string.

<img class="button-press" src="../assets/button-ress-meme.jpg" width=200 style="float:right">
Pass it to the CTC and run this time machine. **Note that it's unclear** what this "run" step looks like. But maybe it's as simple as pressing a button and observing the output.


In any case, the CTC will return some assignment, $$e$$, which you will now verify against your formula $$\phi$$. If $$e$$ is a satisfying assignment to $$\phi$$, then we know that $$\phi$$ is satisfiable. Otherwise, $$\phi$$ is not satisfiable (this case is because unsatisfiable assignments only occur when sampling from the uniform distribution, which has no satisfying assignments to $$\phi$$ because $$\phi$$ is not satisfiable).


Since verification of $$SAT$$ instances can be done in polynomial time, $$NP \subseteq P_{CTC}$$!

### Conclusion
This blog post series was one of my favorites so far, and there's one more post in the series!

The next one will show that $$P_{CTC} = PSPACE$$, with $$PSPACE$$ widely believed to be a much stronger class than $$NP$$!

### References
>[David Deutsch, Quantum Mechanics of Time Travel](https://en.wikipedia.org/wiki/Quantum_mechanics_of_time_travel)
>
>[Scott Aarronson, Democritus](https://scottaaronson.com/democritus/lec19.html)

