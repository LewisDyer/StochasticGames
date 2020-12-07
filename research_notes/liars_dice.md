# Liar's Dice - initial discussion

The aim of this document is to start modelling Liar's Dice. To do this, I should aim to describe the game in more detail, and understand how to start modelling the game from this information. By the time this initial document is completed, I should have enough information to begin modelling a simple version of Liar's Dice.

### Partially observable

A key difference between Shut The Box and Liar's Dice is that Liar's Dice contains hidden information. In other words, we don't know the full state of the game at any one time. We only know _pieces_ of information about the game, and use this to construct _beliefs_ about the full state of the game. So it will be especially important to quantify what we know and what we don't know.

### Understanding POMDPs

The key new structure we use to tackle this game is a Partially Observable Markov Decision Process (or POMDP) for short. This is an extension to the MDPs I've already looked into, with a few extra bits:

* A _finite_ set of observations, denoted by O.
* A labelling of states with observations.

Note that, if the MDP has a finite number of states, then there are certainly a finite number of observations, but there can still be a finite number of observations even if the number of states is infinite (e.g if the states are all of the form (x, y), where x is in {0, 1} and y is an integer, and the observation of (x, y) is x, this gives 2 observations for a countably infinite number of states).

We also require that any two states with the same observations have the same available actions - since actions aren't hidden, this is necessary for two states to be observationally equivalent.

Observation-based strategies are also strategies in the related MDP, with the added constraint that if two different paths have the same observations and the same actions taken, the strategies along them are the same. In other words, we can't distinguish between observationally equivalent paths.

When defining properties for a POMDP, we've got to be careful to use targets based on _observations_, not states. The reason for this is that, if it's based on states, we might not know whether we've reached the target or not. In most cases, we can simply have a specific observable variable for determining whether we're at the target state.

The key, key idea in POMDPs is the concept of _belief_, which represents our current understanding of which state we're currently at. And our idea is that we update our beliefs over time, based on what happens when we perform various actions. This belief space actually forms an MDP, which each belief being a probability distribution across the states of M. (Of course, only those states which fit within our current observations have non-zero probability).

In practice, verifying properties of POMDPs is undecidable - we can use grid-based techniques to get upper and lower bounds, and so in practice it's better to get a numerical value directly than to use a bolean property based on a bound (e.g in case the upper and lower bounds are on either side of the condition).

The general structure for computing optimal probabilities/expected reward values:

* Modify the POMDP, simplifying the problem to a probabilistic reachability/expected cumulative reachability reward.
* Get approx simulation to belief MDP to get over-approximation.
* Find strategy for our modified POMDP, getting an under-approximation.
* If we don't get tight enough bounds, increase grid resolution and try again

NOTE: Increasing grid resolution doesn't always give us tighter bounds! But it does give an _asymptotic guarantee_ of convergence.

In PRISM-POMDPs, use the `observables` keyword to indicate variables that can be used in observations.
