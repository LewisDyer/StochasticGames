# Week 3 Status Report - 14/10/2020

This week, I have completed examples 1 and 2 from the PRISM-games tutorials, along with reviewing the user-centric networks example to gain more experience with SMGs in particular. I've also read the paper William suggested containing case studies on model checking with game design. The source code provided with this paper has been especially helpful, and I've also spent some time reviewing these models in order to understand how they're constructed.


## Questions

I've included .dot files for the model and for the optimal strategy for player 1 winning before player 2 wins with one round of rock-paper-scissors (I've attached images of these files on Teams), and I have a few questions regarding these:

* I think at the moment I'm struggling to understand what strategy generation actually does. My current understanding is that the value of the property tells us what our optimal value is (in this case utility 0 since in the long run we win as much as we lose), and the strategy we get out gives the choices we should make (potentially stochastically) such that this optimal value is obtained, regardless of the choices of other players.

* Is there a way I can define my own strategies and see how they perform under various properties, even if my own strategy isn't optimal?

* I tried creating and exporting strategies on the GUI, but this seems buggy - I've tried it a few times and it doesn't seem to save a strategy in memory (and I can't view it in the simulator or anything like that). The closest I can get is exporting the strategy as a .dot file via the command line (I've also tried exporting as an .adv file on the command line and this doesn't seem to work). I noticed [this post](https://groups.google.com/g/prismmodelchecker/c/Y7sK015zeZQ/m/R4RmtoCFFwAJ) on a similar topic a few years back, so I presume this is some sort of bug.

* I'm still a little unclear on the difference between turn-based and concurrent games - as far as I understand, the main difference is that in concurrent games players all make their decisions simultaneously (i.e player 2 can't base their decision on player 1's choice). So a game doesn't have to be considered "real time" to be a concurrent game.

## Initial plan for next week

* Given the previous issues I've had with previewing large .dot files, I'm concerned that relying on this to display strategies for Shut the Box will be infeasible.

* I'd like to get started modelling Shut the Box. My current thinking is that starting with a relatively small number of boards (say 4 or 5?), with a uniform probability distribution, will be a good starting point - that way, I can focus on building up different components from scratch, yet the model is small enough that I can verify some basic properties by hand. Then, I should spend some time working on pre-processing PRISM models, so that I can scale this up to more boards relatively easily.