# Speech Analysis

This module contains a script and files to conduct analysis of political speeches from around the world. The main data file, `data.txt`, is the senticnet 4.0 database of over 50,000 words and n-grams, and their associated polarity scores. 

The files in `docs` are a collection of 130 public speeches and statements from the last two centuries. Each file has been given a shorthand name, but their actual descriptions are provided in a separate .md file. 

The script `df_gen.py` provided in this module converts the speeches using senticnet 4.0 into a dataframe that contains feature characteristics of the speeches. The columns are as follows: 

 1. Length of the speech, in words
 2. Word-by-word net positivity, normalized over length of the speech
 3. Word-by-word net positivity, normalized and scaled against an "average" speech rating of roughly 0.505
 4. Word-by-word net positivity, normalized, scaled, and re-anchored such that the first and last word of the speech both have a running sentiment of 0. This has the effect of creating an "arc" for a speech, showing how a speech might have a turn of mood in different segments. 
 5. Final net normalized positivity, on a scale of -100 to 100. 
 6. Variance of the speech, measured as the standard deviation of item (4). Higher values indicate more changes of mood or complexity in message. 

You can run the script again after adding more files into `docs`. It produces the file `sentiments.csv`. Do **not** open this file with anything other than a programming language, as the lists contained in the data frame results in inaccurate outputs when opened with applications like Microsoft Excel. 

The output images feature some of the analysis that has been conducted so far as a result of this script. In `conventions`, we see the scaled positivity scores of political convention speeches for Democrats and Republicans between 1980 and 2016. Each successive image adds an election cycle to the last. It validates the belief of some that President Trump's 2016 RNC speech was the darkest convention speech given in the last 40 years, as his oratory comes in at a record low for conventions of 3.44 (all other convention speeches have a score of at least 4.03, with a maximum of 6.42). 

In `obama`, we see a collection of all of the speeches of President Obama and their associated normalized sentiments. Perhaps the more interesting of the two is `speeches_var.jpg`, which shows the former President's speech at the July 2020 funeral for John Lewis as the speech with the largest change in mood of any speech he has given. 

