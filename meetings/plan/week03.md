# Week 3 Status Report - 14/10/2020

This week, I have completed parts 5 and most of part 6 of the PRISM tutorials, studying the EGL contract signing protocol and the dining philosophers problem. In particular, I found these tutorials especially helpful to gain more practice in expressing algorithms using the PRISM modelling language, and various methods to debug these models. I also read some of the slides for the lecture course on [Probabilistic Model Checking](http://www.prismmodelchecker.org/lectures/pmc/), specifically lectures 1-7 and 10-12. In addition, I have developed a proposal for a potential game to analyse, based on a traditional parlor game called "Shut the Box", which I'll discuss further in this week's meeting.


## Questions

* PRISM includes several different model checking engines (Hybrid, Sparse, MTBDD, Explicit) - how would I figure out which engine is best for a particular model? What happens if I use a "bad" choice - would this lead to potentially flawed analysis, or is it mainly a performance consideration? The PMC lecture notes seem helpful with some of these decisions in theory, but I'm unsure how those decisions come up in practice.

* What makes a game "interesting" to analyse? My current thinking is that the best strategies shouldn't be too simple (or else they're discovered really quickly as in tic-tac-toe - whereas chess and go technically have dominant strategies, but they're so complex that humans can't possibly learn them), and they should be powerful enough to make a difference (i.e if using an optimum strategy only leads to a 1% increase in winrate over a random strategy, I probably wouldn't make the effort to learn that strategy).

* I'm not quite sure I understand MDPs - my current understanding is that, once a strategy(/adversary/policy) is chosen, this causes the MDP to "transform" into a DTMC, since the strategy resolves nondeterministic choice. And in particular Markov adversaries (where the strategy always makes the same choice in a given state) are useful because they map MDPs to a finite state DTMC.

* I spent a few minutes poking around the case studies, and noticed some absolutely massive model files, such as [this one](https://www.prismmodelchecker.org/files/clima11/models/STPG_offline.nm.php) arranging 5 agents in 120 different orders. Typing this out by hand seems like it's bound to cause issues - could there be a more efficient way to generate these models (for example, a program in some other language, say Python, that generates each of these permutations and outputs them to a model file)? 

## Initial plan for next week

* I haven't completed the section in Part 6 of the PRISM tutorial on [courteous philosophers](https://www.prismmodelchecker.org/tutorial/phil.php), but I think it would be more useful to start using PRISM-games soon - the last two tutorials took longer than expected, so I don't think I'll have time to complete this extension this week.

* I should start using PRISM-games, in particular understanding the differences between turn-based and concurrent games. The provided [examples](https://www.prismmodelchecker.org/games/examples.php) look fairly straightforward, but these are both concurrent, so I should also look over the [case studies](https://www.prismmodelchecker.org/games/casestudies.php) and pick one of the SMG-based examples to work through as well, to build an understanding of these types of games and how they differ.

* I have a few more PMC lectures to look through (most likely lectures 13-14).