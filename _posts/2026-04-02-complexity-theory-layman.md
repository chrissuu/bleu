---
layout: post
title: the amazing theory of complexity!
subtitle: ramblings on complexity theory (pt 1)
tags: [cs]
type: nr
---
Four months ago, this blog turned 2 years old! As a result, maybe I'll try to go over some of my favorite ideas from the field of computational complexity theory (CCT), which has been the primary motivator for this blog, and recount the several ideas that I've encountered along the way[^1]. 

# What is CCT?
As it turns out, **almost everything we encounter in our day-to-day life is a computation**. By computation, I mean, at a high level, some "process" which ingests "information" and "transforms" it[^2]. Since we're human, it becomes very natural to ask questions that help us probe what a "computation" really is. 

>*How long* does computations take? *How much space* do we need to do a computation? Can *flipping coins* help us do a computation faster (i.e., can randomness help us do a computation)? What's the *fastest* time that some computation can be completed? What sorts of computations does our universe allow? What sorts of computations could exist in other universes? What is the nature of a proof?

Indeed, when applied to more formal systems, these questions are precisely what CCT tries to study and determine answers to. In particular, CCT tries to formalize the notion of a "resource" and tries to figure out how much of it we need to do something interesting. More interestingly, however, is that when we begin to ask these questions (and answer them), we get a field that is capable of doing "meta"-reasoning.

At the end of each section, I'll pose some questions which follow as interesting follow ups to that particular section. My hope is that this blog post will sort of motivate and show the types of (meta-)questions that might arise as we learn more about computation.

## Algorithms & Computers
The language of CCT is mathematics, but the systems that we use to analyze CCT is mostly with respect to these things we call "algorithms" and "computers". "Computers" are the medium in which a computation is performed. We must define this, because a computer is what actually "performs" the computation. In other words, the "computer" is exactly the "process" in the above definition[^3].

So what is an algorithm?

>"An algorithm is a *finite* answer to an infinite number of questions" - Stephen Kleene

The above might be hard to wrap your head around, but here's the general idea: suppose you wanted to multiply together two numbers. Obviously, there are an infinite number of numbers, so it doesn't make much sense to try to have an infinite-sized "rule book" which tells you "ahh yes, 1x1=1, 1x2=2, 1x3=3.... 100x100=10000, etc" (this would be impossible for the human brain, since our brain only has finite memory). Instead, we've learned in gradeschool how to multiply two arbitrary numbers. Indeed, this rule which we've all internalized is a *finite* description to an infinite number of questions (what is the product of $$a$$ and $$b$$?), and so... (drumroll) it's an algorithm!

Here, you might wonder a few things. Amongst them:

1. Is an algorithm allowed to answer only a finite number of questions?
2. Are there really that many "categories" of questions that have an infinite number of questions?

To answer the first question: suppose that your category of questions only had a finite number of them. In this case, someone could just write up a GIGANTIC book containing the answers to each of your questions and give them to you. Since there are only a finite number of questions, this is indeed no problem, unlike the question before, which had an infinite number of potentially ask-able questions.

To answer the second question: yes! The question "what is the product of $$a$$ and $$b$$" has an infinite number of variants, but it's only one *type* of question[^4]!

# CCT, Mathematics, and the Sciences
Though computational complexity theory (CCT) is often seen as a subfield of computer science, I like to think of computer science as a subfield of CCT. I would go as far as to say that almost all fields that practice the sciences are relevant to CCT, and in a sense, subfields (applied, if you will) of CCT. This viewpoint is not immediately clear, but I hope to elucidate this point throughout this post. 

For one, CCT has matured to become a field which, to my knowledge, uses ideas from almost all areas of mathematics. If you find this hard to believe, I'll leave a footnote[^5]. There are few fields whose study requires the enlistment of so many large and well-studied fields as CCT. These connections between CCT to other areas of mathematics, on a second thought, maybe isn't too surprising. **'Doing mathematics' is fundamentally a computation.**

In a [letter from Kurt Godel to von Neumann](https://www.cs.cmu.edu/~odonnell/15455-s17/hartmanis-on-godel-von-neumann.pdf), he hypothesized whether machines, or an algorithm, could prove arbitrary statements in some proof system, and the consequences of being able to do this efficiently. Naturally, this lends itself to some interesting questions itself. 

### Questions
>What is the nature of mathematics? Do we discover mathematics or create it? Is mathematics only syntactic manipulation? Should mathematicians look for "meaning" in syntax?

## Nature of Mathematics
To say that mathematics is only syntactic manipulation is essentially like saying that painting is only putting brush strokes on a canvas. Both of these are true, yet we *feel* as though there is some notion of "form" or "beauty" or "elegance" when all these small movng parts are put together. Locally, mathematics might look like syntactic manipulation. Locally, painting may look like brush strokes on a canvas. Yet, when you take a step back to see what you've created, you're able to derive some sense of satisfaction from it. In other words, mechanical and locally uninteresting "computations" can come together to make something quite elegant indeed.

It is most often the case that for the largest and deepest ideas in mathematics, you need to be able to internalize the semantics, or, the meaning of the syntax. Almost every deep result in mathematics has been the result of carving out the meaning from syntax, and creating new meaning. The syntactic manipulation rules are only there to guarantee the correctness of what you've done. 

Interestingly, this point leads us to answering the second question that we proposed in the previous section. 

>Do we discover mathematics or create it?

It seems to be both! The syntax of mathematics is created by us, yet it seems really likely that an advanced-enough alien civilization will likely have created similar constructions to us. Constructions such as finding the area of a triangle, having a constant for $$\pi$$, or even proving very abstract results on the variation of Fermat's Last Theorem. This is only possible because the space of potential mathematical semantics which the syntax attempts to capture, is almost surely the same across all universes[^6]!

### Questions
>What should be the role of humans as it pertains to mathematics? Does AI need to understand the structure of math in order to do math? Why does 'doing math' feel hard? Can we show that 'doing math' is provably hard? Is there an efficient algorithm which can prove all provable theorems under some formal system? If the role of syntax is only for correctness guarantees, is there a more formalized way to combine ideas in the semantic space of mathematical objects instead?

## Church-Turing Thesis
The Church-Turing Thesis says the following.

>Anything that is physically computable in the universe can be done by a Turing machine (computer).

Note that this statement is not a "theorem", in the sense that it is proven or disproven. Rather, it is a *remark* about *observations* that we've seen in our universe, and what we make of them.

At a high level, it says: for any computation that we can observe in the universe, this computation can be "simulated" on a computer. In other words, any time you see the universe (1) ingesting information (2) transforming that information (3) updating the state of the universe, a computer can simulate it. For instance, back to our falling apple example from footnote 1, it's not difficult to see that there exists a computer program which can take in the description of an apple, its height, and then output the trajectory it will take through the laws of physics. 

More simply put: any time you see something occur in the universe, Church Turing Thesis says there exists a computer which can simulate it.

Ok, so this seems reasonable. Anything the universe can do, I can simulate it on my laptop, assuming that I understand the underlying mechanics of the computation. But recall, complexity theorists are not really in the business of whether something is "possible" but whether something can be done *efficiently*. 

The Extended Church Turing Thesis says the following.

>Anything that is physically computable in the universe can be done **efficiently** by a Turing machine (computer).

This statement is a little less believable. For instance, simulating the fall of an apple to *perfection* would require us to know quite literally every single detail about the apple down to the number of atoms, *and then* also know the underlying physical mechanics (air resistance, gravity, etc etc) to be able to simulate just one apple falling. It's not immediately clear if this is easy to do on a computer[^7].

Furthermore, there seems to be evidence that this is not true, due to the existence of quantum computers[^8]. Hence, this becomes an interesting phenomena to study. 

### Questions
>What makes quantum computers different from classical computers? Do they offer more computational power? Can we solve problems on a quantum computer that a classical computer cannot? These questions are posed in the field of quantum computational complexity theory.

# Computational Hardness
One of the main questions that tend to be posed in CCT relates to the notion of computational hardness. 

>*How difficult* is it to carry out some computation? How can we show that we've found the best way to do this computation? Is it even possible to show that this is the best way to do a computation?

For instance, recall the earlier example of multiplying two numbers and the gradeschool multiplication algorithm. Is this gradeschool multiplication algorithm the fastest way to multiply two numbers?

As it turns out, there's actually a more efficient way to multiply two numbers together (for some intuition: multiplying two large numbers is expensive so you can break the number up into smaller pieces, multiply those, and then combine these results together)!

The naive algorithm for multiplication was not the best one, so how do we *know* that this new algorithm that we've come up with is the best possible one? Could it be the case that there's a multiplication algorithm which lets us multiply two numbers by just doing some really small number of additions?

CCT is the field that gives us the tool to answer these questions, so that we don't have to look for more efficient multiplication algorithms once we've proven "lower bounds". Unfortunately, the mathematical tools we have today are not really powerful enough to answer the most interesting questions[^9].

As one example, consider the process of **factoring** a number into its prime factors. Factoring is the opposite operation of multiplication. Intuitively, factoring *feels* more difficult to us than multiplication.

>Try factoring 1377

>Try multiplying 17*81

Hopefully you'll get the correct answer that 17*81=1377, but multiplying the two numbers was much more easier than factoring 1377 into 17\*9\*9. Why do some problems feel more "difficult" than other problems? How can formally show that one problem is more difficult than another?

## Reductions
Reductions is an important tool in CCT that lets us gauge the difficulty of one problem with respect to another. Even though it's hard to *prove* that a certain problem is difficult to solve (compute), it turns out that showing that one problem is more or less difficult than another one is pretty straightforward. 

In order to not be as rigorous, I'll just keep it as high level as possible: Let's say you have two questions types, $$A$$ and $$B$$. Suppose that I was able to come up with a clever trick such that questions in the question type of $$B$$ can be answered very quickly. Later down the line, someone shows that, if you can answer question types of $$B$$, then you can actually answer question types of $$A$$. Hence, answering question types of $$A$$ has now become easy!

Vice versa, if someone were to show that question types of $$A$$ are naturally very, very difficult to answer, and later down the line someone shows: if you can answer question types of $$B$$, then you can actually answer question types of $$A$$, then answering question types of $$B$$ must be just as difficult if not more difficult than answering question types of $$A$$!

Hence, we now have a pretty solid method for comparing the difficulty of question types[^10].

### Questions
>Why should anything be 'provably' difficult to do? Is it possible to show that there isn't a better way to do certain things (i.e., computations)? Can you come up with other problems that feel difficult to solve? Can you come up with two question types, $$A$$ and $$B$$, such that one can be solved using answers from the other?

# CCT and the Nature of the Universe
So far, we've seen that CCT is rather interwoven into mathematics, and as corollary, into many of the sciences that we care about. We've seen the Godel machine, a thought experiment or conjecture, if you will, about the consequences of something that is able to do pure syntactic manipulation to solve mathematical proofs. We've seen the Church Turing Thesis and that there exists some nontrivial connection between the universe we live in and the computation it allows. Finally, we've seen a quick example about natural computations like multiplication and factoring and the idea of computational hardness.

It seems like CCT is about more things than it initially lets on, and that is sort of what I would like for you, as the reader, to understand. CCT allows us to reason about our univere. Broadly put, if physics studies *how* the universe works the way it does, then CCT could be seen as studying *why* the universe works the way it does. What problems are naturally difficult in our universe? What sorts of computers would we need to efficiently solve harder problems?

# Meta Results and Meta Questions
With much of the primer on some of the big ideas in CTT out of the way, this last section will cover some explicit results that I feel very strongly highlight CCT's abilities to make fascinating connections to our universe, our understanding of the universe, and also about mathematics (as in, what does mathematics say about mathematics?, what does mathematics say about our universe?, what does mathematics say about the computation which is possible in our universe?). 

## Halting Problem
A desiderata, perhaps, is a theorem which proves that *any* computation can be implemented on a computer. In other words, for any computation or phenomena we can think of, even super abstract phenomena, does there exist a computer which can simulate this computation? Intuitively, it seems like this should be the case. Why should there *exist* a description of a computation, yet, no computer which can carry out said computation.

Unfortunately, this desiderata is not met, and even more strongly, provably so. Alan Turing, one of the founder of computer science (for which the Turing machine is named after) showed in his seminal paper that not every computation for which there exists a description of, can be implemented on a computer[^11].

## P vs. NP
The P vs. NP problem is one of the most well known (and perhaps the most difficult) open problems in computer science. It is one of the Clay Mathematics Institute's Seven Millenium Problems, for which there is a million dollar reward for solving it. 

So why is this problem so important?

So far, we've talked about "question types", which are essentially just a package of a bunch of different question variants. If an algorithm is a finite description for answering an infinite number of questions, then a question type is a finite description to an infinite number of questions.

However, there is also a new notion we need to talk about: complexity classes. One can think of a complexity class as a finite description to an infinite number of question types. Simply that there even exists a finite description to an infinite number of question types is quite amazing to me. 

However, it actually turns out that in most complexity classes, all the question types inside the complexity class can actually be answered if you know how to answer the hardest question inside the complexity class. This is truly one of the most amazing results. 

In the P vs. NP question, P and NP are both complexity classes. You can think of P as the complexity class of questions that can be answered easily (for instance, multiplying two numbers is in this complexity class). On the other hand, NP is the complexity class of questions whose *answer* can be checked easily. 

For instance, going back to our factoring example from earlier, we have some intuitions that factoring a number into its prime numbers is difficult. However, if I were to *give you* the prime factors themselves, you could multiply these prime factors together and see for yourself if these prime factors were actually the prime factors. Since multiplication is easy to do, the **problem of factoring a number is easy to check.**

The P vs. NP question asks the following. Is the complexity class P equal to the complexity class NP? In other words, if you can *check* answers to some question type efficiently, is this question type *solvable* efficiently? 

Applied to our example: if someone were to show that P equals NP, then there must exist a fast algorithm for factoring a number. On the other hand, if someone were to show that P doesn't equal NP, then there must NOT exist a fast algorithm for factoring a number. 

Most complexity theorists believe that P does not equal NP. That is, just because you can efficiently check the answer to question types, it does NOT mean you can solve them easily. This is aligned with our intuition, but we have yet to prove it formally. 

### Questions
>Why should there be a question type which lets us answer all question types in some complexity class? Are all question types inside some complexity class really the same question? Are question types just variants of other question types? What do I mean when I say, "the hardest question" inside the complexity class? Can you come up with other problems that feel easy to check the answers to, but feel hard to solve (can you see why a game of Sudoku might meet this property)? Is P vs. NP a fundamental rule of our universe (that is, might an alien civilization discover the P vs. NP question just like us)? Is 'doing math' one of these "hard" problems? What does this say about AI which can solve math problems?

## Nature of Randomness
Earlier, I asked, "can *flipping coins* help us do a computation faster (i.e., can randomness help us do a computation)?"

It turns out that, yes, flipping coins or some source of randomness can help us do computations faster. 

It may seem strange why this should be the case or why this should be true. However, consider population sampling.

One of the core ideas of statistics is that if you want to learn something about an entire population, you can randomly sample some smaller subset of this population and ask them the question instead. Assuming you've done this part judiciously, you can actually learn a whole lot of interesting things about an entire population by only finding out the answer to your question for a smaller subset.

A more concrete example: suppose you want to figure out what the average height for an adult male in the US is. Of course, you can find every single adult male, tabulate their heights, and compute the average, but this would take forever! Instead, just obtain a list of all adult males in the US (legally, I hope), take some random sample, say ~1,000 of them, track them down, and compute the average of their heights. We've effectively reduced the amount of computations required from ~150,000,000 to ~1,000. 

In this example, randomness helped us find the average of their heights, but this is of course not without **error**. Randomness allows us to compute things but at the price of error. By *increasing* the number of people that you pick, you *decrease* the error.

### Questions
>Do you get the same power from randomness with a biased coin flip? What if you had weak sources of randomness -- do these help with computations? For problems which randomness benefits, is there a way to remove randomness from these algorithms (i.e., derandomization)? Is there anything that is truly "random" in our universe[^12]? If there is no randomness, then could there be a machine which can predict what a human will do in the next second, minute, or even years later down the line?

# Conclusion
Hopefully you were able to learn a few things about what sorts of questions are asked in CCT. The main takeaway that I wish you leave this post with is that mathematics can help us reason about the universe and our own existences in very strange ways indeed. For some reason, the universe is well-defined and complex, yet these complexities are stripped bare using the tools provided by physics and mathematics and CCT. As humans, we like to solve problems. It is in *our nature* to solve problems (both small and large), and CCT provides a rather unique perspective on what it means to solve problems and what sorts of resources one needs to solve them. To me, this is the essence of CCT and CCT provides such an elegant and beautiful language for discussing these ideas. 

### References
>[Kurt Godel's Letters to von Neumann](https://www.cs.cmu.edu/~odonnell/15455-s17/hartmanis-on-godel-von-neumann.pdf)
>
>[Avi Wigderson's Talks on Randomness](https://www.youtube.com/watch?v=Jz1UoAWD80Q)


[^1]: This post shouldn't be too technical, and most people should be able to follow along, at least at the high level, even if you haven't done math in ages. Part 2 of this post series will cover similar ideas but in more mathematical rigor. 

[^2]: Here are some examples to help hone in this point. When you search something up on your browser, the software (the "process") will ingest your searched words (the "information"), and then return you a page filled with the results (here, your searched words were "transformed" into the page of results). Another example: when an apple loosens from its tree, the universe's rules of physics (the "process") will inspect the state of the apple (the "information") and then have it fall to the ground (the "transformation"). **Observe that computation doesn't really have to happen on a computer. However, it just so happens that computers are 'good' at doing computations.**

[^3]: If you read footnote 1: according to our definition of a "computer", the universe is a computer. 

[^4]: Try to come up with your own type of question that might have an infinite number of variants. If you can, try to show that there are infinite *types* of questions that have an infinite number of variants.

[^5]: Off the top of my head, here are a few connections: Graph theory for expander graphs and PCPs. Number theory for cryptographic protocols. Combinatorics in the study of circuits. Formal logic in the study of proof theory. Analysis/Fourier Analysis in the study of boolean functions.

[^6]: Perhaps a tangent on AI that does math. Because semantics are preserved between syntactical systems, we may have a criteria for what sorts of AI will be capable of solving difficult math problems. They should be able to reason about the *semantics* of the syntax, rather than trying to reason about the syntax. It's unclear how well current LLMs are able to do this, but it seems that reasoning models have, in their latent space representations, some notion about the semantics of the syntax and not just a syntactical rulebook.

[^7]: The well definedness of this is a different problem as well. I.e., recall we care about there being an infinite number of variants to a single question type. Is there an infinite number of variants of apples falling from the tree? Maybe, but perhaps this example isn't too interesting. However, it turns out, there are truly natural problems, ones related to quantum physics, that seem to be difficult for us to simulate on a classical computer.

[^8]: It is believed that a regular computer cannot *efficiently* simulate what a quantum computer can do. Hence, we believe that the Extended Church Turing Thesis is probably false.

[^9]: Questions such as P vs. NP, P vs. BPP, P vs. NC.

[^10]: Here's a concrete example of this. Suppose you had a bracelet of beads which alternates in colors: red, white, red, white... and so forth, until it wraps back to the first bead which is red. Now, this bracelet is getting pretty old so you want to replace the beads, but you're not too sure how many beads you will need. Hence, you'd like to count the number of beads your current bracelet has. One way to do so would be to count all the beads. However, another way to do so would be to count all the red beads, and multiply by two! Counting all the red beads is the "harder" problem (even though there are less beads), since you can use this information to count ALL the beads. In fact, the other direction also holds true! If you wanted to know how many red beads there are, you could count all the beads and divide by two. In this case, both problems reduce to each other.

[^11]: Take some time to understand what this is saying. There exists some description of a problem, or a computation, for which you can not write down an algorithm which solves it. Even if you had infinite time and wrote down all possible programs, this problem would not be solved by one of the programs you have written down. 

[^12]: Avi Wigderson, a theoretical computer scientist praised for his work on derandomization has an interesting perspective on randomness: "randomness is powerful in the eyes of the beholder", or in our case, how much compute power we have. For instance, in the setting of coin flipping, we treat it as "random" since, across several coin tosses, no human can accurately predict, **before** the coin lands, what face the coin will land on. Thus, with respect to humans, coin tosses are "sufficiently random". However, suppose that we had 100 slow motion cameras and a super computer which can process all this data. In this case, it isn't that surprising to think that this supercomputer could accurately predict (maybe to 95% accuracy) what face the coin will land on before it lands! So is anything really random? Or to talk about randomness, do we need to presuppose some model that **observes** the randomness for discussions about randomness to be meaningful? These ideas are talked about in [this interesting talk by him](https://www.youtube.com/watch?v=Jz1UoAWD80Q) and I strongly suggest you take a listen!