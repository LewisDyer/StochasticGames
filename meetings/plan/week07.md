# Week 7 Status Report - 11/11/20

This week, I have focused on further developing the preprocessor for Shut the Box. I have implemented most of the remaining functions I need, in particular a complex function to generate PRISM code for all coverings, including a potential strategy for ordering coverings. I have also refined the core functionality of the preprocessor, in particular inheriting whitespace when a template tag is used (so for instance, if a template tag is indented one level, all of the outputted PRISM code will be indented as well).

At the moment, the preprocessor is powerful enough to produce a Shut the Box model that is *almost* complete - I'm having an issue with action labels across modules (it doesn't consider the covering actions to be controlled by the player), but I know how to resolve this (when defining the player, include the action labels for these coverings in the states they control) and I should be able to continue this next week. Once this is complete, I should be able to start experiment automation.

# Questions/Comments

* So far, I've found most of my preprocessor functions are quite messy. I can still understand them, and functionality-wise they're almost complete, but I'm concerned about maintainability in the future. I figured that since this was a research-focused project this code being messy isn't a big concern, but would you recommend taking the time to tidy things up some more/add some more documentation?
* Do PRISM action labels support any special characters? I've noticed that action labels can end up being ambiguous if the board numbers are just appended after one another (e.g "cover112" could mean covering 1 and 12, or 11 and 2), which could cause problems with large numbers of boards (where actions are improperly synchronised). I initially thought a special character would be useful to use (something like "cover_11_2"), but this doesn't seem to work in PRISM. Alternatively I could use a letter as a separator such as "X", but this is slightly messy.
* My preprocessing function to get the probability of all possible die values seems quite inefficient - it works for 12 boards and 2d6 with no problem, but when I get closer to 15-20 boards, or try using more smaller dice (say 3d4), the function doesn't return a value in a reasonable time. I think this is because I'm using recursion and there's a lot of values that are repeatedly calculated. I could refactor this function to improve efficiency (say by using memoization), but this probably isn't a priority and I can still perform interesting analysis without this optimisation.


# Plan for next week

* Finish off final feature of Shut the Box preprocessing (this should be fairly easy, I might have even completed it between writing this status report and this week's meeting)
* Fix a bug in Shut the Box preprocessing (the model exhibits unusual behavior when the possible die values are larger than the number of boards, e.g rolling 2d6 with 9 boards. I know how I can fix this, but it's a lower priority)
* Test out basic properties of generated Shut the Box models (mainly as an initial check that the models are compiling correctly, also as an extra step to check if the models are sensible)
* Get started with experiment automation (set up a Jupyter notebook, in essence replicate the process of my research notes in the notebook, and output the results to a data folder, including raw data and visualisations).