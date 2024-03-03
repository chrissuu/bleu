---
layout: post
title: but, what is math?
subtitle: a high level overview of the age old question
tags: [math]
---
>There are no such people. People who succeed in mathematics, like people who learn a musical instrument or a new language, spend a lot of time not understanding and feeling frustration. The path to understanding in mathematics necessarily involves, in the words of Steve Klee (4), being willing to struggle.” It is strange that people do not understand this about mathematics when it is commonplace in essentially every other field of human endeavor. The people whose stories are in this book clearly understand this fact. Some of them, for example Lola Thompson (7) and Laura Taalman (8), avidly embrace the struggle, they seek out the experience of frustration and confusion because they have realized that persistence in the face of difficulty leads to the rewards of learning and growth.
>
>From the book [Living Proof](https://www.ams.org/about-us/LivingProof.pdf) and a quote that one of my professors had written on our second homework assignment

A few weeks ago, I was talking to my friend about what math is. Like me, he enjoys music, but he studies piano performance as well as English. As we were walking back to our dorm, he told me that he's not really a numbers person and that he always struggled in highschool math classes. 

I'm sure a handful of other people are also in the same boat - they find math to be difficult. To be completely fair, some people definitely have a natural aptitude for mathematics and the sciences. But I think that the reason why math might be so difficult is because 

In the same regard, I think math should be difficult, and because it's difficult, it's fun! (Nothing in life that's good for you and fun for you is also easy for you)

### But, what is math?

In middle school and high school, most math classes have teachers throw a bunch of computational questions for you to do. For example, a common class this occurs in is precalculus or calculus, where students are asked to memorize a bunch of formulas for derivatives, trig rules, etc. Although computation is important for building your mathematical toolkit, it doesn't really teach you _why_ we learn these things. 

In the next few sections I want to outline what _math_ is. (Of course, each section could have an entire post by itself)

### Math as the study of phenomena (mathematical modeling)

It is not an overstatement to say mathematics is at the heart of everything. But what do I mean by everything? Do I mean books? Or perhaps the water bottle I threw out yesterday? What do I mean when I say math is at the heart of everything?

Simply put, every interaction you do with any object in your every day life has something to do with math! In our book example, there are machines that have carefully printed those books out, water bottles have also been molded by machines; anything and everything has something to do with math! And behind those machines, there are the mathematicians and engineers who have carefully and rigorously made them. 

This nuance becomes easier to see in the sciences, since that is where mathematics is most directly applied. Human biology needs equations to predict bloodflow and viscosity, game theory and economics needs equations to study the equilibrium of systems, physics needs equations to predict planetary motion and atoms - 

Math as a field is not just math for the sake of doing math. It is a field that allows us to study our universe - and more precisely, it is a _tool_ that lets us do just that. To have a "math" mind might mean that you are able to model problems as math problems pretty well or analyze patterns that come up in our universe and change it into math problems! (Examples of this might include game theory for modeling animal territory and behavior, or stochastic calculus for random systems like the stock market, this list is endless)

### Math as the study of problem solving

Humans are curious animals. We like things that stimulate our brains and while some people stimulate their brains with athletics, video games, board games, music, and other hobbies (on the flip side, think alcohol, drugs, sex). Others like to solve math problems because of how it stimulates their brain the right way. There is a certain and undeniable satisfaction with solving a hard problem that you've struggled with for countless hours (this is the same in athletics when you reach a goal that you might have wanted to beat for the longest time ever or finally learning that one piano piece you've always wanted to play). 

**There is no better playground for mental gymnastics than mathematics**. Once you start learning mathematics, the availability and range of puzzles that suddenly you can now start to tackle becomes bigger and bigger. And because of how broad the field of mathematics is, you can bring your other interests into mathematics and you'll usually find a related problem!

Math is a **difficult** but very rewarding subject and it is very much a universe of puzzles. 

### Math as the study of abstraction and generalization (optional)

This section is for people who know a bit more math - so feel free to skip it (or don't) if you want.

This is my personal favorite part about math - it is the study of abstraction and generalization. 

In calculus 1 / 2 for example, we learn some basic fundamentals about single variable functions, their derivatives, and their integrals, yada yada. But what's a generalization we could make? How about a function of two or three or infinite number of variables? Can we really reason about infinite value functions if we can't even graph them?

And the answer is yes! This is the most powerful part about mathematics - it is the tool that lets us make possibly infinite generalizations and abstractions of concepts that may seem intuitive in our universe, but whose abstractions make no sense whatsoever using just a "universal" intuition. 

Vector spaces over the reals? Why not vector spaces over an arbitrary vector!

This is what is often what is known as "(abstract) algebra", but of course abstractions and generalizations don't belong just in AA. Groups help us understand symmetries, vector spaces allow us to understand anything that might act as vectors, fields let us understand number systems, and etc... The power of abstraction is that if you are struggling with a problem, try giving it a structure (such as a vector space, a field, a group, or perhaps make it into a graph theory problem) and voila! Now you have access to the shoulders of countless giants who have proven thousands of theorems about them. 

### Math as the study of computation
In the early 17th century, "computer" referred to "one who computes", or a physical person who would sit down to do countless arithmetic operations every single day. This was an important part of mathematics, since computation is so intricately tied with it.

<p align = "center">
  <img src="../assets/HollerithMachine.jpg" />
</p>

Or, in the year 1614, a book titled "Mirifici Logarithmorum Canonis Descriptio" was published, that had thousands upon thousands of calculations of logarithms, exponents, sines, cosines, etc, at different values. (This was before the age of calculators) This book was to be used as a reference for mathematicians doing research, such as astronomers that needed precise values for sine and cosine at various angles. Although some entries were inevitably erroneous, the process of computation is deeply linked with mathematics as something that is very important.

Without doing any computation, there is really no way to reason about certain problems. It is a skill that mathematicians need (the bread and butter) and it is followed by the skill of algebraic manipulation. Take for instance the following integral:

$$\int sec(x) dx$$

Without pulling from highschool calculus formulas, how would you integrate this? 

It's a hard (and possibly impossible integral) without the insight of a powerful algebraic manipulation (the identity element for multiplication):

$$\int sec(x) dx = \int sec(x) * 1 dx = \int sec(x) * \frac{sec(x) + tan(x)}{sec(x)+tan(x)} dx $$

$$\Leftrightarrow \int \frac{sec^2(x) + sec(x)tan(x)}{sec(x)+tan(x)} dx $$

And substituting $$u = sec(x) + tan(x)$$, $$du = sec(x)tan(x) + sec^2(x) dx$$, we get that 

$$\int sec(x) dx = \int \frac{du}{u} = ln(u) + C = ln|sec(x)+tan(x)|+C$$

Computations allow us to get from one place to another, but the skill of algebraic manipulations lets us creatively use these computational abilities; This is also why we learn these algebraic properties, manipulations, and computation techniques from such a young age. However, it is very much a shame that teachers don't have a good answer to _why_ we learn the math we do, apart from the lousy answer we sometimes get: taxes, tips, and tabs. (Seriously? Who uses basis vectors and span for calculating 30% tip on steak dinners???)

### Summary

I think in some way, the education system has failed math: we start with tedious work with no rhyme or reason as to why we have to learn these tedious counterparts of a rather beautiful subject. It's sort of like climbing an apple tree to get an apple but by the time your highschool education ends, you either never get an apple or you do, but you don't taste how sweet it is. Once in college, the freedom of choosing your classes becomes greater, and those that struggled in highschool with mathematics might never look twice on taking another math class. 

#### But where can I start?

The best class to take if you've struggled with or hated math in highschool, in my opinion, is a class that teaches you mathematical modeling. Introduction to game theory, introduction to theoretical computer science, introduction to theoretical chemistry, introduction to discete mathematics, are all good classes that teach you "mathematical modeling", or the process of converting universe phenomena into math. That way, you get the best of both worlds: math as it is applied and math as it is computed. 

Good luck!

References: 
>[Living Proof](https://www.ams.org/about-us/LivingProof.pdf)
>
>[Mirifici Logarithmorum Canonis Descriptio](https://en.wikipedia.org/wiki/Mirifici_Logarithmorum_Canonis_Descriptio)