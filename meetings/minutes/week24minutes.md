# Week 24 Minutes - 30/03/21


First, several questions were discussed from the status report:

* Since the representative beliefs form a convex hull, every belief is a linear combination of the representative beliefs. Hence, value iteration only iterates the values on the grid points, and other points are interpolated from there.
* The abstraction of belief MDPs producing an over-approximation is a rather involved proof - in general, proving statements about unbounded POMDPs is much harder than for discounted POMDPs (with some sort of "decay" through each step of a POMDP, since these sequences converge to 0).
* The lower-bound on an POMDP has little to do with the strategy from value iteration having finite memory - rather, just because it's some strategy on the POMDP.
* I should add some basic README files saying where different models are and how to run them, but the vast majority of the focus is, and should be, on the dissertation itself.

Then, some questions were discussed about the recent Overleaf comments:

* A clarification was made that the conditional probability graphs are really conditional on attaining a particular score, not on a given board being covered.
* Symmetry in subgames was clarified, in that some subgames can be "reframed" by swapping player 1 and player 2, allowing for further reductions in computation.
* The current page count is concerning, and I should consider reducing some background sections, moving some parts to appendices, or reducing figure size later on, but for now I should focus on writing things down, then cut content as needed.

Finally, the plan for next week was agreed. I would add my progress so far onto Overleaf on Thursday, and on Friday morning we would decided whether or not a meeting would be useful for Friday. After that, next week's meetings would be arranged, most likely including a meeting on Thursday for any last questions/feedback before the final submission.