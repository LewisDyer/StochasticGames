# Week 10 Minutes - 09/12/20

First, the questions were discussed for this week:

* With regards to strategy generation, Gethin remarked that this feature exists, but graphs of strategies cannot be generated within PRISM. However Gethin mentioned that this tool existed elsewhere, along with some instructions to interpret the tool's output, and that he would send them to me if possible. In particular, Gethin emphasised that belief MDPs are comprised of two main parts: values of observable variables, and probability distributions of hidden variables.

* For debugging POMDPs, Gethin recommended initially creating the model as an MDP (with the full set of debugging/simulation features), then convert this back to a POMDP once finished, which is what I had tried so far. While the behaviour of the MDP and POMDP will differ, the general logic of the model will be very similar, if not identical.

* For designing opponents for Liar's Dice, Gethin recommended starting with very simple opponents, since POMDPs are already very complex, and starting simple means that some positive results can be obtained - while being unable to develop something is not a major setback, it is much easier to discuss positive results than negative results. I agreed with this logic, and added that my aim is to consider opponents that do not take beliefs into account, then generate strategies that are allowed to consider beliefs, to show the benefit of these more powerful strategies.

* Gethin agreed that treating each round as a separate model would be a good idea, especially to minimise the amount of redundant model checking and reduce the number of states in each model. I remarked that I already faced challenges with verifying results in a timely manner, so I would look further into state reduction for my model before commencing preprocessing.

* A brief discussion ensued about the 3rd game to study, and Gethin recommended that this game should be modelled using a CSG. This acts as a useful complement to the previous games using an MDP and a POMDP, and that optimal strategies for CSGs can involve probabilties, since all players make decisions simultaneously.

Finally, the plan for next week was discussed. I should aim to refine my existing model for Liar's Dice, in particular to reduce the state space further and consider some different opposing strategies. After this, I should add some preprocessing functions for the model (which should be slightly easier than Shut the Box, depending on various strategy choices). Then, I should create an experiment automation environment for Liar's Dice, building on existing work for Shut The Box. I remarked that this is quite an ambitious plan, but I believed I could complete it by the end of the semester.