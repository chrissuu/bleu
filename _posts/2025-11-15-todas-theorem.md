---
layout: post
title: toda's theorem
subtitle: PH is a subset of P^#SAT
tags: [complexity theory]
type: r
---
Today, I read Toda's 1989 paper. Titled "PP is as hard as the polynomial-time hierarchy", Toda proved that $$PH \subseteq P^{\#SAT}$$. This is quite the strange theorem since we know that $$P^{SAT} = {\Delta}_{2}^{P}$$, which is contained within $$PH$$ at the second level. $$\#SAT$$ and $$SAT$$ are closely related, so why does one give so much more computational power than the other? Maybe one insight is that instances of $$\#SAT$$ could have *exponentially many* satisfying models (to which the $$\#SAT$$ oracle can know right away). Hence, a program which takes advantage of being able to encode some exponential amount of computation (since model enumeration would be exponential in input length) might just be powerful enough to compute languages more powerful than those at arbitrary levels of the polynomial hierarcy (which can only support a constant number of alternations). This also creates an interesting point of view for computational resources: if something encodes "exponential" of some resource, then there's probably a hacky way to use its oracle to do some crazy things, like making P with a $$\#SAT$$ oracle as hard as $$PH$$!

### References
>[Toda's 1989 Paper](https://dl.acm.org/doi/10.1137/0220053)
