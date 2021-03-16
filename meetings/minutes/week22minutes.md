# Week 22 Minutes - 16/03/21

First, discussion ensued on various comments made on the most recent dissertation work on Overleaf:

* Discussion on PRISM-games should primarily occur in the third case study, since adversary generation for MDPs is technically supported in PRISM, although in a more unwieldy format.
* The partial function based definition of a probability transition function is easier to handle than the ordered-pair based definition, since each possible action in a state has one associated probability distribution, so I should use this definition instead of my current one.
* Some issues with convergence in value iteration was discussed, mainly either "plateaus" of small but consistent change, or initially small values. Gethin mentioned recent work to solve this problem, and recommended I cite this work but don't go into too much depth on it

Then, the questions in the status report were briefly discussed:

* Generating maximum strategies is slightly more difficult, since 2 states linking to each other with 2 actions with probability 1, along with linking to the goal, may get stuck in cycles rather than going immediately to the goal - this requires a small modification to value iteration, though it shouldn't take much extra time to write.
* I should try to avoid using too many snippets, since the analysis is far more important than the specific implementation. However mentioning some code snippets can be illustrative, and they can be useful in the evaluation section as justification for the preprocessor.

Finally, I stated that I would plan to write up Shut the Box results, maybe start Liar's Dice background, and add adversary generation to the cluster properties.




