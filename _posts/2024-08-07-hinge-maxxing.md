---
layout: post
title: how to hinge
subtitle: the stable marriage problem (pt3)
tags: [cs, graph theory]
type: nr
---

### Introduction
This is the last of a three part series that will talk about matchings! This part will be for the layman and talk about the Gale-Shapley algorithm in practice. Namely, the popular dating app Hinge, that implements Gale-Shapley!

### Dating apps and the like

From the Hinge website: 

>Our recommendation algorithms are designed to help compatible daters find each other and get on great dates. We suggest people based on the preferences each dater sets in the app (such as age, distance, family plans and more), who you are likely to like, and who we believe will like you back – all based on previous interactions. Your interactions with other daters - who you send comments to, who you’re having conversations with, who you’re intentionally engaging with – may all be used to continually adjust the predictions as the recommendation algorithms learn more about your preferences and mutual compatibility.
>
>Our Most Compatible feature (which **runs on a combination of machine learning and the Nobel-prize-winning Gale Shapley algorithm**) suggests daters recommended by the algorithm - with the goal of getting all daters out on great dates. Your Most Compatible feed refreshes every 24 hours based on your latest activity, such as any updated preferences, dealbreakers, and profiles recently liked or skipped.

The most important idea of the Hinge app, like other dating apps, is to recommend possible matches on your feed. 

Hinge uses a combination of ML and the Gale-Shapley algorithm to recommend potential partners. 

### Creating a dating algorithm

How does Hinge create these recommendations? 

**Disclaimer: All writing after this point is completely theoretical. I have not been on the Hinge dev team or even used Hinge before. What I do have is a semi-working knowledge of the ideas behind it**

First, daters sets preferences: "... age, distance, family plans and more". This comes from the information that you give to the Hinge app. 

What likely happens is that an initial preference list / ranking is created to create subproblems. That is, it wouldn't be ideal to try matching the 20million + people that are on hinge with each other. This would be a computationally ridiculous and impossible task to conduct efficiently. 

Instead, Hinge will take a subset of people, based on these initial preferences, and create a list. 

This is where Gale-Shapley will first be used. Your Hinge "recommended" feed will be comprised of your most compatible (stable) matching, based on these precomputed preference lists. 

One problem though: Gale-Shapley will only output one matching! This is inconsistent with what we know about Hinge. That is, Hinge gives you a *feed* of people / potential partners. So how do we get more potential partners?

This is where ML plays a significant role: depending on who you interact with, your preference list will be updated and Gale-Shapley will be recomputed on these new preference lists. When preference lists are updated, the stable matching outputted by Gale-Shapley will also change due to the large userbase of Hinge. 

Hence, your future potential matches that show up on your feed depend on how you interact with the app. 

Another thing that Hinge might implement to increase the number of potential matches is to recompute Gale-Shapley after removing one of your initially set preferences such as "age, distance family plans and more". 

For example, suppose the dating profile for "Billy":

>**Billy**
>
>Age: 22
>
>Height: 5' 9"
>
>Hometown: Queens
>
>Looking for people in: NYC
>
>College: NYU

Gale-Shapley (the first time around) will compute the matchings on all of Billy's preferences. Then, Hinge might change some of the details in the preferences to, for example:

>**Billy v2**
>
>Age: **22, 23, 24, 25**
>
>Height: **5' 9", 5' 10", 5' 11"**
>
>Hometown: Queens
>
>Looking for people in: **NJ, NYC**
>
>College: NYU

Even though Billy's age is not 23, 24, or 25, and his location is not NJ, small changes in his profile allows for more stable matches to be created. This allows for more people to see Billy in their recommended feed. No one will exactly fit everyone's dating preferences, so these compromises make sense. Add on to the fact that the matchings are guaranteed to be stable, Hinge's success is likely due to their robust ML model that creates the initial preference lists. 

### Overview

There are various ways that graph theory and computer science interact with the real world. Dating apps are one example, but things like web search, networks, and a lot of other social media apps depend on the ideas from graph theory and computer science. 

### References

>[Hinge Website](https://hinge.co/ai-principles)
