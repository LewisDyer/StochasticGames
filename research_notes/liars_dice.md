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

### Rules of Liar's Dice

In Liar's Dice, each player starts with a given number of 6-sided dice (let's say 4 for now). The game takes place over a series of rounds. At the beginning of each round, each player rolls their dice, keeping the faces on each die secret. The first player then makes a bid, saying how many of a particular value is available on the table (e.g "4 fives"). Players then go in order, and have one of two options. They can either make a higher bid (by increasing the quantity by 1, or by increasing the face value by 1), or by challenging the previous bid. If a challenge is made, all dice are revealed. If the bid was correct, the challenger loses a die. If the bid was incorrect, the bidder loses a die. Play then repeats, with the losing player starting the next round, and the last player to still have dice left is the winner.

### Simplifications

To start with, I'll consider the case with 2 players, and 3 die. POMDPs inherently only really allow one "non-fixed" player, so my thinking is I should focus on the 2 player case and define strategies for that player. Also some variants use 1 as wild, but I don't intend to include that due to complexity.

### Things to consider

* How subsceptible is the game to the "snowball effect"? In other words, what's the probability of winning if you start from behind? (Could model this by changing the initial state so a player starts with one less die). Does this act as an effective "handicap"? Are some strategies better at dealing with this handicap? (Intuition: safe strategies won't do well because they don't give the peaks that you need to get out of such a hole. You need something risky, even if it's unlikely).
* How do different strategies compare against each other? Potential for non-transitive strategies...
* Does adding more dice make for a more interesting game, or just a longer game?
* Does it matter who goes first? Starting bidding early seems to be very powerful (you can essentially dictate the flow of that round).

### Different Strategies

One way to think about strategies is that there's different mechanics in the game (I could separate it into the initial bid, subsequent bid, and decision to challenge), and each of these mechanics naturally splits into different strategies. So what I could do is define a small number of options per strategy (say 2 or 3), then take each combination of these to produce bigger strategies.

#### Initial Bid

1. `SAFE-LOW`: Make the absolute lowest bid you can, based on what you can see.
2. `SAFE-HIGH`: Make the highest bid you can, based on what you can see.
3. `RISKY`: Use the expected value of your opponent's dice to make a bid that potentially requires information from them.

#### Subsequent Bid

1. `ALL-SAFE`: Always choose the bid type that gives you as many turns as possible. Never bluff, unless it's required.
2. `LEAD-BLUFF`: If you can bluff, you should do so, but only if you have more dice than the opponent.
3. `ALL-BLUFF`: If there's an option to bluff, _always_ take it, unless it leads to an obviously impossible situation (e.g going over the number of visible dice).

#### Decision to challenge

1. `FULL-TRUST`: Never challenge unless it's an impossible bid.
2. `INFERENCE`: Calculate the probability of a bid being false, and challenge if it's below a certain value.
3. `FULL-DISTRUST`: Never trust your opponent unless you can see the results in your own hand.

Alternative idea: Increase the probability of calling for a challenge with each bid (except in the case where the bid is known to be valid). More trusting strategies have a smaller increase in this probability. Much, much simpler to implement!

### Another approach to strategies

This could get complicated, so instead I could define a few "archetypes" of players like so:

* `SAFE`: This player always tries to avoid bluffing if given the opportunity. This player makes the smallest valid bid they can, so they can avoid bluffing for as long as possible. This player challenges infrequently, only when a bid is very risky (e.g the probability of it being false is very high)
* `RISKY`: This player is very willing to bluff. This player makes large bids, frequently bluffing to try and catch their opponent out. This player will challenge bids often, trying to exploit their opponent's trust.
* `HYBRID`: This player will play `SAFE` if they're tied, or have a lead, but will switch to playing `RISKY` if they're behind.