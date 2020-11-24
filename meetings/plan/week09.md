# Week 8 Status Report - 25/11/20

This week, I have continued to develop the experiment automation environment - namely, I've included a few more visualisations (for the probability of each score under each strategy, cumulative probability,
and the difference in cumulative property between each pair of strategies). I still have some polish to work on, but the skeleton of the environment is mostly completed.

I have also started analysis of some larger variants of Shut the Box - specifically, 12 boards using 2d6 (two six-sided die), and 9 boards using 2d6. This has introduced some new challenges (mainly to do with numerical convergence and performance), but it also includes some interesting results that correspond fairly naturally with previous work on Shut the Box for 6 boards. I don't think it's a good idea to look into these too closely until the environment is more fleshed out (right now results override each other so it's cumbersome to compare models), but inital results are encouraging.

# Questions/Comments

* I've noticed some unusual behavior regarding numerical convergence of some properties - in particular the probability of termination is slightly over 1, but more concerningly the conditional probability of a score given a particular board is covered is sometimes 0, or even NaN (my solution involves dividing potentially very small probabilities which may cause the issue). I've got two ideas for solutions - either reduce the termination epsilon, or capture the data for the numerator and denominator separately and perform the division later when creating visualisations. My current thinking is the latter is better (in particular I already compute the denominators of these conditional probablities, so this should improve performance), but I'm not sure about this.
* I've been considering separating the two stages of experiments - model checking and visualisation - into two separate notebooks. My thinking is that ideally model checking should only be performed once for a particular model, but once that data is obtained many visualisations could be developed from that data, so separating out the logic seems sensible.

# Plan for next week

* Continue polishing the development environment - in particular, I'd like to parameterise the filenames for output data (so I can store multiple versions of a model at once), and organise the directory structure a bit more.
* Take a closer look at strategy generation - I haven't really considered this for Shut the Box yet. In particular comparing with the high-board strategy to maximise the probability of a perfect score should be quite interesting (since the high-board strategy is very close to optimal, but not exact).
* If I get time, start collecting data and writing some initial research notes, similarly to my initial work with the manual Shut the Box model.

* Looking ahead to the December crunch period - I'm spending slightly more time on experiment automation than I originally anticipated in my month-to-month plan, but I'm not concerned about this since this is important work which should save time later. That being said, I think it would be useful to start thinking more about Liar's Dice next week, so that I can make as much progress as possible in modelling the game in the crunch period.



