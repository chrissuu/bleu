---
layout: post
title: pre training as bootstrapping
subtitle: llm post-training
tags: [ai]
type: nr
---
Super quick post, but I wanted to talk about this semi-interesting phenomenon about training steps for LLMs.

Modern LLMs are (mostly) trained in two stages: pre-training and post-training.

Pre-training combines large datasets of basically the entire internet with clever architecture designs made around 
transformers to do next token prediction. During this step, the model can be thought of as "advanced auto complete".
In general, the model during this step has learned a lot of the syntactical rules of the language(s) that it
is trying to next token predict. 

Post-training is composed of many different fine-tuning steps:

1. supervised fine-tuning where you try to teach the model how to do basic instruction following
2. RLHF, where you learn human preferences for responses (i.e., when ChatGPT produces two parallel responses and asks you to rate them). 
This step is slightly dangerous since it increases sycophancy in LLMs (where the model is more likely to agree with what you say. Intuitively,
you might see why this is the case -- humans are more likely to rate outputs which agree than disagree with them.)
3. RLVR, which is RL applied to problems where reward is verifiable (such as in the case of math or coding problems)

Lastly, there's some inference tricks you can do to make the model more efficient or increase output quality:

1. KV Caching
2. Quantization (there's also quantization aware **training**)
3. Temperature adjustments
4. Sampling techniques
5. Context Optimization / Management
6. Chain of thought prompting

*Etc.*

But maybe the most interesting part here is the post-training step:

An important question to ask is why we couldn't just skip the pre-training step and go straight to post-training.

Maybe one answer is that the enormous amount of data on the internet creates a good prior for fine tuning.
Without this step, the weights of the LLM would be randomly initialized, and convergence to behaviors that you want (such
as good reasoning) may be computationally infeasible.

This has implications for two interesting points to consider:

1. If your goal is for the model to exhibit some behavior, then pre-training + post-training can be seen a form of transfer learning, 
where weights of the initial task (next token prediction) is "transferred" to the context of some "behavior" (reasoning, instruction
following, RAG, etc). In other words, pre-training is a way to bootstrap the model's weights towards the direction of weights which are 
closer to your desired behavior's weights.

2. Much of the "behavior" that we would like the model to exhibit is earned through post-training. Since pre-training $$\rightarrow$$ post-training is faster than random-initialization $$\rightarrow$$ post-training, the post-training step is important for
the model to learn the syntax of the language as well as having a baseline world model of how things interact. Perhaps what isn't as clear 
is how much each component is necessary in exhibiting some behavior, and could be an interesting ablation for training efficiency. For instance, if your goal is to have a good reasoning model, you could train a small model until its outputs are coherent, and then increase the
model's expressiveness by adding further layers (but with identity weights) and then post-train your model. Pre-training would thus be "make your model coherent" and post-training would be "make my model exhibit xyz behavior", rather than "make my model coherent but also have some prior for world modeling" and "make my model exhibit xyz behavior".