---
layout: post
title: creative collapse
subtitle: a rigorous introduction to the P vs. NP problem
tags: [cs, philosophy]
---
### Introduction

Read the previous post for an introduction! Here, we dive right into a rigorous statement of the problem and one of the most amazing implications of $$P=NP$$!

### Formal statement of P vs. NP

The P vs. NP question asks the following:

Does the set of polynomial time decidable languages equal the set of polynomial time verifiable languages?

Clearly, the set of polynomial time decidable languages is a subset of polynomial time verifiable languages (NP). Hence, the question simplifies to whether all languages that can be verified in polynomial time also has an algorithm that decides it in polynomial time.

For the rest of this post, I will assume that you have some familiarity with the following:

1. Verifiers
2. Deciders
3. P vs. NP

### The mechanization of creativity

Given a decider $$M_L$$ for a language $$L$$, we know that it will always halt and output "ACCEPT" or "REJECT". However, most of the time, we aren't just interested whether a word is in the language or not! We want to know exactly WHY it's in the language, that is, we want a proof U that the word is in the language!

Given some verifier $$V_L(<w, u>)$$, where $$V_L$$ is a verifier to the language $$L$$, we want to figure out what proof $$u$$ shows that $$w \in L$$! But how can we output this $$u$$? Is this a limitation to the P vs. NP problem?

In fact, it is not!

Assuming $$P = NP$$, we can find a way to output this proof $$u$$!

### Creative collapse
Assume $$P = NP$$. Given some language $$L \in NP$$, we define the following language:

$$L_{V} = \{<x, w> \in \Sigma^{*} \text{ | } \exists u \in \Sigma^{*}, |w \cdot u| \leq x^k \text{ s.t. } V(<x, w \cdot u>) \text{ ACCEPTS }\}$$

It is easy to see that $$L_V \in NP$$:

>def $$\text{Verifier}_{L_{V}}(<(x,w), u>)$$:
>
>&emsp;return $$V(<x, w \cdot u>)$$

Small proof: If $$w \in L_{V}$$, then by definition, there exists some $$u$$ that lets $$V(<x, w \cdot u>)$$ accept. If $$w \notin L_{V}$$, then, by definition, no $$u$$ exists such that $$V(<x, w \cdot u>)$$ accepts.

Also, recall we assume that $$P=NP$$. Since $$L_{V} \in NP$$ and $$P = NP$$, then $$L_{V} \in P$$, so there must be some polynomial time decider for that language. We will call this decider $$M$$. Now, we have all the tools to output a proof $$u$$ of membership in a language $$L$$! 

### A human algorithm and a sprinkle of divine inspiration
Without loss of generality, we will restrict our language to a binary set: $$\Sigma = \{0,1\}$$. 

>(1)def $$\text{give_proof}_{L}(<w>)$$:
>
>(2)&emsp;&emsp;if $$M(<w, \epsilon>)$$ rejects: reject
>
>(3)&emsp;&emsp;proof_u = ""
>
>(4)&emsp;&emsp;while $$V(w, \text{proof_u})$$ rejects:
>
>(5)&emsp;&emsp;&emsp;&emsp;if $$M(<w, \text{proof_u} \cdot 1>)$$ accepts:
>
>(6)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;proof_u = proof_u + "1"
>
>(7)&emsp;&emsp;&emsp;&emsp;else:
>
>(8)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;proof_u = proof_u + "0"
>
>(9)&emsp;&emsp;return proof_u

We will go through a line by line explanation of the above algorithm. 

Recall the point of our algorithm is: given a language $$L \in NP$$ and a word $$w$$ that we know to be in $$L$$, find some proof $$u$$ s.t. $$V(w, u)$$ accepts.

Notice that when we pass in $$(<x, \epsilon>)$$ to $$M$$ in line 2, $$M(<x, \epsilon>)$$ accepts $$\Leftrightarrow$$ $$\exists$$ proof_u s.t. $$V(x, \text{proof_u})$$ accepts. We need this initial check, since if no proof exists for $$w$$, then our algorithm won't be a decider for the language. (i.e, never halts)

Then, on line 4, we can safely loop. The key insight here is that if a proof exists, we can slowly build up our proof using our decider $$M$$. $$M$$ checks if there is some string that can be appended to our current proof to let $$V$$ accept. Once $$V(w, \text{proof_u})$$ accepts, we know that we've found our proof for $$w$$'s membership in $$L$$!

### Overview

The question of P vs. NP doesn't just ask about deciders. It is much more general, intricate, and perhaps beautiful than a binary True/False result. P vs. NP asks whether creativity can be mechanized; whether creativity is part of the problem solving process; and in a more philosophical sense, whether the human creativity and intellect is inherently less powerful than the very logic and proof system we created using it!

### References

>[Knowledge, Creativity, and P vs NP](https://www.math.ias.edu/~avi/PUBLICATIONS/MYPAPERS/AW09/AW09.pdf)
