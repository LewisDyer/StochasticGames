# Week 16 Status Report - 01/02/21

This week, I have started preprocessing work for 26.2, starting writing some background information in my dissertation, and investigated memory issues during model checking.

# Questions and notes

* I noted an unusual issue with the PRISM GUI, where in essence it turns out I had never increased the max CUDD memory in the first place (I didn't realise that pressing "okay" in the settings menu doesn't actually update your settings!). However I tried increasing the max CUDD memory and always received an out of memory error, even with a modest increase like from 1GB to 2GB. This occurred on the command line version as well as the GUI. 
* As a potential backup (in case the models are too big to run locally, or there's access issues with accessing a larger machine), I experimented with statistical model checking (mainly focusing on APMC). While of course statistical model checking is flawed (especially with resolving nondeterminism), the results were rather quick (100000 iterations took about 2 minutes per property), and the results matched up very closely to previous results with probabilistic model checking (e.g the win rate of player 1 was around 0.498 +/- 0.005), even for rare circumstances (e.g a tie). The addition of a probabilistic guarantee seems quite useful as well for communicating uncertainty. I think that running on a larger machine would give better results, but there's also potential risks such as the possibility that I don't collect enough data/end up changing the model and need to run model checking again.
* When writing the background, I'm not sure how much detail to use when describing/defining particular terms. In 2.1 I've described a TSG in full detail, whereas in 2.2 I've only described PCTL relatively informally - my logic here is that a TSG is a key definition I'll use over and over again, whereas I only use a relatively small subset of PCTL so it doesn't make much sense to describe the whole thing (I cite the source if the reader wants to know more).
* When I'm writing up definitions, would it read better to use examples during the definition, or give examples afterwards? For instance, when describing a TSG I use a few chess examples for some parts of the TSG as they're defined, which I think gives some more context.

# Plan for next week

* Keep working on preprocessing, I'm back into the swing of it now so it should hopefully be more straightforward from here.
* Complete some more work on the background chapter - at the moment I feel like I've frontloaded some of the dense background, so I'm anticipating things to be slightly faster this week.