# Week 24 Status Report - 28/03/21

This week, I have written up most of the background for Liar's Dice, and made a start at writing up the results.

# Questions

* I don't understand what the "convex hull" is for beliefs in Dist(S) - My current understanding is, with |S| = n, that beliefs are points in R^n such that x_1 + ... + x_n = 1, and the convex hull is of this space.
* Grid-based techniques for POMDPs - why does an abstraction of the belief MDPs produce an over-approximation? My understanding is the grid points are a convex hull, so they lead to maximal values, hence interpolation gives larger values than the "true" values of inner points.
* I'm not sure how code is considered in the final assessment - at the moment everything's there but it's not especially tidy. Should I try and tidy it up?
* On the same topic, when I'm submitting the source code, should I just zip up the Github repo and send that over, or only send a few parts (e.g the src/data folders)? I've checked the filesize limit and it just about fits (if I need to I can delete some data files to make space).