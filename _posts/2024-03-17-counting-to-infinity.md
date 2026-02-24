---
layout: post
title: a real and natural dilemma
subtitle: a nonrigorous introduction to cardinality
tags: [math]
type: nr, f
---

One of the first things we ever learn how to do is count! 

Indirectly, we are learning how to use the natural numbers: the numbers that are positive (and usually includes 0).

Mathematicians like to denote the natural numbers with a curly N: $$\mathbb{N}$$.

The natural numbers are also sometimes called "counting numbers" since they have a direct correlation to how we count things in real life, otherwise known as "enumeration". For example, if we were asked to count the number of skittles in a bag of Skittles, we would individually count them, one by one, incrementing at each skittle we come across!

Hence, we also have an implicit notion of a "next number". That is, given a number like 5, you can give me the next number, which is 6! And you can always do this for all numbers n.

Likewise, we can then define a "previous" number. For example, given 3, I would give you the "previous" number, which is 2. But what about 0? What is the previous number to 0? 

This poses an interesting question since we can't have "negative" of anything in a physical sense, like "negative skittles", but it's pretty useful to define!

This is called the set of integers, denoted $$\mathbb{Z}$$!

### A natural dilemma

In highschool or middle school, sometimes even early as elementary school, math classes start to introduce a notion of "real numbers", numbers that fill in the gaps between our natural numbers, like $$\pi$$, $$e$$, $$\sqrt{2}$$, etc. 

But there's something that differentiates our natural numbers with real numbers. If I asked you to give me the first natural number, that would be easy: 0 or 1 depending on the convention you use. But what if I asked you to give me the first non-natural real number? Is it 0.1? Why not 0.01? Or 0.000000000000000001? Is there such thing as a "first number" for real numbers?

### Counting sets

The question I posed above is connected to a notion of "countability", that is, what can be connected with our fingers and what cannot, like the skittles example above.

Since we're comfortable with natural numbers, we will say that if we can count things using the natural numbers as a benchmark, then that thing we're counting is also countable!

This makes pretty good sense so far, since, in a sense, whenever we count, we always refer back to the natural numbers! In fact we'll make our definition for countability even more powerful: suppose we have some box with numbers in it, say 0 through some number k. If in some other box, we can put labels on all the items inside it using our first box with numbers, then the two boxes have the same number of elements!

#### Example 1

Let's say box 1 has {1,2,3} and box 2 has {red, blue, green}. Since we can give red the label "1", blue the label "2", and green the label "3", the two boxes have the same size!

But if box 1 has {1,2,3} and box 2 has {red, blue, green, yellow}, then we can't give yellow a label! So the two boxes must not have the same size.

Interestingly, this heuristic also works for INFINTE SETS!!!!

For example, let's say we wanted to count how many square numbers there. That is, numbers of the form $$k^2$$, for some k that is a natural number.

Well, we can give the label $$k$$ to each number $$k^2$$!

Like so:

1 | 2 | 3 | 4 | ... | $$k$$
1 | 4 | 9 | 16 | ... |$$k^2$$

Using our heuristic above, we can say that the number of natural numbers is the same as the number of square numbers!!! That is, there is just as many natural numbers as there are square numbers.

But this is kind of counter intuitive, isn't it? The square numbers are a subset of the natural numbers! (That is, every square number is also a natural number) So how is it possible that they are the same size????

The reason is *because* we are able to count the square numbers in that manner, that they are equal in size. (Stuff in infinity tends to be counterintuitive)

#### Example 2

In the same way, we can also argue that the number of natural numbers is the same as the number of integers! Let box 1 be the box with natural numbers and let box 2 be the box with integers.

1 | 2 | 3 | 4 | 5 | 6 | ... | k | k + 1
-1 | 1 | -2 | 2 | -3 | 3 | ... | -k/2 | k/2

So in a sense, our heuristic for something being "countable" is if we can number them with the natural numbers, such that all the numbers in our second box eventually appear at least once! 

<strong>This matches our intuition, an intuition we've had since we were kids: count stuff with your fingers, and if there are more than 10, then we can't count them on our fingers! </strong>

<strong>Same thing with natural numbers: count stuff with natural numbers, and if there is stuff still left, then we can't count them with natural numbers!</strong>

In the previous examples, we never ran out of natural numbers, so we can safely say that both integers and square numbers are countable! (And they must be the same size as the natural numbers, which also implies that the integers and square numbers have the same size!)

### A real dilemma...

In the previous examples, we saw that being able to count in another box with the natural numbers kind of meant that we were able to count the stuff in that second box. We also had no issue doing that. 

So does that mean all sets are countable? Our intuition betrayed us once, so is it possible that all things are really countable?

Well this post wouldn't be that interesting if that were the case...

>**Theorem 1**
>
>The real numbers are uncountable

Here is when intuition meets mathematical reality: the real numbers are in fact, uncountable! That is, we can TRY to list all real numbers with natural numbers, but there will always be more real numbers!

This matches our intuition:

You name a number, say 10, and I'll name a number, say 11.

Next, we'll take turns naming numbers that are between each other's last called number. So for example, you would name 10.5, and then I would give 10.75, and you might give 10.6, and so forth... till infinity.

But how can we prove something like this??

#### Enter, Georg Cantor

Georg Cantor was a mathematician in the late 1800s that formalized our notions of mathematical infinity today. When he first introduced his work, it was met with fierce objection. The ideas were considered "utter nonsense" by many of his peers and many claim that the psychological load of the hostility he faced caused him to develop bipolar disorder later in his life. 

Nonetheless, his ideas serve as a foundation for infinity today and is one of the most important ideas to have been conceived. 

#### Diagonalization

To show that there are more real numbers than natural numbers, we will try to count them, and then arrive at some contradiction.

We will start by assuming that the real numbers are countable with the natural numbers. However, if we arrive at some contradiction, it must mean that our initial assumption was false, that is, the real numbers CANNOT be counted with the natural numbers, and then we are done!

Here, think we introduce some notation:

$$0.b_1b_2b_3b_4b_5...$$ 

Represents a decimal string. For example, 0.12345 is the case where $$b_1 = 1, b_2 = 2, b_3 = 3, b_4 = 4, b_5 = 5$$.

Next, consider some arbitrary decimal strings, and we will write them out in a table. We will also use infinite degrees of precision, that is, these decimals are infinite! (This is always the case since we can always keep adding 0's to the end of a decimal without changing a value)

Number 1 | 0. | $$b_1$$ | $$b_2$$ | $$b_3$$ | $$b_4$$ | ... |
Number 2 | 0. | $$c_1$$ | $$c_2$$ | $$c_3$$ | $$c_4$$ | ... |
Number 3 | 0. | $$d_1$$ | $$d_2$$ | $$d_3$$ | $$d_4$$ | ... |
Number 4 | 0. | $$e_1$$ | $$e_2$$ | $$e_3$$ | $$e_4$$ | ... |
Number 5 | 0. | $$f_1$$ | $$f_2$$ | $$f_3$$ | $$f_4$$ | ... |
... | ... | ... | ... | ... | ... | ... |
Number k | 0. | $$k_1$$ | $$k_2$$ | $$k_3$$ | $$k_4$$ | ... |

Cantor then noticed that he can "create" a real number not in the enumeration above! 

Cantor's new number = 

$$0.B_1C_2D_3E_4F_5K_k....$$

Where $$B_1 = b_1 + 1$$, $$C_2 = c_2 + 1$$,  $$D_3 = d_3 + 1$$...

Cantor's observation was that if the real numbers really were countable, then all real numbers should be enumerable. So, enumerate all the numbers and put them in a table! But cleverly, we can construct some new number by "disagreeing" at a single digit in each number in the table (of which there are infinite rows). Our new number should appear somewhere in the table, but that isn't possible! 

Why can't our new number appear somewhere in the table? Take a look: our new number can't be equal to Number 1 since the **first** decimal digit is different (in our new number, the first decimal digit is $$B_1$$ which has the value $$b_1 + 1$$). Our new number can't be equal to Number 2 since the **second** decimal digit is different; Number 3 can't be equal since the third digit is different... and so forth. In fact, for all the numbers in our table, our new number disagrees with each number!!!! In other words, our new number CAN NEVER be the same as a number in the table. 

But this is a contradiction!!! We said we can count the real numbers with the natural numbers, so that means that any number we create should appear in the table eventually, but it doesn't!!!

Hence, the real numbers are uncountable. 

This technique was created by Cantor to prove that infinite sets actually have different sizes! The technique is called diagonalization because the new element is created by disagreeing at the diagonal elements on the table!

### Overview

With infinity, our intuition often betrays us, but not always! The real numbers feel uncountable because they really are! And Georg Cantor formalized this notion. His work allowed for us to reason about infinity and sets of different sizes! The applications are wide ranging, with a notable example being the Halting problem in computer science!

As an exercise, try to see if you can come up with a way to count the rational numbers.

### References

>[Infinite Hotel Paradox (veritasium video)](https://youtu.be/OxGsU8oIWjY?feature=shared)
>
>[Diagonalization (wiki)](https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument)
>
>[Cantor (wiki)](https://en.wikipedia.org/wiki/Georg_Cantor)

