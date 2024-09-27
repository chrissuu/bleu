---
layout: post
title: gale-shapley is perfect
subtitle: the stable marriage problem (pt2)
tags: [cs, graph theory]
type: r
---

### Introduction
This is the second of three posts that will talk about matchings! This part will be prove correctness for the three main properties of Gale-Shapley. Feel free to skip, but it will help with the intuition later on. The proofs will mostly be high level overviews. Just rigorous enough to be convincing, but not formally typed out.

For convenience, I copied the GS algorithm from the previous post here:

#### Code

>(1)def $$\text{gale_shapley}(A, B)$$:
>
>(2)&emsp;&emsp;while there exists $$\textbf{guy}_i$$ in $$A$$ that is not matched:
>
>(3)&emsp;&emsp;&emsp;&emsp;let $$\textbf{guy}_i$$ propose to the first $$\textbf{girl}_j$$ in $$B$$ that $$\textbf{guy}_i$$ has not yet proposed to
>
>(4)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if $$\textbf{girl}_j$$ is not yet matched:
>
>(5)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;match $$(\textbf{guy}_i, \textbf{girl}_j)$$
>
>(6)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;else:
>
>(7)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;that means $$m = (\textbf{guy}_i', \textbf{girl}_j)$$ must be matched / is a pair
>
>(8)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;if $$\textbf{girl}_j$$ prefers $$\textbf{guy}_i$$ over $$\textbf{guy}_i'$$:
>
>(9)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;### ($$\textbf{guy}_i$$ is higher on her pref list than $$\textbf{guy}_i'$$)
>
>(10)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;match $$(\textbf{girl}_j, \textbf{guy}_i)$$
>
>(11)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;unmatch $$\textbf{guy}_i'$$ (i.e, he now has no partner)
>
>(12)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;else:
>
>(13)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;keep $$(\textbf{girl}_j, \textbf{guy}_i')$$ matched
>
>(14)&emsp;&emsp;return all matches

### Main properties

Recall from the previous post, the Gale-Shapley algorithm, as well as the following 3 important properties that it guarantees upon completion:

1) All members are matched

2) All matchings are stable

3) The algorithm is polynomial time

#### Theorem 1
>**All members are matched**

All girls will eventually be proposed to, and they will accept the proposal if they are not matched. Notice that all girls that are matched will never become unmatched **(Code lines 10, 13)**. Hence, all girls must be matched at the end of the process. However, we defined the stable matching problem to have parties of equal cardinality. Since there must be an equal number of girls and guys, all guys must also be matched. Hence, all members are matched.

#### Theorem 2
>**All matchings are stable**

Assume for the sake of contradiction that there is a pair $$(A, X)$$ that is unstable at the end of the Gale-Shapley algorithm. Let $$(A, B), (Y, X)$$ be the current matchings. We have two cases to consider. 

(1) $$A$$ proposed to $$X$$ when $$X$$ was already matched and was rejected, or (2) $$A$$ proposed to $$X$$, was matched, but $$Y$$ later matched with $$X$$. In the first case, if $$A$$ proposed to matched $$X$$ and was rejected, $$X$$ must prefer their current match $$Y$$ over $$A$$. Since one sided preferences aren't unstable, this is not an unstable matching. In the second case, if $$A$$ proposed to $$X$$, was matched, but $$Y$$ later matched with $$X$$, this means that $$X$$ preferred $$Y$$ over $$A$$. Hence, this is also not unstable. 

All matchings must therefore be stable.

#### Theorem 3
>**The algorithm runs in polynomial time**

This is easy to see. Namely, suppose the set sizes are $$n \in \mathbb{N}$$. Then, since the preference lists are only of size $$n$$, and there are $$n$$ members, we will only loop through $$n^2$$ times. Hence, the algorithm runsin $$O(n^2)$$. 

### References

>[Stable Matchings Wiki](https://en.wikipedia.org/wiki/Stable_marriage_problem)
>
>[Gale-Shapley Algorithm Wiki](https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm)

