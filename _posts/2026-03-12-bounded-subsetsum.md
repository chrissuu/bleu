---
layout: post
title: bounded subset sum
subtitle: np-complete-like problems
tags: [complexity theory]
type: nr
---
Recall the $$\textsf{PARTITION}$$ decision problem (and variations thereof) which asks: given some set of integers, is there two disjoint subsets of these integers such that their sums are equal? As it turns out, this decision problem is $$\textsf{NP}$$-hard and in $$\textsf{NP}$$, making it an $$\textsf{NP}$$-complete language. In other words, we're unsure if there is a polynomial time decider computing this language (and we think that $$\textsf{P} \neq \textsf{NP}$$, so such a decider probably **doesn't** exist). However, consider the following new language: $$\textsf{BOUNDED-PARTITION}$$, which has the same specifications as before except now the magnitude of our integers are polynomially bounded. In this case, we can show a non-deterministic log-space decider for this new language (left as an exercise), which thus puts this language in $$\textsf{P}$$, since $$\textsf{NL} \subseteq \textsf{P}$$. 

This is quite peculiar: seemingly, both nondeterministic deciders have mostly the same protocol. The only difference is that in $$\textsf{BOUNDED-PARTITION}$$, their respective **inputs** are length/size-bounded, and immediately this puts one solvable in polynomial time but the other in (conjectured) exponential time!

A few observations: $$\textsf{PARTITION}$$ is not the only language where this phenomena arises. For instance, $$\textsf{3SAT}$$ is $$\textsf{NP}$$-complete, but $$\textsf{2SAT}$$ is not (in fact, $$\textsf{2SAT}$$ is $$\textsf{NL}$$-complete). $$\textsf{3COL}$$ of graphs is also hard, but $$\textsf{2COL}$$ reduces to bipartite matching. 