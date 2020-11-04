# Week 6 Meeting Minutes - 04/11/2020

This week mainly acted as a short progress report and a recap of work completed this week. Firstly, Gethin advised that statistical model checking is probably unsuitable for my project, since it doesn't support nondeterminism and strategy generation isn't supported. Indeed, Gethin remarked that statistical model checking is more like sampling as opposed to "actual" model checking.

I mentioned the paper on Chained Strategy Generation I had read, and Gethin said it's unlikely I would have time to use CSG in my project (which I agreed with), but suggested that the main things I should take from background reading are what makes a game "interesting" to play (for instance whether a dominant strategy exists or not).

My work on the preprocessor was discussed, and Gethin suggested that the existing preprocessor was quite limited, mainly handling simple behaviour such as for loops. Gethin suggested that, if I polished this further, my preprocessor could be used as the foundation for an additional feature in a future version of PRISM. I agreed to this, and agreed to show the preprocessor in more detail after some further polishing.

The design decision to contain board covering behaviour in the Shut the Box model was discussed, and Gethin agreed with my reasoning of wanting to ensure changes in strategy only impacted one module, namely the module the player directly controls. The use of module renaming was discussed to simplify processing of the model, but I remarked that this may not be feasible since the behaviour of each board differs (for instance, many possible die rolls end up covering board 1, but only one ends up covering board 12 using 2d6).

My choice of 3rd game was discussed. Gethin recommended that I delay my final decision so that I can gain more experience modelling games with PRISM and understanding more of the challenges involved with creating a model, to ensure that my final game is amenable to modelling. I agreed with this idea, and decided to keep a wide net for now, coming up with multiple different ideas but deciding on them at a later date.

Finally, the plan for the next week was discussed. I should finish the Shut the Box specific functions in the preprocessor, and start setting up an environment so that model building, model checking and visualisation can be automated. If I have time, testing this process on my existing simplified model (with 6 boards and 1d6) could be useful to ensure the process is successful before trying it on larger models.

