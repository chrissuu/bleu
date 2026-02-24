---
layout: post
title: your time is taking up my space!
subtitle: time travel as a computational resource? (pt 3)
tags: [complexity theory]
type: r
---
### Introduction
To finally wrap up this series, we will finally talk about one of the more interesting results equating polynomial time CTC machines with the complexity class, PSPACE!

### PSPACE
PSPACE is the complexity class containing languages that can be computed with polynomial space. Even intuitively, you might see why this class contains powerful languages.

Observe that because proofs for instances of $$NP$$ languages is bounded by polynomial length, $$NP \subseteq PSPACE$$ since we can simply loop over all proofs for an instance of your favorite $$NP$$-complete language and see which proof allows the instance to be accepted (and if none, then reject).

The key observation is that space, unlike time, is reusable, and so we can simply overwrite the existing bits on the tape when looping over proofs. Note that this is one key piece of intuition for why $$P_{CTC} = PSPACE$$.

We can also look into languages that are $$PSPACE$$-complete.

### $$P_{CTC} \subseteq PSPACE$$
We begin the proof by showing that $$P_{CTC}$$ is contained within $$PSPACE.$$
The intuition here is as follows.

Suppose we have a language $$L \in P_{CTC}.$$ On an input of length $$n,$$
the CTC machine for $$L$$ can be modeled by a polynomial-size circuit
$$C : \{0,1\}^m \to \{0,1\}^m,$$
where $$m = \mathrm{poly}(n)$$ represents the number of bits in the CTC register.

This circuit defines a deterministic map on a finite set of size $$2^m.$$
Any sequence $$x, C(x), C^2(x), \ldots$$
must eventually repeat, and hence there exists some finite $$k \le 2^m$$
such that $$C^k(x) = x.$$ Note that this is true due to the pigeonhole
principle. Equivalently, we can say that each trajectory under applications
of $$C$$ will enter a cycle.

To find a stationary distribution, we need only identify such a cycle:
for any $$x$$ that satisfies $$C^k(x) = x,$$
the set of states in that cycle forms a self-consistent collection of
CTC states. Assigning uniform probability mass to those states yields
a stationary distribution, since the probability mass cannot flow out of the cycle.

Finding this $$x$$ is a $$PSPACE$$ computation, since $$x$$ and computations
related to it are polynomially-**space** bounded. This is because we can reuse space
for all inputs $$x$$ (probably by additionally having some auxiliary bits
storing which states we've been in).

Therefore, every language decidable by a polynomial-time CTC machine
can also be decided in $$PSPACE,$$ and hence
$$P_{CTC} \subseteq PSPACE.$$

### $$PSPACE \subseteq P_{CTC}$$
To see why this is true, we define the following procedure:

First, let $$M$$ be some machine which computes a PSPACE language, $$L$$.

Next, suppose we want to decide whether $$x \in L$$ or not. 

Let $$M_i$$ represent the $$i$$th state of machine $$M$$ while it is computing
$$M(x)$$. Let $$M_{acc}, M_{rej}$$ be the accepting and rejecting states of $$M$$.

Now, we introduce some extra bit, $$b$$, about whether this computation has accepted
or not. 

In particular, we define a new function, $$f$$, which computes the following:

>(1)def f($$M_i$$, b):
>
>(2)&emsp;&emsp;if $$M_i$$ == $$M_{acc}$$: return <$$M_0$$, 1>
>
>(3)&emsp;&emsp;elif $$M_i$$ == $$M_{rej}$$: return <$$M_0$$, 0>
>
>(3)&emsp;&emsp;else: return <$$M_{i+1}$$, b>
>

Like before, we will now analyze what the stationary distribution over this
playout looks like. Suppose that $$M(x)$$ accepts. In this case, we
observe the following behavior from $$f$$:

1. $$f(M_i, b)$$ will eventually be 1.
2. $$f(M_i, 0)$$ will eventually be 1.

In other words, no matter the (tuple) input, after the computation ends,
bit $$b$$ will be set to the result of $$M(x)$$. This holds even if 
$$f$$ was given the negation $$M(x)$$. 

Hence, for this to be causally / distributionally consistent,
the universe will require a uniform distribution over the
states involved in the computation of $$M(x)$$,
but with $$b$$ set to the result of $$M(x)$$.

If $$b$$ was not set to the result of $$M(x)$$, or we had
nonzero probabilities assigned to both
$$b = 0$$ and $$b = 1$$, then observe that the probability
masses would eventually shift back to whichever of $$b$$ was
the result of $$M(x)$$, hence breaking probabilistic causality. 

For our procedure, all we must do is thus run our CTC (which like
the previous post, we have no idea what this would look like), and
then read our bit $$b$$, which is exactly the result of $$M(x)$$. 

### Conclusion
As Scott Aaronson says, perhaps it isn't that surprising that enhancing
polynomial time computation with a time machine results in PSPACE! After all,
we're treating time much like space -- reusable. 

What I'd like to add on to this is the following:

One of the markers of modern complexity theory still being a ridiculously
mysterious field is its inability to prove  (probably true) statements like 
$$PSPACE \subsetneq P$$.

We've shown in this post that for $$P$$ to equal $$PSPACE$$, we need a literal
time machine! Yet the constructions that complexity theorists come up with in the past few
decades haven't been able to show that $$P$$ has less resources than $$PSPACE$$ to separate
these two classes.

I think these ideas and open questions are what make complexity theory so fascinating as
well as being "practical" in the sense that it helps you reason about what **is** a 
computational resource!

### References
>[David Deutsch, Quantum Mechanics of Time Travel](https://en.wikipedia.org/wiki/Quantum_mechanics_of_time_travel)
>
>[Scott Aarronson, Democritus](https://scottaaronson.com/democritus/lec19.html)

