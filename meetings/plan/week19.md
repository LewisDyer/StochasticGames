# Week 19 Status Report - 23/02/21

This week, and last week, I have completed a (rather rough) first draft of most of the initial background section. Most of the preprocessing is complete, so I'm now ready to start setting up a development environment to process model checking results.

# Questions/Notes

* I'm not sure where to write about the PRISM-games specific section of the background - I think that putting it in the first case study's background would be best, since the initial background is already quite long.
* Similarly I'm not sure what sort of depth I should go into about solving systems of linear equations - at the moment I've just compared direct and iterative methods in general, and I think describing specific methods in detail won't add much.
* Also, I'm unsure about what I should be mentioning about PRISM at this stage. I've focused on how models and properties are defined in PRISM, with a few small snippets from case studies, opting to mention some of the technical details in the general model checking section instead.


* The cluster results took quite a while to obtain, but the results themselves are sensible and they're in line with what I expect at the moment. The size limitations are potentially concerning, but I think that around 50 spaces should give useful results given the number of faces per dice has been reduced. But I should try and avoid building models on 100 spaces unless I can show a clear benefit of it, given the substantial increase in computation time.
* In the same vein, I'm planning to scope the third game down to only two players, since the substantial increase in model size with many players is quite risky.


# Plan for next week

* Work on a development environment for the third game (Aim to use statistical model checking to get very rough results, but also take the existing cluster logs and obtain data from them).
* Finish off the last sections of the initial background section (model checking reward-based properties along with related work - should be able to tweak my RMT coursework a bit and use that).
* If I get time (I probably won't), make a start on the Shut the Box case study (I'm expecting to be able to write that section relatively quickly).

