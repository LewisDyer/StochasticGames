# Week 5 Meeting Minutes - 28/10/2020

First, we discussed the models I had sent Gethin to review. Gethin remarked that the models looked good and the approach was feasible, but suggested some improvements to improve the model's readability and potentially make automated model creation easier. We briefly discussed the changes, and noted that a corner case still exists where no valid covers are found which could limit the possible improvements. Nevertheless, I agreed that a number of the changes were definitely feasible, such as using different action names for each covering decision, and agreed to review the updated model later and investigate which changes to include during automated generation.

We then discussed my issues when trying to synthesise strategies using PRISM-games. Gethin remarked that support for this was considerably better for CSGs, and that since all SMGs can be modelled as CSGs I should try this. Gethin demonstrated how the resulting `.dot` file should look, and how I could tidy it up to make it easier to review.

The issue of computing the expected number of roles required was discussed. Gethin mentioned this was technically possible, but quite involved to model. I then decided not to pursue this further, given I wasn't convinced whether that line of enquiry could be useful anyway.

Some further subtleties of Shut the Box were discussed and some example strategies were discussed, for instance strategies that prioritise keeping a particular board open for as long as possible. I remarked that automated generation could make these strategies very easy to generate, since I could generate a list of allowed partitions and then order them based on a strategy before converting these partitions into PRISM code.

A timeframe for the end of development was discussed, and Gethin remarked that it was still early to decide a final end date, but recommended I start writing my dissertation concurrently with the final stages of development around the start of semester 2. Gethin emphasised that dissertation writing can be challenging, and in particular it can be hard to stay motivated, so interleaving some of this with development work could help me stay engaged.

Finally, the plan for next week was agreed. I should start developing preprocessing scripts to generate larger models for Shut the Box automatically. I should also create a month-to-month plan for the remainder of the project to get a rough idea of what I should be worked on at each point, now that I have an idea of how long model development takes. If I have some time free after these tasks, I should start building and analysing larger models of Shut the Box, ideally starting experiment automation at the same time.





