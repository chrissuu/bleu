---
layout: post
title: feynman's integral trick!
subtitle: feynman's integral trick, made by Leibniz?
tags: [math]
type: r
---

The motivation for this post comes from a putnam problem I came across the other day (A5 problem from Putnam 2005, linked below):

$$\int_0^1 \frac{\ln(x+1)}{x^2+1}\,dx $$

Clearly not the most elementary integral - so how can we tackle it?

### A clever trick...
Although this has gained some popularity as "Feynman's Trick" after the renowned late physicist Richard Feynman, most credit goes to Leibniz's "differentiation under the integral sign" lemma, which says that:

$$\frac{d}{dt}\int_a^b f(x,t) dx  = \int_a^b \frac{\partial}{\partial t} f(x,t) dx  $$

Using this trick and some clever insight, the problem becomes more manageable! There are two heuristics that we can use when seeing if an integral get be solved using this trick. 

### Heuristic 1
Notice we may write our integral above as a function of x and some constant, $$\alpha$$:

$$I(x, \alpha) = \int_0^1 \frac{\ln(\alpha x+1)}{x^2+1}\,dx $$

It is standard to use the big "I" to represent our function. When using this trick, what we want is that differentiating our integrand with respect to alpha, simplifies the integrand (**this is heuristic 1**). 

Notice:

$$f(x, \alpha) = \frac{\ln(\alpha x+1)}{x^2+1} \Rightarrow \frac{\partial f(x, \alpha)}{\partial \alpha} = \frac{x}{(\alpha x+1)(x^2+1)}$$

We've removed the nasty logarithm and turned our integral into something more managable!

$$\frac{dI(x, \alpha)}{d\alpha} = \int_0^1 \frac{x}{(\alpha x+1)(x^2+1)}\,dx $$

After some partial fraction decomposition (it's tedious to type out so I leave it out lol):

$$\frac{dI(x, \alpha)}{d\alpha} = \int_0^1 (\frac{1}{\alpha^2 + 1})[\frac{x + \alpha}{1 + x^2} - \frac{\alpha}{1 + \alpha x}]\,dx $$

$$ \Leftrightarrow \frac{dI(x, \alpha)}{d\alpha} = (\frac{1}{\alpha^2 + 1})\int_0^1 [\frac{x + \alpha}{1 + x^2} - \frac{\alpha}{1 + \alpha x}]\,dx $$

$$ \Leftrightarrow \frac{dI(x, \alpha)}{d\alpha} = (\frac{1}{\alpha^2 + 1})[\frac{ln(1+x^2)}{2} + \alpha \text{arctan} (x) + ln(1 + \alpha x)]$$

We must evaluate our integral at the bounds 0 to 1 and get:

$$ \Leftrightarrow \frac{dI(x, \alpha)}{d\alpha} = (\frac{1}{\alpha^2 + 1})[\frac{ln(2)}{2} + \alpha \frac{\pi}{4} + ln(1 + \alpha)]$$


### Heuristic 2

Back to our original integral:

$$I(x, \alpha) = \int_0^1 \frac{\ln(\alpha x+1)}{x^2+1}\,dx $$

Notice that setting $$\alpha = 1$$ returns our original integral:

$$I(x,1) = \int_0^1 \frac{\ln(1* x+1)}{x^2+1}\,dx = \int_0^1 \frac{\ln(x+1)}{x^2+1}\,dx  $$

From where we left off, what we have is not $$I$$ but rather, $$I'$$ with respect to alpha. Hence, we discuss our **second heuristic**!! Our parameter, $$\alpha$$ should allow for us to recover our original integral AND we must have an initial value easily obtainable so that we can solve our first order differential equation, $$I'$$. 

Going to where we left off above:

$$\frac{dI(x, \alpha)}{d\alpha} = (\frac{1}{\alpha^2 + 1})[\frac{ln(2)}{2} + \alpha \frac{\pi}{4} - ln(1 + \alpha)]$$

$$\Leftrightarrow \int\frac{dI(x, \alpha)}{d\alpha} d\alpha = \int(\frac{1}{\alpha^2 + 1})[\frac{ln(2)}{2} + \alpha \frac{\pi}{4} - ln(1 + \alpha)] d\alpha$$

$$\Leftrightarrow I(x, \alpha) = \int(\frac{1}{\alpha^2 + 1})[\frac{ln(2)}{2} + \alpha \frac{\pi}{4} - ln(1 + \alpha)] d\alpha$$

$$\Leftrightarrow I(x, \alpha) = \frac{ln(2)}{2}\text{arctan}(\alpha) + \frac{\pi}{8}ln(1+ \alpha^2) - \int_0^\alpha \frac{ln(1 + \alpha^*)}{\alpha^{*2} + 1} d\alpha^{*} +C$$

Here, we make an important observation. In our original function, 

$$I(x,0) = \int_0^1 \frac{\ln(0 * x+1)}{x^2+1}\,dx  = \int_0^1 \frac{\ln(1)}{x^2+1}\,dx = 0$$

Also, the last integral which I've denoted * is simply our original function with $$\alpha = 1$$!! (The alpha in * is a dummy variable)

Clearly, 

$$* = \int_0^0 \frac{ln(1 + \alpha^*)}{\alpha^{*2} + 1} d\alpha^{*} = 0$$

So now we have all our ingredients to solve this problem. Using the initial value of $$I(x, 0) = 0$$, we get that our integration constant $$C$$ is 0!

Using heuristic 2 that we've identified earlier in this section, we are interested in the value of $$I(x, 1)$$, which equals:

$$ I(x, \alpha) = \frac{ln(2)}{2}\text{arctan}(\alpha) + \frac{\pi}{8}ln(1+ \alpha^2) - \int_0^\alpha \frac{ln(1 + \alpha^*)}{\alpha^{*2} + 1} d\alpha^{*} +C$$

$$\Leftrightarrow I(x, 1) = \frac{ln(2)}{2}\text{arctan}(1) + \frac{\pi}{8}ln(2) - \int_0^1 \frac{ln(1 + \alpha^*)}{\alpha^{*2} + 1} d\alpha^{*} + 0$$

$$\Leftrightarrow I(x, 1) = \frac{ln(2)}{2}\text{arctan}(1) + \frac{\pi}{8}ln(2) - I(x, 1)$$

$$\Leftrightarrow 2I(x, 1) = \frac{ln(2)}{2}\text{arctan}(1) + \frac{\pi}{8}ln(2) $$

$$\Leftrightarrow I(x, 1) = ln(2)\frac{\pi}{8} $$

Phew, that was most calculus I've done in a year

### Overview
Feynman's trick can be seen as solving not just one integral but a family of integrals, and can be seen as the following steps:

1. Identify a parameter to remove nasty functions (and one that lets you get initial values)
2. Integrate normally
3. Change it into a differential equation problem
4. Get initial values from step 1
5. Solve DE
6. Plug in the value that makes the general solution into the specific solution
7. Done!!

### References: 
1. [Putnam 2005](https://kskedlaya.org/putnam-archive/2005.pdf)
2. [Practice problems / further reading (UCONN)](https://kconrad.math.uconn.edu/blurbs/analysis/diffunderint.pdf)

<div class="author-box">Chris Su - Carnegie Mellon University - AI &amp; Computer Science</div>
