---
layout: post
title: revisiting bin. search
subtitle: reduction to partitioned boolean array search
tags: [cs]
type: nr
---
One of the first algorithms that all CS majors might learn is the binary search algorithm, which 
lets you search some sorted sequence with only a logarithmic number of queries. However, binary
search can be made a little more general than just equality checking for an item. In particular,
it can be used to find the maximal / minimal element satisfying some condition, yet the idea of
sorted-ness (that is, you can have sequences of integers, strings, or basically anything that has
a total order) abstracts away some of the key intuition for figuring out *how* to frame a problem 
as binary search.

In particular, whilst practicing my DSA, I found that approaching binary search for maximally / minimally
satisfying elements from the following angle was super helpful.

For each item in your sequence, convert this item to "True" or "False" depending on whether
it satisfies the condition.

Because of the sorted-ness condition, at the end, you'll be left with a partitioned boolean array 
of the following form:

[**True**, ..., **True**, **False**, ..., **False**]

or

[**False**, ..., **False**, **True**, ..., **True**]

And that's it! Note that this formulation essentially abstracts away the *type* of your element
and instead reduces it to the problem of searching a partitioned boolean array as a function of
some "nice" condition where most of the thinking should happen. The sorted-ness condition implies 
that you only need to dynamically query logarithmic points in this sequence. Then, the "hard" part of 
reducing your search problem to binary search is trying to see if the sorted-ness invariant holds and if it does, how can 
you create a condition for each element such that the switching index satisfies the element
you're looking for in the first place. So the sequence of transformations looks like:

>Search Problem -> Boolean Partitioned Search Problem -> Binary Search

### Example: Peak in Mountain Array
Consider the problem of searching for the [peak index](https://leetcode.com/problems/peak-index-in-a-mountain-array/description/) in some integer array. 
Formally, we say that an array, $$A$$, is a "mountain" array if there exists some index $$i, 1 \leq i \leq \text{len}(A)$$
such that $$\forall j \lt i, A[j] \lt A[i]$$ and $$\forall j \gt i, A[i] > A[j]$$.

An example of a mountain array is the following:

>[1, 3, 4, 7, 11, 9, 2, 1]

And the appropriate index we should return is $$4$$, since that's the maximum of your array. Naively, you can just
argmax this seequence and return the index (which is $$O(n)$$), but we can use binary search to do this in $$O(\text{log}(n))$$. 

The key insight is that the pivot index is the only index, $$i$$, is the first index with $$a[i] > a[i + 1]$$. Under
this condition, the above array reduces to this partitioned boolean array:

>[False, False, False, False, True, True, True]

Where we omit the last element since it doesn't have a "next" element. Finally, we have two choices: we can search for
the first True element or the last False element and add 1 to the index that is returned. 

### References
>[Peak Index in Mountain Array Leetcode](https://leetcode.com/problems/peak-index-in-a-mountain-array/description/)