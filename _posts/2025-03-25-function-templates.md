---
layout: post
title: currying and function templates
subtitle: a gentle introduction to functional programming
tags: [math, programming]
type: nr
---
### Introduction
This is a shorter post, with hopes that by the end of it, you'll begin to see some of the very natural elegance that arises in a functional programming paradigm.

A main idea of "function"-al programming is that everything is a function! (See [Thomas Garrity on Functions](https://www.youtube.com/watch?v=PAZTIAfaNr8&ab_channel=Mujtabawrite%27s)) Under this notion, functional programming paradigms allow the programmer to work with functions as first class objects: in other words, functions can take in other functions as arguments, return functions and manipulate functions$${}^{*}$$. 

### Currying
Jumping straight in, suppose we have the following function which adds two numbers:

>(1) def $$\textbf{add}(a, b)$$:
>
>(2)&emsp;&emsp; **return** a + b;

The concept of currying applies when we have functions that take in more than one argument. We say that a function is "curried" if the arguments to it are passed to the body of the code through a sequence of univariate functions. In the above example, we say that **add** can be curried as such:

>(1) def $$\textbf{add_curried}(a)$$:
>
>(2)&emsp;&emsp; **return** (**add'** (b) = **return** a + b);

Note here that **add_curried** now takes in a *single input*, $$a$$, and returns a new function **add'** which takes in an input, $$b$$, and adds it to $$a$$ in the body of **add'**. Also note that the overall computation that occurs hasn't necessarily changed. 

**add**(1, 2) = 3 and **add_curried**(1)(2) = 3. Note that the parentheses in the latter are intentionally done so that way, since **add_curried** only takes in one input and can't take in a tuple (1, 2).

As another example:

>(1) def $$\textbf{add3}(a, b, c)$$:
>
>(2)&emsp;&emsp; **return** a + b + c;

Can be curried to become:

>(1) def $$\textbf{add_curried3}(a)$$:
>
>(2)&emsp;&emsp; **return** (**add'**(b) = **return** (**add''**(c) = **return** a + b + c));

In this example, we created a curried version of **add3**, **add_curried3**, which takes in one input, $$a$$, returning a function, **add'** which takes in one input, $$b$$, returning a function, **add''** which takes in one input, $$c$$, and finally does the required computation: $$a + b + c$$. 

Both functions, upon given similar inputs, would do the same thing, with the only difference being that inputs have to be passed in one at a time vs. as a tuple. 

A very natural question might arise: **so what's the point**? If these two functions do the same thing, currying is effectively useless! 

### Folding
To answer the previous question, we will look at a slightly more complex function. Often times, when working with lists, it becomes very natural to want to do some sort of "accumulation" across its elements. 

For example, consider the following functions **sum_list**, **prod_list**:

<hr style="height: 2px; background-color: black; border: none;">

>(1) def **sum_list**(L : integer list):
>
>(2)&emsp;&emsp; sum = 0
>
>(3)&emsp;&emsp; for x in L:
>
>(4)&emsp;&emsp;&emsp;&emsp; sum += x
>
>(5)&emsp;&emsp; return sum

<hr style="height: 2px; background-color: black; border: none;">

>(1) def **prod_list**(L : integer list):
>
>(2)&emsp;&emsp; prod = 0
>
>(3)&emsp;&emsp; for x in L:
>
>(4)&emsp;&emsp;&emsp;&emsp; prod *= x
>
>(5)&emsp;&emsp; return prod

<hr style="height: 2px; background-color: black; border: none;">

Both of these functions have a sense of "accumulation" over the elements of the list. The first one collects the sum of all the elements in the list while the second collects the product of all the elements in the list. 

In all paradigms of programming, the idea of repeated code suggests that some refactoring could be done. Here, we have a repeated notion of accumulation. We can imagine that some more complex ideas of "accumulation" over a list might arise compared to simple ones such as **sum_list** or **prod_list**. We may also imagine that these ideas of "accumulation" can exist for lists of other types. 

Hence, we introduce the following function, "fold", which accumulates the elements of the list using a **custom "combine" function**, $$f$$, a **base accumulator** or "identity", $$z$$, and the **list we are folding** over, L. 

>(1) def **fold** (f) (z) (L): # syntax for curried arguments
>
>(2)&emsp;&emsp; if L == []: return z # return what you have accumulated
>
>(3)&emsp;&emsp; if L == [x1, x2, ..., xn]: return **foldl** (f) (f (x1, z)) ([x2, ..., xn])

First, note that this function is recursive because of the **foldl** call on line (3). Line (2) says that when you have no more elements left in your original list, return what you have accumulated so far (and corresponds to the base case). Line (3) says that when you still have more elements left, you should combine the elements at the front of the list, x1, with your accumulator, $$z$$, using $$f$$, and make it the new accumulator in the recursive call. 

Now, using **fold**, we can redefine the functions **sum_list** and **prod_list** with a single line of code:

<hr style="height: 2px; background-color: black; border: none;">

>(1) def **sum_list**(L : integer list):
>
>(2)&emsp;&emsp; return **fold** (+) (0) (L)

<hr style="height: 2px; background-color: black; border: none;">

>(1) def **prod_list**(L : integer list):
>
>(2)&emsp;&emsp; return **fold** (*) (1) (L)

<hr style="height: 2px; background-color: black; border: none;">

Verify for yourself and your intuition that these function definitions are in fact the same as the ones above!

### The Power of Currying
Recall the question / concern posed earlier:
>"A very natural question might arise: **so what's the point**? If these two functions do the same thing, currying is effectively useless!"

Consider **fold** (+), which, because the arguments were curried, returns a function. Specifically, inputs to this function will be the initial accumulator followed by the list L. Earlier, in **sum_list**, we passed in the accumulator 0. What if we passed in something else? Such as 1? 2? $$k$$?[^1] Well now we have functions that will sum the list L, and then add $$k$$ to the result!

In other words, **fold** (+) is a **function family** of the "sum list" function, simply because the arguments were curried! In the same way, **fold** (*) is a function family of the "prod list" function.

With no extra effort on our end (other than changing the syntax to become curried arguments) we've managed to make reusable and modular code.

### Conclusion
When you think of code, you should think about function specifications that might benefit from the natural expressiveness granted by currying. The **fold** function above was one such exmaple, where, depending on the inputs to **fold**, we were able to construct different function families under the main concept of accumulation. 

Given some multivariate function, $$f$$, the idea of currying allows us to naturally modularize it to several different functions, $$h_1, h_2, ... h_n$$ which, when applied in a sequence: $$h_n(h_{n-1}(...h_1(x)))$$, returns the same function $$f$$. 

Yet, this idea is deeper than it seems: since we've essentially serialized the execution of $$f$$, stopping the execution at some $$i$$, $$h_n(h_{n-1}(...h_i(x)))$$, creates function families that have a similar concept to the original function $$f$$, but more "general". This notion allows for us to create clever function templates and instantly increase the expressiveness of a programming language without much added syntactical complexity.

[^1]: **fold** (+) 1, **fold** (+) 2, **fold** (+) k, respectively