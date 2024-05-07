---
layout: post
title: spectral theory for fibonacci
subtitle: an interesting application of linear algebra
tags: [math, linear algebra]
---

### Introduction

While linear algebra may be naively thought of as a framework for solving systems of linear equations, the abstraction it provides allows us to do a lot more than just that! 

In this post we will take a look at one such example: the fibonacci sequence

### Fibonacci Sequence

The fibonacci sequence is a recurrence relation defined as such:

Let $$f_0 = 0$$, $$f_1 = 1$$, and $$f_n = f_{n-1} + f_{n-2}$$. That is, take the previous two terms and add them together to get your next term! 

How can we find a closed form expression for the nth term?

### Exploration of spectral theory

Recall the definition for eigenvectors and eigenvalues for a matrix $$\textbf{A}$$ satisfies the following expression:

$$\textbf{A}\vec{x} = \lambda \vec{x}$$

Where $$\vec{x}$$ is the associated eigenvector for the eigenvalue, $$\lambda$$. Why is this important? Notice if we do a left multiplication of $$\textbf{A$}$ on both sides, we get the following expression: 

$$\textbf{A}^2\vec{x} = \lambda \textbf{A}\vec{x}$$

The RHS simplifies to the following, since $$\textbf{A}\vec{x} = \lambda \vec{x}$$:

$$\textbf{A}^2\vec{x} = \lambda^2\vec{x}$$

In other words, we've found an easy way to express repeated left multiplications on a system in terms of the vector of interest and powers of a scalar constant.

We can induct on n to prove the following is true: 

$$\textbf{A}^n\vec{x} = \lambda^n\vec{x}$$


### Connection to relations 

If we can somehow encode our sequence (the fibonacci sequence) into a matrix $$A$$ and $$\vec{x}$$, then it might be possible to find some sort of closed form expression for the fibonacci sequence! Notice that there are some parallels between the power $$n$$ in the above expression and the nth term of a sequence. This connection to spectral theory and linear algebra is pretty intuitive, because the terms of the fibonacci sequence can be described as linear combinations of previous terms. 

Since the fibonacci sequence is related by the previous two terms computed, a good choice for the vector $$\vec{x}_n$$ might be:

$$\vec{x}_n = \begin{pmatrix}f_{n+1}\\ f_{n}\end{pmatrix}$$

Then, we can try finding what matrix $$\textbf{A}$$ that $$\vec{x}_n$$ is the eigenvector to. 

Notice that we may apply our definition for the fibonacci sequence onto the terms $$f_{n+1}, f_n$$. And so we're left with the following: 

$$\vec{x}_n = \begin{pmatrix}1*f_n + 1*f_{n-1}\\ 1*f_{n} + 0*f_{n-1}\end{pmatrix}$$

Which allows us to say that our choice for the matrix $$\textbf{A}$$ could be:

$$\textbf{A} = \begin{pmatrix}1 & 1\\ 1 & 0\end{pmatrix}$$

It's easy to see that:

$$\textbf{A}\vec{x}_{n-1} = \begin{pmatrix}1 & 1\\ 1 & 0\end{pmatrix} \begin{pmatrix}f_{n}\\ f_{n-1}\end{pmatrix}= \begin{pmatrix}f_{n+1}\\ f_{n}\end{pmatrix} = \vec{x}_{n}$$


Inductively, this also means that:

$$\vec{x}_{n} = \textbf{A}^{n}\begin{pmatrix}1\\ 0\end{pmatrix}$$

Where the vector $$\begin{pmatrix}1\\ 0\end{pmatrix}$$ comes from the base case defined by the fibonacci sequence.

Like we talked about before, now we want to connect this to some ideas in spectral theory, particularly that of eigenvectors of eigenvalues.

The procedure for finding the eigenvectors and eigenvalues of $$\textbf{A}$$ is pretty straightforward so I'll leave it as an exercise for you to verify, but here they are:

$${\lambda}_1 = \frac{1}{2} + \frac{\sqrt{5}}{2}$$

$${\lambda}_2 = \frac{1}{2} - \frac{\sqrt{5}}{2}$$

$$\vec{\lambda}_1 = \begin{pmatrix}\frac{1}{2} + \frac{\sqrt{5}}{2}\\ 1\end{pmatrix}$$

$$\vec{\lambda}_2 = \begin{pmatrix}\frac{1}{2} - \frac{\sqrt{5}}{2}\\ 1\end{pmatrix}$$

These eigenvectors are clearly linearly independent, this detail will be important later.

For now, see that the base case vector, $$\begin{pmatrix}1\\ 0\end{pmatrix}$$, can also be rewritten as such:

$$\begin{pmatrix}1\\ 0\end{pmatrix} = \frac{1}{\sqrt{5}}\vec{\lambda}_1 - \frac{1}{\sqrt{5}}\vec{\lambda}_2$$

Verify this for yourself.

We now have all the tools necessary to finish the problem. 

Recall from earlier the following relation:

$$\vec{x}_{n} = \textbf{A}^{n}\begin{pmatrix}1\\ 0\end{pmatrix}$$

Hence, we have:

$$\vec{x}_{n} = \begin{pmatrix}f_{n+1}\\ f_n = \end{pmatrix}  \textbf{A}^{n}\begin{pmatrix}1\\ 0\end{pmatrix}$$

Substituting the above base case representation:

$$\begin{pmatrix}f_{n+1}\\ f_n \end{pmatrix} = \textbf{A}^{n}\begin{pmatrix}1\\ 0\end{pmatrix} = \frac{1}{\sqrt{5}}\textbf{A}^{n}\vec{\lambda}_1 - \frac{1}{\sqrt{5}}\textbf{A}^{n}\vec{\lambda}_2 $$


Since $$\vec{\lambda}_i$$ are eigenvectors for A:

$$\begin{pmatrix}f_{n+1}\\ f_n \end{pmatrix} = \frac{1}{\sqrt{5}}\textbf{A}^{n}\vec{\lambda}_1 - \frac{1}{\sqrt{5}}\textbf{A}^{n}\vec{\lambda}_2 = \frac{1}{\sqrt{5}}{\lambda}^{n}\vec{\lambda}_1 - \frac{1}{\sqrt{5}}{\lambda}^{n}\vec{\lambda}_2$$

Multiplying the matrices out according to the base cases, we have:

$$\begin{pmatrix}f_{n+1}\\ f_n \end{pmatrix} = \frac{1}{\sqrt{5}}{\lambda}^{n}\vec{\lambda}_1 - \frac{1}{\sqrt{5}}{\lambda}^{n}\vec{\lambda}_2 = \frac{1}{\sqrt{5}}\begin{pmatrix} 
({\frac{1 + \sqrt{5}}{2}})^{n+1} -  ({\frac{1 - \sqrt{5}}{2}})^{n+1} \\ ({\frac{1 + \sqrt{5}}{2}})^{n} -  ({\frac{1 - \sqrt{5}}{2}})^{n}\end{pmatrix}$$

By vector equality:

$$f_n = \frac{1}{\sqrt{5}}({\frac{1 + \sqrt{5}}{2}})^{n} -  \frac{1}{\sqrt{5}}({\frac{1 - \sqrt{5}}{2}})^{n}$$

Coincidentally, the terms within the exponents involved are exactly the golden ratio! That is:

$$f_n = \frac{\varphi^{n} -  (-\varphi)^{-n}}{\sqrt{5}}$$

### Overview

Linear algebra is an interesting perspective on solving linear recurrence relations. It allows us to come to a closed form solution in a really elegant way! The fibonacci sequence is a textbook example of linearn recurrence relations, but see if you can derive other closed forms using the tools from linear algebra!

### References

>[Golden Ratio (wiki)](https://en.wikipedia.org/wiki/Golden_ratio)
>
>[Fibonacci Sequence (wiki)](https://en.wikipedia.org/wiki/Fibonacci_sequence#Relation_to_the_golden_ratio)