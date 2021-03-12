# 26 Point 2 Notes

Aim: I currently have results obtained via statistical model checking - aim is to use these to find good results to consider via probabilistic model checking.

Curently:

* Against the 4 strategy, hybrid and 3 perform very, very similarly. Need to investigate this difference - probably too close for statistical model checking to consider!
* Winrate should be 50% on the same strategy, with potential exceptions for numerical convergence via value iteration
* Nondeterminism really doesn't work with SMC, need probabilistic techniques for this