# Strategy Exploration in ShutTheBox

These are some notes I'm making to support the strategy exploration process.

### Aim

I'm trying to explain and explore the differences between the "optimal" strategies and the "high-board" strategy for Shut the Box. I notice that the high board strategy converges very closely to the optimal strategy for high scores, but not exactly, and this difference seems slightly larger as the model includes higher numbers of boards.

### Tools used

Because of how strategies are generated in PRISM-games, I need to use .dot files. In order to visualise graphs presented in .dot files, I explored several tools, including Gephi, ZGRViewer and Pajek. However the large size of these .dot files (hundreds of thousands of lines of code) means these graphs are typically too large to visualise normally. Hence, I decided to start with a small example of the game, `stb6_1d6`, the simplest version I have explored so far, where the visualisation is somewhat practical to explore (albeit it is still quite large!).

### Data Processing

`.dot` files for the high-board and nondeterministic versions of the `stb6_1d6` model were generated, verifying the probability that the max score was obtained, and were cleaned up as so:

* The label for each state was simplified to remove the state number, only showing the information for each state (the phase, value on the die, and the status for each board).

* The floating point numbers for the dice rolls were simplified to use fractions instead.

* The Unsat actions (where a vertex had an edge directing to itself because it could not continue but also did not reach the max score) were removed, so each unsatisfied vertex is now a sink vertex.

### Exploratory analysis

My aim in analysis was to identify ways in which the optimal and high-board strategy differed. After some searching, I found some interesting points. In particular, consider the state where a 6 is rolled, and boards 1, 3 and 5 are covered. The optimal strategy chooses to cover boards 4 and 2, while the high board strategy covers board 6. In the optimal strategy, the probability of getting the maximum score after making this move is 1 in 6 (need to roll a 6), whereas the probability of maxmimum score in the high board strategy is 1 in 18 (need to roll either 4 then 2, or 2 then 4). However, the expected value of the score is higher in the high-board case (16 1/6, as opposed to 16 for the optimal strategy).

In essence, this is because the optimal case _only_ values satisfying the particular property (namely, getting the highest score). It assigns no value whatsoever to attaining anything lower than 21, so the higher expected value is completely irrelevant. On the other hand, the high board strategy is more general, designed to obtain high scores more generally (if not the highest score possible).

Further property verification presents an interesting fact - the optimal and high-board strategies both have the same expected score at the end of the game, even though the strategies are different.