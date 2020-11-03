# Week 5 Status Report - 04/11/20

This week, I have focused on developing a preprocessing system for generating PRISM models automatically. The core functionality of this system is mostly complete (The template system is functioning properly and defining values for parameters in `.csv` files has now been implemented, I mainly need to add a little extra code to properly handle whitespace). I have also started developing specific functionality for Shut the Box, including a function to generate a probability distribution for rolling multiple dice. In addition, I have created an initial month by month plan for the remainder of the project.

Moreover, I've reviewed the suggestions that were made to refine my original Shut the Box model and have concluded that, the idea of moving boards to separate modules is a good one, along with adding specific action labels for each possible covering, but I should keep the logic for deciding which set of boards to cover in the player module. A key reason for this is that changes in strategy are based on changes to board covering choices, and I think that restricting the strategy changes to just the player module (rather than spreading them between the player module and each board module) will make for a clearer comparison between different strategies.

# Questions/Comments

* While doing some background reading, I noticed that some papers used probabilistic model checking while others used statistical model checking. Statistical model checking seems especially useful if I end up analysing an especially complex game with many states, but I'm slightly concerned about spending time researching a technique I won't end up utilising in my project. Would you recommend doing some further background reading on statistical model checking?
* I read the paper from Kavanagh et al. on Chained Strategy Generation. I don't think I'll end up using CSG in any of my models (due to time constraints and likely being unsuitable for my current games), but I found the idea of material choice in games to be quite interesting - in essence, providing two "layers" of strategy, both before and during a game. This could be an interesting mechanic to consider when choosing my 3rd game.


# Plan for next week

* Continue building preprocessing system for Shut the Box (I don't have much left to do, but that includes the function to generate board coverings which is probably the hardest function I need to create so far). By the end of next week, I'm aiming to have enough preprocessing done to create fully functional PRISM models.
* If I manage to complete this, I should start working on creating an enviroment for automating model checking and visualisation.
* Continue investigating possible ideas for the 3rd game I should model - I'd like to figure this out by next week, or potentially the week after. This isn't a high priority for now, but I should get this decided and discussed before December so that I can hopefully start modelling the game as part of the December project period.