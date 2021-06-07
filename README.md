# 141B-Final-Project
## Group members: David Wong

For this project, I decided to explore more of the covid-19 data from the covidcast API, specifically with a view on how mask usage affected covid rates and how similar variables influenced the covid-19 pandemic.

First, I made broad visualizations to get a sense of the scale of the pandemic. The cumulative total cases, daily cases, and daily deaths across the nation were compared through plotting in matplotlib. The data was scraped from the covidcast API using the request package.   

I then compared the total number of cases, proportionately, and deaths by each state with a bar graph. Some states were clearly outliers, but the average number of cases per 100,000 persons was 10,000, meaning 10% of the population was infected with covid-19 on average.  

The mask usage was plotted as a time series from when the data was availale from the fb-survey for the signal that was used earlier in the pandemic and more relevant as the vaccine was not availabl during the time period examined (approximately from September to November was analysed due to the limitations of the dataset). While this time series is interactive as you can hide individual states, a comparison of behavior towards masks as viewed seperately containing some of the outliers. 

The daily number of new cases reported was plotted as a time series from April to June of 2020 to see which states were particularly struggling in the beginning of the pandemic.

Two scatter plots were then constructed to visualize the correlations between mask usage and the number of known sick people in a community. Each scatter plot represented one of two dates: September 8th and December 11th of 2020, as these were the endpoints of the date range usable. Running spearman correlation tests on each individual scatter plot and the combined data showed a clear negative correlation between wearing masks and knowing sick people showing covid-like symptoms.

Additional variables considered in this correlation were the proportionate percentages of people who visited restaurants or bars in the last 24 hours and the proportionate percentages of people who attended large events, those with ten or more people attending. The spearman correlation test showed these factors were positively associated with higher likelihood of knowing someone in the community with covid-like symptoms, while wearing a mask was negatively associated with all three other variables.  

We find that there is clear, numerical evidence between the association of mask-wearing, and other socializing, with greater numbers of people sick with covid-like symptoms 

### Directories

The code directory has python .py file for the web scraping, data munging, and visualizations, along with a script for functions. 

Specifically, my_func.py has is for using the request function. 




The corresponding pandas dataframes variables used are as follows:

datfram2: cumulative cases

datfram3: nationwide daily new cases 

datfram4: nationwide daily new deaths

datfram5: cumulative cases by state (usafacts)

datfram6: cumulative deaths by state (usafacts)

datfram8: percentag eof people who wore masks in the last 24 hours

datfram11: proportion of daily new cases by state

datfram12: community covid sypmtoms (perecentage of people)

datfram13: percentage of people who went to restaurants/bars in the last 24 hours

datfram14: percentage of people who attended large events (10+ people) in the last 24 hours




The data directory has the JSON files used for each request. 

The notebooks directory has the Jupyter notebook writeup that goes into more detail of the code. 
