# Week 8 Status Report - 18/11/20

This week, I have finished preprocessing for ShutTheBox, and have started building an automation environment using a Jupyter notebook. So far, I've been able to generate models, run experiments and verify properties using the PRISM command line, and I've started plotting data. Overall I've found this process easier than expected, in part because the preprocessing work I've completed substantially simplifies the process of generating PRISM models. Using a Jupyter notebook also seems like a good decision - in particular I discovered several features of Jupyter notebooks (in particular inserting Python variables into command line commands) that simplifies automation across Python scripts, PRISM command line tools and csv files.

# Questions/Comments

* I'm noticing that, according to the first property, my updated model doesn't always terminate. My remaining results match up precisely with my previous model, so I'm not sure why this first property gives a different result.
* Is there any way I can receive less verbose output when running PRISM from the command line? In my experiment notebook the output is quite long, which can make it quite hard to view the results of verifying properties. I could probably use pipes/greps to achieve this, but a flag when running PRISM from the command line would be more elegant.
* Should I commit my experiment data (i.e the generated models, .csv files containing results of PRISM experiments, and the visualisations) to version control? The data files are fairly small, but since they're automatically generated anyway I'm not sure if they should be included.

# Plan for next week

* Test experiment automation environment on my laptop (which runs Ubuntu) - beyond ensuring compatibility across different operating systems, this should help make sure the experiment environment is self-contained and provides everything needed to run experiments successfully.
* After starting automation, I've realised that I should extend preprocessing to support properties files as well as PRISM models. This should be a natural extension, since my preprocessor is sufficiently general, but I should take a little time to do this.
* Continue developing the automation environment. The core steps are there, for the most part I just need to tidy up some of the organisation, especially when running experiments on multiple configurations (e.g comparing the nondeterministic and high-board/low-board cases).
* If I manage to complete work on the experiment environment, start running experiments on a larger model (12 boards and 2d6).