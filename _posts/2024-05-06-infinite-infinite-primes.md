---
layout: post
title: infinite, infinite primes
subtitle: a proof of infinite primes using finite automata
tags: [math, cs]
---

### Introduction

When Euclid proved in the *Elements* that there are an infinite number of primes, he opened the flood gates to a very deep field of mathematics: number theory!

Number theory's applications today are broad and powerful, ranging from cryptography that keeps us safe on the Internet, to powerful computational algorithms, to pseudorandom number generation. 

In this post, we explore a very unique proof of infinite primes!

### Euclid's proof of infinite primes

In a way, it seems sort of unintuitive that there would be infinite primes! After all, primes are defined to be the indivisible (other than 1 and itself) factors of other numbers. As numbers grow larger and larger, wouldn't it be more likely that these numbers share factors with smaller numbers? That is, if we say that the set of primes are finite, and call this set P, wouldn't it be more likely that the larger the number, the more likely it is to have factors in P? This phenomenon is sort of reflected in the Prime Number Theorem, but our intuition here is wrong. The set of primes are in fact infinite!

Since it's a short proof, I'll attach Euclid's proof here to build some intuition:

The proof follows by contradiction.

Assume for the sake of contradiction, that the set of primes are finite. Call this set F.

Then, define a product across all elements of F as such:

$$ \text{prod}(F) =  \prod_{p \in F} p $$

This is well defined since F is assumed to be a finite set.

Now, consider $$\text{prod}' = \text{prod}(F) + 1$$

If $$\text{prod}'$$ is prime, then that contradicts the construction of $$F$$, which contains all primes (and $$\text{prod}'$$ is not in $$F$$)

If $$\text{prod}'$$ is not prime, then some prime $$p$$ in $$F$$ should divide $$\text{prod}'$$. However, also by construction of $$F$$, this prime $$p$$ should divide $$\text{prod}(F)$$. Then, trivially, $$p$$ should divide $$\text{prod}' - \text{prod}(F) = 1$$. However, no prime divides 1, a contradiction.

### Infinite primes with finite automata

This is an interesting proof of infinite primes using the language of DFA's. In a similar way to Euclid's proof, it begins with a contradiction. But first, we build up some relevant definitions and ideas.

#### Regular Language

A language is said to be regular if there is a DFA solving (or computing) it.

#### Non-regular Language

A language is said to be non-regular if there does not exist a DFA solving (or computing) it. Usually, such proof involves the pigeonhole principle (PHP).

#### Character counting function

Given a word $$w$$, we define the following function:

$$\#_c(w) = \sum_{c \in w} 1$$

In other words, a function computing the number of occurences that character c makes in the word w. 

#### Prime set

$$PRIMES := \{n \in \mathbb{N} | n \text{ is prime }\}$$

#### DFA Union Closure

DFA's are closed under union. To see this, consider two regular languages $$L, K$$, and let $$M_L$$ and $$M_K$$ be the DFA's computing them. 

We define a new DFA, $$M'$$ that solves their union. That is, the language of $$M'$$ = $$L \cup K$$ is regular.

$$Q' = Q_L \times Q_K$$

$$\Sigma' = \Sigma_L = \Sigma_K$$

$$\delta'(q' = (q_L, q_K), \sigma) = (\delta_L(q_L, \sigma), \delta_K(q_K, \sigma))$$

$$q_0' = (q_{0L}, q_{0K})$$

$$F' = \{ (q_i, q_j) | q_i \in F_L \lor q_j \in F_K \}$$


Verify for yourself that the above language computes the union of $$L$$ and $$K$$.

We can generalize this to $$N$$ regular languages.

Let $$L_1, L_2, L_3, ... , L_N$$ be regular languages.

Then, $$\bigcup\limits_{i = 1}^{N} L_i$$ is also regular. (For $$N \in \mathbb{N}, N >= 2$$)

The proof is simple and follows from induction.

Base case: $$N = 2$$

True from the above reasoning.

IH: Suppose that $$\bigcup\limits_{i = 1}^{N} L_i$$ is regular. Want to show that $$\bigcup\limits_{i = 1}^{N+1} L_i$$ is also regular.

We know that the regular languages are closed under the union operator. $$V = \bigcup\limits_{i = 1}^{N} L_i$$ is regular by assumption and $$L_{N+1}$$ is regular by definition. Hence, $$V \cup L_{N+1}$$ is also regular. 

#### Proof

With some of the definitions out of the way, we begin the proof. The main idea is to construct a family of languages that encode prime numbers, assume that the union of this family is regular, and then arrive at the contradiction that the language is not regular.

Without loss of generality, we will restrict our language to $$\Sigma = \{0, 1\}$$. (Remember that all encodable languages can be re-encoded to the binary language, so this is not a problem)

Now, consider the following language:

$$L_n = \{w \text{ | }  n \text{ divides } \#_1(w) - \#_0(w) \} $$

Verify for yourself that this language is in fact regular.

Consider now, the following new languages:

$$L = \bigcup\limits_{ p \in PRIMES } L_p $$

$$K = \{ w | \#_1(w) - \#_0(w) \notin \{-1,1\}\}$$

We will show that the above languages are equivalent by double containment:

For the forward direction: ($$L \subseteq K$$)

Assume $$w \in L$$, we want to show that $$w \ in K$$. Since $$w \in L$$, we know that $$w$$ is in the union of $$L_p$$, $$\forall p \in PRIMES$$. Hence, we can find some prime $$p_i$$ such that $$w \in L_{p_i}$$. By the definition of $$L_{p_i}$$, $$p_i$$ divides $$ \#_1(w) - \#_0(w) $$. However, we know that no prime divides $$1$$ or $$-1$$. Hence, $$ \#_1(w) - \#_0(w) \neq 1, \neq -1$$. By definition, of $$K$$, $$w \in K$$. 

For the backward direction: ($$K \subseteq L$$)

Assume $$k \in K$$, we want to show that $$k \in L$$. Since $$k \in K$$, we know that $$ \#_1(k) - \#_0(k) \neq 1, \neq -1 $$. Thus, $$  \#_1(k) - \#_0(k) > 1,  \#_1(k) - \#_0(k) < -1, \#_1(k) - \#_0(k) = 0$$. These intervals allow the differences to have prime factors. That is, there exists some prime $$p$$ that divides $$\#_1(k) - \#_0(k)$$, which means that $$k \in L_p$$, so $$k \in \bigcup\limits_{ p \in PRIMES } L_p = L$$, as required. 

Next, we show that the language $$K$$ is NOT regular, by pigeonhole principle:

Assume for the sake of contradiction that $$K$$ can be solved by a DFA with $$\|Q\| = n$$ states. We define the fooling pigeon set of size $$n+1$$ as follows:

$$ fps = \{ 1^{3k} | 1 \leq k \leq n+1 \} $$

By the pigeonhole principle, there are $$n+1 > n$$ states, so two words, (WLOG, we say) $$w_i = 1^{3i}$$ and $$w_j = 1^{3j}$$ (such that $$w_i \neq w_j$$) end up in the same state and will have the same computation path for future computations.

That is to say, appending any word $$k$$ to $$w_i$$ and $$w_j$$ will also follow the same computation path.

WLOG, suppose that $$i < j$$.  Append $$k = 0^{3i+1}$$ to both words. By the reasoning above, the resulting words, $$w_ik$$ and $$w_jk$$, must end up in the same state. Since $$\#_0(w_i) - \#_1(w_i) = 3i - 3i - 1= -1$$, $$w_i$$ is not in $$K$$, so the DFA **rejects** $$w_i$$. However, $$\#_0(w_j) - \#_1(w_j) = 3j - 3i -1 = 3(i + c) - 3i -1 = 3i + 3c - 3i - 1 = 3c - 1$$. With $$c>=1$$, we can bound $$3c - 1 >= 2$$, so $$w_j \in K$$, so the DFA **accepts** $$w_j$$. But both $$w_jk$$ and $$w_ik$$ should end up in the same state! This is the desired contradiction. Hence, $$K$$ is not regular. It follows from $$K = L$$ that $$L$$ is also not regular. 

Finally, assume for the sake of contradiction that there are a finitary amount of prime numbers. Recall from the above definitions that if we have a finite sequence of regular languages, their union is also regular! 

Hence,

$$\bigcup\limits_{p \in PRIMES} L_p$$

is regular! However, $$\bigcup\limits_{p \in PRIMES} L_p = L = K$$, and we have shown that $$K = L$$ is not regular! Thus, a contradiction! There must be an infinite number of primes.

### Overview

Number theory is a rich field and it's always cool to see new proofs of established theorems come up. New proofs provide useful insights or techniques to prove other (possibly unproven) ideas! The theorem proven here shows an unexpected connection between automata theory and number theory and provides insight in the powerful ability of automatas to encode information.

### References

>[Euclid's Theorem Wiki](https://en.wikipedia.org/wiki/Euclid%27s_theorem)
>
>CMU CS 15-251
>
>[arxiv paper](https://doi.org/10.48550/arXiv.2005.10372)
