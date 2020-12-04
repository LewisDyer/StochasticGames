# Week 11 Status Report - 09/12/20

This week, I have collected more data on ShutTheBox, in particular varying the number of dice in the 12-board variant to investigate the triangular number phenomenon (using 1, 2, 3, 4 and 6 dice). I have also started investigating POMDPs, starting background reading, downloading the development version of PRISM with support for POMDPs and investigating several of the built-in examples (especially McCallum's maze problem).

# Questions/Comments

* Given that this development version of PRISM doesn't support strategy generation, is there any way I can still get the optimal strategy for a particular property? (e.g the sequence of moves taken for McCallum's maze problem)

* I noticed there's also no support for simulating paths manually - do you have any particular tips for debugging POMDPs? I found with ShutTheBox that simulations were really helpful, and I'm concerned about showing my game acts as expected without a few simulations. Converting them to MDPs is trivial and could be partially effective, albeit in some models having hidden information has far larger implications than others.