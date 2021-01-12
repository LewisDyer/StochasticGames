# Timelog

* Modelling and analysing Stochastic games
* Lewis Dyer
* 2299195D
* Dr. Gethin Norman

## Guidance

* This file contains the time log for your project. It will be submitted along with your final dissertation.
* **YOU MUST KEEP THIS UP TO DATE AND UNDER VERSION CONTROL.**
* This timelog should be filled out honestly, regularly (daily) and accurately. It is for *your* benefit.
* Follow the structure provided, grouping time by weeks.  Quantise time to the half hour.

## Week 1

Date | Duration | Summary
---- | -------- | -------
30/09/2020 | 1 hour | Downloaded example project template from Moodle. Modified template for my project, removing irrelevant folders. Tested .tex files to ensure they could successfully compile. Inserted project information into timelog and plan markdown files.
02/10/2020 | 0.5 hours | Supervisor meeting
04/10/2020 | 2 hours | Read industry-focused paper on quantitative verification, completed first 2 tutorials on the PRISM model checker.

## Week 2

Date | Duration | Summary
---- | -------- | -------
05/10/2020 | 0.5 hours | Tidied up weekly status report in preparation for supervisor meeting, created git repository and committed progress so far.
07/10/2020 | 0.5 hours | Supervisor meeting
08/10/2020 | 2.5 hours | Completed PRISM tutorial part 5 on EGL contract signing

## Week 3
Date | Duration | Summary
---- | -------- | -------
12/10/2020 | 2 hours | Worked on PRISM tutorial on dining philosophers (up to courteous extension). Read lectures 1-4 of PMC lecture notes.
13/10/2020 | 1.5 hours | Read lectures 5-7 and 10-12 of PMC lecture notes, prepared summary and questions for tomorrow's supervisor meeting.
14/10/2020 | 1 hour | Supervisor meeting + refining minutes
18/10/2020 | 3.5 hours | Completed examples 1 and 2 of PRISM-games, along with reading up on user-centric networks case study. Read first two case studies of game design paper and downloaded source code to read through/experiment with


## Week 4
Date | Duration | Summary
---- | -------- | -------
19/10/2020 | 2 hours | Finished reading case studies of game design paper, Read through some source code from their examples. Reviewed .dot file from rock paper scissors to try and understand strategies. Added some questions for this week's meeting.
20/10/20 | 0.5 hours | Completed plan for week 4 meeting
21/10/20 | 0.5 hours | Supervisor meeting
24/10/20 | 2.5 hours | Started developing shut the box model with 6 boards, basic model definition + created some properties to analyse.
25/10/20 | 2.0 hours | Wrote up initial analysis, tidied up project structure, planned next steps for Shut The Box model.

## Week 5
Date | Duration | Summary
---- | -------- | -------
27/10/20 | 1 hour | Added questions, prepared notes for upcoming supervisor meeting
28/10/20 | 1 hour | Supervisor meeting + writing minutes
29/10/20 | 1.5 hours | Started work on preprocessing scripts - developed core system to handle function calls and write to new files.

## Week 6
Date | Duration | Summary
---- | -------- | -------
03/11/20 | 3.5 hours | Wrote month-by-month plan for remainder of project, extended preprocessing to support parameters, added some ShutTheBox specific functionality. Prepared status report and questions for tomorrow's meeting.
04/11/20 | 0.5 hours | Supervisor meeting, added minutes
07/11/20 | 2 hours | Added board cover generating function to preprocessing

## Week 7
Date | Duration | Summary
---- | -------- | -------
10/11/20 | 2.5 hours | Improved preprocessor to inherit whitespace from template tag. Almost finished off ShutTheBox specific functions, generated a few example models and prepared status report.
11/11/20 | 0.5 hours | Supervisor meeting, added minutes
15/11/20 | 4 hours | Finished off preprocessor for ShutTheBox, included documentation for preprocessor, started experiment automation environment. Updated status report with some questions

## Week 8
Date | Duration | Summary
---- | -------- | -------
18/11/20 | 0.5 hours | Supervisor meeting, writing up minutes
19/11/20 | 1.5 hours | Adding more visualisations to automation environment, fixed bug in preprocessor with nondeterministic strategy in ShutTheBox
21/11/20 | 1.0 hours | Extended plotting capabilities to add keyword arguments, plotted more sets of data. Plan to start analysing larger models now

## Week 9
Date | Duration | Summary
---- | -------- | -------
23/11/20 | 2 hours | Tidying up visualisations, improving experiment automation, added some questions for next meeting
24/11/20 | 2 hours | Fixed bug with model not fully generating when max roll is greater than number of possible boards. Tidied up questions and comments for next supervisor meeting
25/11/20 | 1 hour | Supervisor meeting and writing up minutes
26/11/20 | 1.5 hours | Reorganised folder structure, parameterised filenames, separated visualistion and model checking into separate notebooks
29/11/20 | 1 hour | Trialled generating and viewing strategies using .dot files - experimented with various tools for visualisation (Gephi/Pajek/ZGRViewer), tried out diff (seems really messy, focus on subsets of .dot files instead)

## Week 10
Date | Duration | Summary
---- | -------- | -------
30/11/20 | 0.5 hours | Looked into gvpr for processing .dot files, decided it was probably overkill/ill-suited for my usecase
31/11/20 | 1.5 hours | Visualised stb6_1d12 with ZGRViewer, wrote up initial notes on strategy generation
01/12/20 | 3.5 hours | Improved strategy generation notes, wrote up questions for supervisor meeting, refactored conditional probabilities to improve efficiency
02/12/20 | 1.5 hours | Supervisor meeting, added minutes and tidied up plan
03/12/20 | 3 hours | Collected more data for multiple dice in stb12 case, started background reading on POMDPs. Built development version of PRISM using Cygwin, still need to edit system path to be able to access both versions of PRISM at once
04/12/20 | 1 hour | Experimenting with McCallum's maze problem in PRISM-POMDPs
05/12/20 | 1 hour | Built prism-pomdps on Ubuntu, setup aliases for prism-games and prism-pomdps. Verified dev environment works as expected on linux.

## Week 11 (Crunch period part 1)

Date | Duration | Summary
---- | -------- | -------
07/12/20 | 6 hours | Read through POMDPs paper in more detail, took notes on aspects of POMDPs that would be relevant when designing Liar's Dice. Added notes on the mechanics of Liar's Dice, and ideas for potential opponents. Started implementation of Liar's Dice model, implementing die roll phase and simple initial bid phase. Also implemented extremely simplistic betting strategy to show game flow. Completed skeleton model of Liar's Dice - _very_ simplistic, and still needs double checking/verifying, but the whole process of a round is modelled.
08/12/20 | 5 hours | Morning + afternoon session of project guidance lectures. Wrote up rough draft of status report (will update next week with more relevant information). Noticed problem with properties taking a long time to terminate with MDPs - will investigate further tomorrow.
09/12/20 | 5 hours | Investigated long verification time for Liar's Dice - tried making smaller variants of models, altering grid resolution. Supervisor meeting + adding minutes. Came up with method to reduce state space, started creating preprocessing tools to permit this.
10/12/20 | 6 hours | State reduction method unsuccessful, need to find other ways to simplify model. Tried combining all die rolls into one step - this too was unsuccessful. Storing both player's bids in one set of variables also unsuccessful - for now, start preprocessing and adjust as needed later.
11/12/20 | 6 hours | Started preprocessing for Liar's Dice, can now generate an entire model (albeit with simple strategies). Noticed some strange issues with model size between POMDPs and MDPs - will investigate further.

## Week 12 (Crunch period part 2)

Date | Duration | Summary
---- | -------- | -------
14/12/20 | 5.5 hours | Sketched out ideas for evaluating Liar's Dice using game trees, generated smaller example with 2 dice each to demonstrate viability of model checking. Started plan for the week, polished status report slightly. Defined some more challenge strategies. Setup prism-pomdps alias on Windows, will be able to start experiment environment tomorrow.
15/12/20 | 5.5 hours | Started work on experiment environment, noticed a few things I needed to update in preprocessing to get useful results. Started working on developing game trees and understanding how I could export model checking results in order to answer questions about games using rounds.
16/12/20 | 4 hours | Continued work on game tree construction. Supervisor meeting, wrote up minutes, finalised status report. Drafted message to designer of 3rd game asking some questions about their design decisions.
17/12/20 | 5 hours | Debugged POMDP, encountered issue with different action choice based on hidden variables. Reverted to previous challenge criteria due to this issue, continued work on experiment environment. Tomorrow - use game tree results to get probability of winning game.
18/12/20 | 4 hours | More debugging of game tree construction - modified reward structure to support different starting players. Constructed tree, got meaningful results about winrate! Code might need a refactor (currently need to generate relevant model checking data beforehand). Still need some sort of visualisation (.dot file?)

## Week 13 (start of semester 2)

Date | Duration | Summary
---- | -------- | -------
11/01/21 | 0.5 hours | Started planning structure of dissertation, getting up to speed
12/01/21 | 1 hour | Further work on dissertation structure, added very approximate page counts. Supervisor meeting plus adding minutes
