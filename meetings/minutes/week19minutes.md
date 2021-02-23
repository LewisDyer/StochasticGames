# Week 19 Minutes - 23/02/21

First, the cluster results were discussed. The results seemed in line with expectations, but concern was raised regarding the time taken to obtain results in the 100 space case. I agreed with this concern, and explained that I had decided to stick with the 50 space case where at all possible, and only consider the 100 space case where there is a clear benefit or comparison to make.

Some suggestions were discussed in order to handle obtaining experimental results before running on the cluster. Gethin suggested building the models as MDPs or DTMCs using the MTBDD engine (with an -m flag on PRISM), which can exploit symmetry and structure in the model in order to dramatically reduce the model size. I decided to investigate this suggestion, while also remarking that the experiment prototype results need not be terribly accurate, since I don't intend to use those results in final analysis.

Then, some finer points on dissertation writing were discussed. Gethin agreed to review my current background work and make suggestions over the next few days. Gethin also suggested that I don't need to go into full technical detail on how PRISM operates, but I should focus on the principles of model checking. Gethin also recommended placing PRISM-games specific details in the first case study, while recommending I remain flexible in where it should be placed.

The plan for next week was discussed - I would start work on a prototype environment for the third game, considering the MDP/DTMC suggestions along with statistical model checking. I would finish off some last small sections of the initial background, and potentially start writing up the first case study if time allows.



