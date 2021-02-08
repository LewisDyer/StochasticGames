# Week 17 status report - 09/02/21

This week, I have focused on preprocessing work for 26.2 - the bulk of preprocessing is complete, I just need to finish some relatively easy work and I'll be able to generate models. In particular I've implemented the suggested refactoring to calculate dice rolls in one step. I've also tidied up some work in the background section, changing the TSG definition to a DTMC (it's simpler and makes progression to future model types easier to motivate). I haven't added much dissertation content this week, but I've spent some time organising my thoughts to speed up future writing.

# Questions/Notes

* I'm considering removing the proposed work about weighted dice from the project. In particular, dissertation writing is taking more time than I expected, and the weighted dice work seems potentially risky, since I don't feel that the work can be well presented unless I implement it for all 3 games. This should help me avoid the situation where I start a large chunk of work, find myself unable to finish it, and get nothing out of the work in the end dissertation-wise.

* So far when I'm choosing references to cite, I'm finding that I end up citing a few sources repeatedly (in particular the tutorial paper on stochastic model checking). Is this something I should be concerned about, compared to citing a wider variety of sources?

* I've written a section on probabilistic model checking, but it mainly focuses on the motivations for the technique (e.g compared to simulation-based techniques) rather than the technical details - I'm not sure whether this would fit better in the introduction or the background section. My current thinking is that the introduction is focused on why a particular technique's being used, whereas the background section is focused on describing the techniques more technically. In other words, subject experts should be able to skip the background section and still be able to understand the dissertation.


# Plan for next week

Unfortunately I don't get much time off due to the reading week (since I only take one taught computing science course and maths doesn't do a reading week), so I don't anticipate to spend much longer on the project than I currently am. That being said, over the reading week I'm hoping to spend a good chunk of time working on finishing off preprocessing, and hopefully start processing results and determinining whether the proposed refactoring reduces the state space significantly. In addition, I would like to complete more of my initial background section, namely a description of probabilistic model checking techniques and how they're implemented in PRISM.