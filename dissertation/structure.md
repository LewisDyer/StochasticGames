# Structure

A very rough outline of how the dissertation will be structured (page counts are very approximate, subject to change)

## Introduction (2 pages)

Motivate the project. Why is balancing games a challenging problem in the first place? Why is model checking an appropriate tool to examine game design/balance?

## Background (3 pages)

Give context on existing work, both in model checking and in automated game design (RMT coursework very helpful for this). Identify a gap in current work (e.g certain types of games that haven't been analysed very much, or discussion on robustness of models). How can I tie this into my project?

Note: don't go into specific details about model types here (MDPs/POMDPs/CSGs) - leave them to later on.

## Case Study One (Shut the Box):

### Game description (1/2 page)

Describe the game, mention some variants, set out the sorts of questions we'd like to answer about the game.

### Background (1 page)

Describe MDPs here, explain why they're a suitable tool to model Shut The Box (essentially a 1 player game).

### Analysis (3 pages)

Collect some data, show the results.

### Evaluation (2 pages)

The key section - use the results from model checking to answer questions about the game (for instance, to examine the difficulty and/or complexity of a game).

## Case Study Two (Liar's Dice):

### Game description (1/2 page)

Very similar to case study 1, description of the game and potential questions about it.

### Background (1 page)

Describe POMDPs here - what makes them important and useful compared to MDPs? Explain why we add this additional complexity, but also mention trade offs in terms of the sorts of analysis we can perform.

### Analysis (3 pages)

Collect data, show results. Make sure to mention how game trees are constructed to infer results about games based on individual rounds.

### Evaluation (2 pages)

Again, use model checking results to answer questions about Liar's Dice. Discuss potential limitations of analysis that arise from using POMDPs.

## Case Study Three (26.2)

### Game description (1/2 page)

Again describe the game, come up with some questions to answer about the game. What happens with n players?

### Background (1 page)

Introduce CSGs, compare them to MDPs and explain why they're useful for modelling 26.2

### Analysis (3 pages)

Vary different parameters of the game (spaces, number of dice, different strategies...), show results.

### Evaluation (2 pages)

Use results to answer questions about 26.2, show the differing behaviour of using different model types.


## Evaluation (2 pages)

Discuss the general process of conducting these case studies. What makes this rigorous research? What could have been improved? Use weighted dice analysis to compare and contrast games. (This is where I could mention experiment automation/preprocessing work to improve replicability)

## Conclusion (2 pages)

Summarise the project, discuss some potential future work. In particular, could the techniques used while analysing weighted dice be used in other applications of model checking (say safety critical systems)?