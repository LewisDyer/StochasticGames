# Week 3 Status Report - 14/10/2020

This week, I have completed examples 1 and 2 from the PRISM-games tutorials, along with reviewing the user-centric networks example to gain more experience with SMGs in particular. I've also read the paper William suggested containing case studies on model checking with game design. The source code provided with this paper has been especially helpful, and I've also spent some time reviewing these models in order to understand how they're constructed.


## Questions

* I'm struggling to understand what strategy generation actually does. My current understanding is that the value of the property tells us what our optimal value is, and the strategy we get out gives the choices we should make (potentially stochastically) such that this optimal value is obtained, regardless of the choices of other players. (Using an analogy, the value of the property is like the maximum value of a function, and the strategy is the inputs that give us that maximum value)

* I tried creating and exporting strategies on the GUI, but this seems buggy - I've tried it a few times and it doesn't seem to save a strategy in memory (and I can't view it in the simulator or anything like that). The closest I can get is exporting the strategy as a .dot file via the command line (I've also tried exporting as an .adv file on the command line and this doesn't seem to work). I noticed [this post](https://groups.google.com/g/prismmodelchecker/c/Y7sK015zeZQ/m/R4RmtoCFFwAJ) on a similar topic a few years back, so I presume this is some sort of bug.

* Is there a way I can define my own strategies and see how they perform under various properties, even if my own strategy isn't optimal?

* I'm still a little unclear on the difference between turn-based and concurrent games - as far as I understand, the main difference is that in concurrent games players all make their decisions simultaneously (i.e player 2 can't base their decision on player 1's choice). So a game doesn't have to be considered "real time" to be a concurrent game.

* When we specify properties for a game, would I be right in saying that the coalition of players in that strategy represents the set of players whose choices we can directly control to try and optimise that particular property?

## Initial plan for next week

* I'd like to get started modelling Shut the Box. My current thinking is that starting with a relatively small number of boards (say 5?), with a uniform probability distribution (say values from 2-5) will be a good starting point - that way, I can focus on building up different components from scratch, yet the model is small enough that I can verify some basic properties by hand. If I finish this, then I should spend some time working on pre-processing PRISM models, so that I can scale this up to more boards relatively easily.

* I think I'm ready to start creating a more formal plan for the project (say, month by month). In particular, I'm noticing several "branches" of the project start to form that should be completed concurrently (so not just direct model development, but further research and background reading, developing miscellaneous tools like preprocessing scripts, potentially writing up parts of my dissertation and so on...), and having some sort of plan will be essential to make sure I don't neglect any of these branches.