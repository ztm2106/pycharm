Check Your Understanding
QUESTION: Which function can help you determine the number of entries for a state?
num_entries(state)

QUESTION: If a state has 496 entries, then the ID of the first entry is 2020-03-01 and the ID of the
most recent entry is 2020-07-05.


Short Answer Questions
1. Approximately how long did this assignment take you to complete?

About 2 hours

2. Describe some of your artistic choices for the visualization.

x axis label which is yellow
y axis label which is an orange/red color
2 white axis for x and y
Title that is white
The death plots are red
The case plots are blue
The background is darkgrey
All blits are set to true to have it look a little smoother

** I learned how to rotate things in pygame from a simple google search and used it to rotate the axis label to look a little better


3. What do you think the slope of the line means about the COVID-19 cases or deaths?

When the slope is horizontal that means there was not any deaths or cases.
When the slope is upward that meanings cases and deaths have increase.

4. Can you find any states for which there are very different curve shapes or where the
death and case curves are different? Which states did you find? Do you have any
thoughts on why the shapes are different?

More populated states like NY, FL, CA, NJ, PA have similar case graphs, however
graph begin to differ drastically when comparing states like MT, VT, Guam, OR  and others.
There is a slower rate of exposure to COVID 19 for these less populated and largely more inland states.
Same thing is true about the deaths graphs are the death rates are much greater and seem earlier
in comparison to the less populated and largely more inland states.



5. Is there a part of the program you had to try to write several times to get correct?
Explain what went wrong with your initial attempts.

Yes, when inputting information for the tuple in the win.set_at().
I needed to use covid_data.num_entries(state) inside the covid_data.cases_by_entry_id function to retrieve the number of entries.
Also, I had to subtract 1 from the entries to plot point all the way up to but not including today.