# Week 15 Status Report - 26/01/21

This week, I have refactored my model for 26.2 to only count the quantity of each dice face rather than the specific value of each dice. This has substantially reduced the size of the model, allowing for feasible analysis of games with larger numbers of spaces. However actually performing analyis on much larger models is still slow, since the number of spaces leads to a large number of states, even though the behaviour of the game varies very little as the game progresses.

As a result, I have created a variant model with only one player playing at a time. This model is obviously more limited than the multiplayer model (since any strategies for choosing how many dice to roll cannot incorporate the opponent's position), but it can handle longer boards without any difficulties, allowing for useful analysis. So what I would ideally like to do is to use the singleplayer model to collect most data, then use a multiplayer model to show how concurrency adds power to the model. For instance, I could use the single player model to show an optimal strategy with no competition, then show how a more interactive strategy is better in the multiplayer model on a smaller example.

# Questions

* I'm not sure what to do about the case where the game ends in a tie (in my model, this is defined as the case where both players have reached the goal, end on the same space, and started on the same space last turn). Initial exploration suggests that this is very unlikely to happen (about 0.3% for a 30 space board and presumably shorter as the board becomes longer or the players have differing strategies) - as a result I think it might be better to assume the first player always wins ties, which may simplify analysis of the model (similar to how models of a coin flip exclude the edge case).
* Is there a way in PRISM to define a property giving the probability (or min/max probability with nondeterminism) of a reward being a particular value? In the single player model I'd like to define a probability distribution for the number of rounds required to complete the game with a particular strategy, but I'd like to do this without storing the number of rounds as a variable since it is unbounded (though in practice I would set a bound on the number of rounds anyway and clamp all values above this, so it's not a problem if I can't do this).
* I have a general question about citations - if I'm paraphrasing some background information from a source, and that source paraphrases information from another source, should I cite the source I'm paraphasing from, or the original work that information is from?

# Plan for next week

* I should have everything I need to start preprocessing now - this should be fairly straightforward for this model, since the strategies are reasonably simple and the structure of the model shouldn't change much either way. (Concurrency also makes adding extra players fairly trivial, even if the number that can be added is limited in practice).
* I can finally start cracking on with writing the background section - I think starting with the "general" background will work well to get a feel for how I should go about writing things, then moving onto the case studies. I'm hoping to get a large chunk of the general background done, though I doubt I'll have time to complete that chapter.