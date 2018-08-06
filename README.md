# regression_college_football_recruiting

### This Python script performs simple linear regression on college football S&P Rating (via [Football Outsiders](https://www.footballoutsiders.com/stats/ncaa2017)) as a function of recruiting (via [247 Sports](https://247sports.com/Season/2017-Football/CompositeTeamRankings)).

The dataset covers 11 seasons of NCAA football (2007-2017) and includes 1,118 data points. I scraped the data myself and I included a clean CSV file in this repository. The columns within the dataset are as follows:

> *season, team, recruiting_avg, s&p_rating*

The dependent variable is end-of-season S&P rating. To measure recruiting, the independent variable, I converted each year's recruiting scores into percentile form. I then took the average of a team's four recruiting classes preceding each season. That means a team's 2007 S&P Rating is plotted against its recruiting performance from 2004 to 2007.

Teams without S&P and/or recruiting data were excluded, but on average over 100 teams per season were tracked.

The script uses *linregress()* within the Scipy library to output correlation data, the standard error, and a p value (the null hypothesis being zero slope or no correlation). I also wrote custom functions to generate 95% confidence bands around the regression line, and to output *Sum of Squares* data. I then use Matplotlib and Pyplot to plot the data.

The output of the script and the plot it generates are below:


```
r = 0.6467180948136898
R² = 0.4182442941594487
std. error: 0.034475161369989044
p = 1.9590276195987828e-133

Explained Sum of Squares: 355125.66791448044
Residual Sum of Squares: 493961.03302469617
Total Sum of Squares: 849086.7009391766
```



![alt text](https://i.imgur.com/mhF3Oey.png "CFB S&P as a Function of Recruiting")


I should make clear that this isn't intended to be a rigorous analysis of a causal effect. In reality, there are many more variables that affect college football success. This is a look at just one correlation.
