# Week 14 Status Report - 14/01/21

This week, I have completed an initial manual model of 26.2, the third game in the project. The general game flow is complete, although the "water tokens" mechanics have not been included yet. Currently, the main challenge in the model is coping with size - the current model builds successfully with around 100 spaces and two players, but the full game uses 262 spaces by default.

In order to try and reduce the state space, I'd like to try directly calculating the number of each face rather than getting die values individually (e.g directly getting that there's 2 threes and a six rather than getting the value for die 1, die 2 and so on). For instance, with 6 six-sided dice, this reduces the number of possible rolls per player from 6^6 (about 45k) to the number of non-negative integer solutions to x_1 + x_2 + x_3 + x_4 + x_5 + x_6 = 6 (about 450).

# Questions

* When writing the background section, how should I make use of examples? Should I try and stick to examples that are closely connected to the case studies (e.g involving dice), or should I focus on using the clearest examples possible even if they explore slightly different domains?
* I'm concerned about adding too much background that's not relevant, or going into too much detail on aspects of background that aren't explored much in the dissertation. Are there any particular strategies you'd recommend for dealing with this (e.g should I just start writing whatever I can think of to begin with and trim things down later, or stay deliberately small and add more background as needed)?
* I think it could be fruitful to write about various techniques I've used to reduce the state space of various games (most notably things like aggregating dice rolls, such as the aforementioned integer solutions method or calculating the distribution of the sum of dice). These techniques are fairly general and apply across multiple case studies - do you think it would be better to describe them in each case study, or leave some space in the background section for them?


# Plan for next week

* Start creating some properties for 26.2 manually - mainly I want to focus on win probability and the expected number of rounds to reach the goal. Does the optimal strategy change when facing an opponent compared to trying to get the fewest number of rounds? (a single player game might encourage different levels of risk, for instance).
* Refactor current model to drastically reduce state space using the integer solutions method.
* Start developing preprocessing tools - I'm expecting this to be a tad easier than previous games since there's a lot of overlap with ShutTheBox.