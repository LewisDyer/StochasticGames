# Week 8 Minutes - 18/11/20

The questions for this week were discussed:

* For the issue with the model not always terminating, this occurs because, for turn-based stochastic games, graph-based methods are employed for reachability conditions, rather than methods based on numerical convergence for concurrent stochastic games. As a result, the probability of the game terminating will converge to 1 but not reach 1, so the property would be false - this can be easily modified by using Pmax instead.
* For receiving less verbose output using PRISM from the command line, grep was recommended as the most sensible tool, although Gethin also suggested exporting the results to a file and processing those as a possible alternative. However I agreed that grep would be a sensible, relatively easy alternative to implement.
* Gethin recommended that I should commit experiment data to version control - this prevents issues with models potentially being overwritten if changes to the preprocessor/model generation occur.

The preprocessor was discussed, and Gethin remarks that it looks good and there is potential for it to be included in a future version of PRISM, however Gethin also suggested determining whether time was available at the end of the project to work on this, since this wouldn't be directly related to my project.

Finally the plan for next week was summarised. I should continue building an experiment automation environment, testing it on Ubuntu to ensure it functions across different operating systems, and start analysis of larger models if this is completed.