# Week 22 Status Report - 16/03/21

* I've reviewed the results of the most recent cluster run, they look good and they align pretty closely with what I expected based on statistical model checking attempts. Also they ran far quicker than I was expecting to, so I can run a few more queries than I expected.
* Added new sections to the dissertation on adversary generation (Updated on Overleaf).

# Questions/Notes

* Section 4.3 of [this paper](http://www.prismmodelchecker.org/papers/sfm11.pdf) on MDPs suggests that generating an adversary for the max probability is harder than the min probability, but I'm not quite sure why this is the case.
* Is adversary generation for reward-based properties similar to reachability properties? My current thinking is it is, and I can probably use that to write relatively little about it/save some space, but I'm not sure.
* When I'm writing up the results for the various case studies, I'm not sure whether I should include snippets of the various PRISM models. I was thinking of using them as an example of the state explosion problem, but equally I think the evaluation would be a better place to discuss general issues like how I created the models (e.g creating a preprocesser to aid replicability). 

# Plan for next week

* Start writing up results for Shut the Box, finish off background as well. Hopefully the notes I've written down during the first case study can transfer over to the dissertation with relative ease. If I get time, make a start on the Liar's Dice background as well - I'm expecting this to be a fair bit shorter than for MDPs, but not quite as short as CSGs.
* Finish off the last pieces of development for the third game, mainly to include some examples of adversary generation. If I get time, make a start on adversary generation for Liar's Dice (with the prism-pomdps fix I was made aware of at the start of semester 1). 