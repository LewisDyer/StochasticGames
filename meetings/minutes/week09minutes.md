# Week 9 Minutes - 25/11/20

The questions for this week were discussed. Firstly, the issue of numerical convergence was discussed. For the probability of termination being greater than one, Gethin remarked that this was unusual since convergence should happen from below rather than above, but that this shouldn't be an issue given that the property is mainly used as a "quick check". With regards to conditional probabilities, Gethin remarked that performing division when compiling visualisations would be best to avoid floating point issues, but that my proposed method of computing conditional probabilities may be problematic, since this method will give unexpected results with nondeterministic models. I remarked that I currently only calculate these probabilities when the strategy is deterministic (e.g the high-board strategy), but that I would keep this in mind for future models.

A short discussion ensued on the type of model to be created. At the moment I'm creating a CSG, since this is sufficiently general to work for all of the games I plan on developing, but this also means that graph-based methods for reachability, which are considerably faster than methods based on numerical convergence, could be utilised. However I also recalled from a previous meeting that support for strategy generation is considerably better for CSGs than SMGs, so I plan to stick to CSGs for the time being.

After this, I asked about separating model checking and visualisation into separate notebooks, which Gethin recommended so that models are not automatically recreated and data is recollected (potentially taking 10-15 minutes, or even longer). Overall, the aim should be to collect data once, and use this data in as many ways as possible.

Strategy generation was discussed, and Gethin recommended using .dot files to compare strategies. For large files, where direct visualisations may be impractical, Gethin recommended using text processing tools like grep and diff to compare strategies (in particular the high-board and optimal strategies for obtaining the maximum score). The .dot file format is fairly simple to understand, so this hopefully shouldn't take too long.

Finally, the plan for next week was reviewed. In particular, I said that I was slightly behind my month-by-month plan, so I would start Liar's Dice in the December project period rather than the last week of November. Gethin said this was fine, since I was on track anyway, and I would naturally make up time in the second semester.



