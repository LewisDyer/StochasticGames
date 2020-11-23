# Week 8 Status Report - 25/11/20

This week, I have continued to develop the experiment automation environment - namely, I've included a few more visualisations (for the probability of each score under each strategy, cumulative probability,
and the difference in cumulative property between each pair of strategies). I still have some polish to work on, but the skeletion of the environment is mostly completed.

I have also started analysis of a larger variant of Shut the Box - specifically, 12 boards using 2d6 (two six-sided die), and 9 boards using 2d6. This has introduced some new challenges (mainly to do with numerical convergence and performance), but it also includes some interesting results that correspond fairly naturally with previous work on Shut the Box for 6 boards. I don't think it's a good idea to look into these too closely until the 

# Questions/Comments

* I've noticed some unusual behavior regarding numerical convergence of some properties - in particular the probability of termination is slightly over 1, but more concerningly the conditional probability of a score given a particular board is covered is sometimes 0, or even NaN (my solution involves dividing potentially very small probabilities which may cause the issue). I've got two ideas for solutions - either reduce the termination epsilon, or capture the data for the numerator and denominator separately and perform the division separately. My current thinking is the latter is better (in particular we already compute the denominators of these conditional probablities, so this should improve performance), but I'm not sure about this.
* I've been considering separating the two stages of experiments - model checking and visualisation - into two separate notebooks. My thinking is that ideally model checking should only be performed once for a particular model, but once that data is obtained many visualisations could be developed from that data, so separating out the logic seems sensible.

# Plan for next week

* Continue polishing the development environment - in particular, I'd like to parameterise the filenames for output data (so I can store multiple versions of a model at once), tidy up some of the grepped output, and in general keep things reasonably organised.
* Fix bug with covers not generating when no. of boards is less than max value of dice (need a filter condition for this...)
* Take a closer look at strategy generation - I haven't really considered this for Shut the Box yet. I don't want to go full on with this (the strategy files become _massive_), but comparing with the high-board strategy will be especially important



