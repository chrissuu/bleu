---
layout: post
title: lazy system
subtitle: lazy, lazy, lazyyy
tags: [math, probability]
---

In Dr. Bob's physics lab, Dr. Bob always seems to go past class time! Instead of fixing his time management, on the days that he has to return his student's tests, he hands them out randomly to save time!!!

What are the amount of students that get their test back? 

Suppose Dr. Bob's class has 3 students: Alice (A), Bob Jr. (B), and Jack (J). 

We can simulate Dr. Bob's test return process pretty easily:

Alice | Bob Jr. | Jack | # that get their own test back
A |  B | J | 3
A | J | B | 1
B | A | J | 1
B | J | A | 0
J | A | B | 0
J | B | A | 1

We are interested in the expected value of the number of students that get their test back, for the case where # students is 3. Let's say that X is the number of students getting their own test back.

$$\textbf{E}[X] = \sum_{x \in \text{range}(X)} x \textbf{Pr}[x] = 3 * \frac{1}{6} + 1 * \frac{3}{6} + 0 * \frac{2}{6} = 1$$

So we can expect that about 1 student will get their test back every time Dr. Bob runs class late. This is not very good! What would happen if the class size was bigger? Say, for arbitrary n? How can we model this problem?

### A counting argument (a naive solution)

Suppose there are n people in the class. The expected value formula still stays the same:

$$\textbf{E}[X] = \sum_{x \in \text{range}(X)} x \textbf{Pr}[X = x]$$

Hence, we want to find some closed form for $$\textbf{Pr}]X = x]$$. With n people, there are $$n!$$ possible ways (permutations) that the tests can be given out, and we're interested in the probability that $$0 \leq k \leq n$$ people get their own test back. i.e, $$\textbf{Pr}[X = k]$$. 

If we imagine permutations as being bijections from some arbitrary (predetermined) ordered set, we can think about how "fixed points" as being the students that get back their own test. i.e, given $$n$$ students and a bijective function $$f: [n] \rightarrow [n]$$, $$f(k) = k$$ would be a fixed point that also encodes the fact that student k got back their own test. 

If we can find how many bijective functions there are that keep $$k$$ points fixed (say $$N$$), we can find the probability that $$k$$ students get their own test back pretty easily: $$\frac{N}{n!}$$

First, there are $$n \choose k$$ ways to pick a subset of size $$k$$ from a set of size $$n$$. After this initial choice of size $$k$$, we are left with $$n-k$$ elements in the domain that haven't been mapped yet. 

For the rest of our elements, we are interested in the number of permutations that don't have any fixed points. This is exactly the derangements problem! [Derangements (wiki)](https://en.wikipedia.org/wiki/Derangement#Counting_derangements)

Without proof, we state that the number of derangements for a $$v$$ element set is, denoted $$!v$$, is:

$$!v = (v-1)* (!(v-1) + !(v-2)), v \geq 2$$

This is a recurrence relation, with $$!0 = 1$$ and $$!1 = 0$$. By the multiplication principle, we are left with $${n \choose k} !(n-k)$$ ways to define a bijective function that keeps $$k$$ points fixed. 

$${n \choose k} !(n-k) = \frac{(n!)(!(n-k))}{k!(n-k)!}$$

Our probability that $$k$$ students get their own test back is hence: 

$$\textbf{Pr}[X = k] = \frac{(n!)(!(n-k))}{k!(n-k)!(n!)} = \frac{!(n-k)}{k!(n-k)!}$$

Hence, our expected value for X:

$$\textbf{E}[X] = \sum_{x \in \text{range}(X)} x \textbf{Pr}[X= x] = \sum_{x \in \text{range}(X)} x \frac{!(n-x)}{x!(n-x)!}$$

Since range$$(X) \subset [0,n]$$, we take $$x$$ to be a natural number: $$0 \leq x \leq n$$

$$\textbf{E}[X] = \sum_{x \in \text{range}(X)}  \frac{!(n-x)x}{x!(n-x)!} = \sum_{x = 0}^{n}  \frac{!(n-x)x}{x!(n-x)!}$$

Below, I attached some code to hypothesize about the closed form expression for the expected value. When I ran it against several integers, I found that it returned 1. So we will hypothesize that $$\textbf{E}[X] = 1$$, for all n. We will show this is true using induction, with 3 being our base case.

$$\textbf{E}[X] = \sum_{x = 0}^{3}  \frac{!(3-x)x}{x!(3-x)!} = \frac{!(3-0)(0)}{(0)!(3-0)!} + \frac{!(3-1)(1)}{(1)!(3-1)!}  + \frac{!(3-2)(2)}{(2)!(3-2)!} + \frac{!(3-3)(3)}{(3)!(3-3)!}$$

With $$!2 = 1$$, we can see that the above simplifies to 1. That is, $$\textbf{E}[X] = 1$$ for n = 3, as desired!

Assuming that 

$$\textbf{E}[X] = \sum_{x = 0}^{n}  \frac{!(n-x)x}{x!(n-x)!} = 1$$

We want to show that 

$$\textbf{E}[X] = \sum_{x = 0}^{n+1}  \frac{!(n+1-x)x}{x!(n+1-x)!} = 1$$

Here, we introduce (once again without proof, but refer to the wiki!) a useful identity:

$$\frac{!n}{n!} = \sum_{i = 0}^{n} \frac{(-1)^i}{i!}$$

We can thus transform our induction hypothesis into the following:

$$\textbf{E}[X] = \sum_{x = 0}^{n}  \frac{!(n-x)x}{x!(n-x)!} = \sum_{x = 0}^{n}  \left(\frac{x}{x!} \sum_{i = 0}^{n-x} \frac{(-1)^i}{i!}\right) = 1 $$

And our inductive step also can be substituted with the above identity to become:

$$\textbf{E}[X] = \sum_{x = 0}^{n+1}  \frac{!(n+1-x)x}{x!(n+1-x)!} = \sum_{x = 0}^{n+1} \left(\frac{x}{x!} \sum_{i = 0}^{n+1-x} \frac{(-1)^i}{i!}\right)$$

$$\Leftrightarrow\sum_{x = 0}^{n+1} \left(\frac{x}{x!} \sum_{i = 0}^{n+1-x} \frac{(-1)^i}{i!}\right) = \left(\sum_{x = 0}^{n} \left(\frac{x}{x!} \sum_{i = 0}^{n+1-x} \frac{(-1)^i}{i!}\right)\right) + \left(\frac{n+1}{(n+1)!} \sum_{i = 0}^{n+1-(n+1)} \frac{(-1)^i}{i!} \right)$$

$$\Leftrightarrow \left(\sum_{x = 0}^{n} \left(\frac{x}{x!} \sum_{i = 0}^{n+1-x} \frac{(-1)^i}{i!}\right)\right) + \left(\frac{n+1}{(n+1)!} \sum_{i = 0}^{n+1-(n+1)} \frac{(-1)^i}{i!} \right) = \left(\sum_{x = 0}^{n} \left(\frac{x}{x!} \sum_{i = 0}^{n+1-x} \frac{(-1)^i}{i!}\right)\right) + \left(\frac{n+1}{(n+1)!} \right)$$

$$\Leftrightarrow \left(\sum_{x = 0}^{n} \left(\frac{x}{x!} \sum_{i = 0}^{n+1-x} \frac{(-1)^i}{i!}\right)\right) + \left(\frac{n+1}{(n+1)!} \right) = \left(\sum_{x = 0}^{n} \left(\frac{x}{x!} \left(\sum_{i = 0}^{n-x} \frac{(-1)^i}{i!} + \frac{(-1)^{n+1-x}}{(n+1-x)!}\right)\right)\right)  + \left(\frac{n+1}{(n+1)!} \right)$$

$$\Leftrightarrow \left(\sum_{x = 0}^{n} \left(\frac{x}{x!} \left(\sum_{i = 0}^{n-x} \frac{(-1)^i}{i!} \right) + \frac{x}{x!} \left(\frac{(-1)^{n+1-x}}{(n+1-x)!}\right)\right)\right)  + \left(\frac{n+1}{(n+1)!} \right) $$

$$\Leftrightarrow \sum_{x = 0}^{n} \left(\frac{x}{x!} \left(\sum_{i = 0}^{n-x} \frac{(-1)^i}{i!} \right)\right) + \sum_{x = 0}^{n}\left(\frac{x}{x!} \left(\frac{(-1)^{n+1-x}}{(n+1-x)!}\right)\right)  + \left(\frac{n+1}{(n+1)!} \right) $$

By the induction hypothesis, the first term is equal to 1, and so we are left with:

$$\Leftrightarrow 1 + \sum_{x = 0}^{n}\left(\frac{x}{x!} \left(\frac{(-1)^{n+1-x}}{(n+1-x)!}\right)\right)  + \left(\frac{n+1}{(n+1)!} \right) $$

$$\Leftrightarrow 1 + \sum_{x = 1}^{n}\left(\frac{1}{(x-1)!} \left(\frac{(-1)^{n+1-x}}{(n+1-x)!}\right)\right)  + \left(\frac{1}{(n)!} \right) $$

$$\Leftrightarrow 1 + \sum_{x = 1}^{n}\left(\frac{(-1)^{n+1-x}}{(x-1)!(n+1-x)!}\right)  + \left(\frac{1}{(n)!} \right) $$

For the sake of conciseness, the proof that term two is the additive inverse of term three is left as an exercise. QED

We have shown that the expected value for all n is one! In other words, when Dr. Bob randomly returns tests to all his n students, only one person will be expected to have their own test!!!! But this solution wasn't very elegant, and in fact, there is a much more easier, intuitive, and concise solution! 

### Using indicators...

We introduce a notion of "indicators"!

Indicators are random variables that have an analogue to characteristic functions for sets!

They are defined as having a range of $${0,1}$$. Then, we can define an event under the notion of this indicator, say, $$I$$. That is, we can define $$I(e)$$ to be $$0$$ if the event didn't happen and $$1$$ if the event did happen.

Then, if there are $$n$$ students, we define $$I_i$$ to be the random variable "the i'th student got their test back".

Hence, we observe that the number of students getting their midterm back, $$X$$, is exactly:

$$X = \sum_{x = 1}^{n} I_x$$

Why? Because recall that $$I_x = 1$$ if student $$x$$ got their own midterm back.

Then, 

$$X = n \Leftrightarrow \forall x \leq n, I_x = 1$$

But why is this useful?

Indicators have a very useful property. Given an indicator $$I$$ for an event $$E$$:

$$\textbf{E}[I] = \textbf{Pr}[E]$$

Proof is left as an exercise (it is quite simple).

This significantly and elegantly simplifies our question, since we can now use linearity of expectation.

$$\textbf{E}[X] = \textbf{E}[\sum_{x = 1}^{n} I_x] = \sum_{x = 1}^{n} \textbf{E}[I_x]$$

And since there are n students, the probability that a student gets their own midterm back is exactly $$\frac{1}{n}$$!

$$\textbf{E}[X] = \sum_{x = 1}^{n} \textbf{E}[I_x] =  \sum_{x = 1}^{n} \textbf{Pr}[I_x]  =\sum_{x = 1}^{n} \frac{1}{n} = 1 $$

QED

### Code

Following is the code used to hypothesize about the expected value for arbitrary n. 

[Code]

[Code]:{{ site.url }}/bleu/downloads/expected.txt

### References

>[Derangements (wiki)](https://en.wikipedia.org/wiki/Derangement#Counting_derangements)
>
>[Linearity of expectation & Indicators](https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_and_Computation_Fundamentals/Mathematics_for_Computer_Science_(Lehman_Leighton_and_Meyer)/04%3A_Probability/18%3A_Random_Variables/18.05%3A__Linearity_of_Expectation)
