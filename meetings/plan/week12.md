# Week 12 Status Report - 14/12/20

This week, I have completed preprocessing functions for Liar's Dice, and started developing the automation environment so that I can analyse entire games by considering individual rounds. During preprocessing, I have experimented with various methods for reducing the state space for Liar's Dice, however most of these methods have been unsuccessful.

Looking ahead, I have an idea for a third game to discuss during the meeting - I don't think I could start this game before semester 2, but it would be useful to get the third game finalised so I can get started ASAP in January. (This game feels somewhere in between Shut the Box and Liar's Dice complexity-wise, but with similar ideas about risk vs reward. Liar's Dice ended up being somewhat more complex than originally intended, and this game should be simpler, so that I have enough time for the write up and for my final piece of analysis using weighted dice).

# Questions/Comments

* The main challenge I've faced so far is reducing the state space of the model. At the moment, I can verify properties where each player has 2 dice relatively easily (with a low grid resolution), but the case with 3 dice each seems too large to handle. My current plan is to stick with a maximum of 2 dice per player (not ideal, but it should suffice for illustration), but the design of my system should allow for larger dice counts without much modification if the models are refined later on.
* I've noticed that verifying certain properties for MDPs is much easier than verifying the same properties for their corresponding POMDPs (likely because model checking for POMDPs involved constructing a much larger MDP). While some properties require checking the POMDP (e.g some problems become trivial if the exact state is known), can some properties be checked by just considering the corresponding MDP of the POMDP (e.g whether a model eventually terminates)?


# Plan for this week

* Finish and submit the status report (this shouldn't take long at all, I just need to find time for it)
* Finish off as much of the automation environment as I can - for now I don't want to polish much, just get enough so that I can look back on it later and not feel completely lost.