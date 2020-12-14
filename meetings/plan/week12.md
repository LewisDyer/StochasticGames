# Week 12 Status Report - 14/12/20



# Questions/Comments

* The main challenge I've faced so far is reducing the state space of the model. At the moment, I can verify properties where each player has 2 dice relatively easily (with a low grid resolution), but the case with 3 dice each seems too large to handle. My current plan is to stick with a maximum of 2 dice per player (not ideal, but it should suffice for illustration), but the design of my system should allow for larger dice counts without much modification if the models are refined.
* I've noticed that verifying certain properties for MDPs is much easier than verifying the same properties for their corresponding POMDPs (likely because model checking for POMDPs involved constructing a much larger MDP). While some properties require checking the POMDP (e.g some problems become trivial if the exact state is known), can some properties be checked by just considering the corresponding MDP of the POMDP (e.g whether a model eventually terminates)?


# Plan for this week

* Finish status report (it's almost finished, just need to add a few more points when I get a bit of time)
* Over the holidays: Take a break(!), but also pin down an idea for a 3rd game so I can get started on this ASAP in January