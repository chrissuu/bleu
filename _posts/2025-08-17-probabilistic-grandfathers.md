---
layout: post
title: probabilistic grandfather
subtitle: time travel as a computational resource? (pt 1)
tags: [math, complexity theory]
type: nr
---
### Introduction
A well known time travel paradox goes like this:

Suppose you have a time machine which can take you back in time. 

For some reason (it's unclear why you might want to do this), you decide to kill your grandfather when he was a little boy.

Indeed, by killing your grandfather when he was a little boy, he never meets your grandmother, and therefore you are never born.

But wait -- since you're never born, how did you kill your grandfather in the first place?

This is the Grandfather Paradox.

### Probabilistically Resolving the Grandfather Paradox
One way to resolve the Grandfather's Paradox is by ensuring that the conditions of the new universe you create is equivalent to the one that existed before.

Consider this observation:

In the classical Grandfather Paradox, you go back in time and kill your grandfather, which results in you never being born, and hence unable to kill your grandfather, implying that you still exist in the universe.

**Observe that your existence is the source of the paradox.**

We can resolve this paradox by considering our existence to be probabilistic. That is, we claim that we exist with probability 1/2.

Some arbitrary (meta-)universe tosses a fair coin. If heads lands up, you are born, at which point, you take your time machine and proceed to blip yourself out of existence. Yet, you're born with probability 1/2, thus the probability that you are able to blip yourself out of existence is also 1/2, which finally implies that the probability you are born is once again 1/2.

At this point, you should note that this circular argument would've given us exactly the Grandfather paradox in the deterministic case, but injecting randomness into our existence has resolved it!


### Biased Nonexistence
Suppose instead that this meta-universe flips a biased coin that has probability $$\rho = 1-\epsilon, \epsilon \gt 0$$ of landing heads. Consider that you're now born with probability $$\rho$$, and hence the probability that you blip yourself out of existence is $$\rho$$, but this implies that the probability that you are born is $$1 - \rho$$! This is indeed a contradiction unless $$\epsilon = 0.5$$.

#### Philosophical Ramifications
In a universe which has time travel into the past within the same space-time curvature that you exist in, the mathematical way to resolve paradoxes which arise is to suppose that it must be the case that you will exist with probability 1/2. The biased nonexistence lemma suggests that your existence must be uniformly random. If it were to tip in one way or the other, you once again contradict your existence on grounds of a Probabilistic Grandfather Paradox.

Of course, it's unclear what is meant by "existing with probability 1/2". It's also unclear what is the timeframe in which you exist with this probability. For instance, up until you made the decision to use the time machine, did you really have probability 1 of existing? Did you only begin to have probability 1/2 of existing AFTER you thought of using the time machine? These natural questions arise, but because the solution is at the very least mathematically sound, an answer likely appeals more to philosophical ramifications.

Maybe one way to resolve it is to think of it as some quantum state that is superpositioned conditioned on the random event of your birth, but I'm not terribly confident that I have enough knowledge of quantum mechanics to make that argument sound :)

### Conclusion
This was a brief post talking about fixed distributions in markov chains, although it may not have seemed like it. The next post will cover some of the main ideas in Scott Aaronson's blog post about a computational model which uses time travel to gain more computational power over the complexity class P. 

In fact, it turns out that with access to this time machine, we can solve NP-complete problems in polynomial time and even PSPACE problems in polynomial time! For those unfamiliar, PSPACE is the complexity class of problems solvable in polynomial space -- this is a class which is believed to be strictly stronger than NP. Note that $$NP \subseteq PSPACE$$ since NP has a polynomially-bounded length in proof size, which means that we can simply enumerate all polynomial length proofs and use the verifier TM to compute the language. The key insight is that across each membership test, you can reuse space (and hence $$NP \subseteq PSPACE$$ but widely believed that $$NP \subsetneq PSPACE$$)!

### References
>[David Deutsch, Quantum Mechanics of Time Travel](https://en.wikipedia.org/wiki/Quantum_mechanics_of_time_travel)
>
>[Scott Aarronson, Democritus](https://scottaaronson.com/democritus/lec19.html)

<div class="author-box">Chris Su - Carnegie Mellon University - AI &amp; Computer Science</div>
