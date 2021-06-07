import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlalchemy as sqla
import requests_cache
import matplotlib.pyplot as plt
import matplotlib.dates as pltdates
import datetime
from my_func import req

b = req('usa-facts', 'confirmed_cumulative_num', 'nation', '20200406-20210601')
#requests.get('https://api.covidcast.cmu.edu/epidata/api.php?endpoint=covidcast&data_source=usa-facts&signal=confirmed_cumulative_num&time_type=day&geo_type=nation&time_values=20200406-20210601&geo_value=*')
# b = cumulative cases 
c = req('usa-facts', 'confirmed_incidence_num', 'nation', '20200406-20210601')
#requests.get('https://api.covidcast.cmu.edu/epidata/api.php?endpoint=covidcast&data_source=usa-facts&signal=confirmed_incidence_num&time_type=day&geo_type=nation&time_values=20200406-20210601&geo_value=*')
# c = daily new cases 
d = req('usa-facts', 'deaths_incidence_num', 'nation', '20200406-20210601')
#requests.get('https://api.covidcast.cmu.edu/epidata/api.php?endpoint=covidcast&data_source=usa-facts&signal=deaths_incidence_num&time_type=day&geo_type=nation&time_values=20200406-20210601&geo_value=*')
# d = daily new deaths 


js2 = b.json()
datfram2 = pd.DataFrame(js2['epidata'])

js3 = c.json()
datfram3 = pd.DataFrame(js3['epidata'])

js4 = d.json()
datfram4 = pd.DataFrame(js4['epidata'])

#Plots

dates = pd.date_range(start="2020-04-06",end="2021-06-01")

plt.subplot(3, 1, 1)
plt.plot(dates,datfram2.value)
plt.title("Covid-19 in the USA")
plt.ylabel("Cumulative cases")

plt.subplot(3, 1, 2)
plt.plot(dates,datfram3.value)
plt.ylabel("Daily cases")

plt.subplot(3, 1, 3)
plt.plot(dates,datfram4.value)
plt.ylabel("Daily deaths")

plt.rcParams['figure.figsize'] = (20,10)



e = req('usa-facts', 'confirmed_cumulative_prop', 'state', '20210601')
#requests.get('https://api.covidcast.cmu.edu/epidata/api.php?endpoint=covidcast&data_source=usa-facts&signal=confirmed_cumulative_prop&time_type=day&geo_type=state&time_values=20210601&geo_value=*')
#cumulative number cases prop
f = req('usa-facts', 'deaths_cumulative_prop', 'state', '20210601')
#requests.get('https://api.covidcast.cmu.edu/epidata/api.php?endpoint=covidcast&data_source=usa-facts&signal=deaths_cumulative_prop&time_type=day&geo_type=state&time_values=20210601&geo_value=*')
#cumulative number deaths prop

js5 = e.json()
datfram5 = pd.DataFrame(js5['epidata'])

js6 = f.json()
datfram6 = pd.DataFrame(js6['epidata'])

#Plots

fig, ax = plt.subplots()
ax.bar(datfram5.geo_value, datfram5.value, 0.5, label = "cases")
ax.bar(datfram6.geo_value, datfram6.value, 0.5, bottom = datfram5.value, label = 'deaths')

ax.set_ylabel("Number per 100,000 population")
ax.set_title("Cumulative Covid-19 cases and deaths by state")
ax.legend()
plt.rcParams['figure.figsize'] = (20, 10)


h = req('fb-survey', 'smoothed_wwearing_mask', 'state', '20200406-20210601')
#requests.get('https://api.covidcast.cmu.edu/epidata/api.php?endpoint=covidcast&data_source=fb-survey&signal=smoothed_wwearing_mask&time_type=day&geo_type=state&time_values=20200406-20210601&geo_value=*')
js8 = h.json()
datfram8 = pd.DataFrame(js8['epidata'])

datfram8['time_value'] = pd.to_datetime(datfram8['time_value'], format = '%Y%m%d') 

datfram8_mod = datfram8[['geo_value', 'value', 'time_value']]

#first interactive plot

import plotly.express as px


datfram_0 = datfram8_mod[['geo_value', 'time_value', 'value']]
datfram_0.rename(columns={'geo_value':'State', 'time_value': "Date", 'value': "Percentage wearing masks"}, inplace = True)

figu1 = px.line(datfram_0, x="Date", y='Percentage wearing masks', color='State')
figu1.show()

#Plots comparing mask usage in SD, ND, HI, and UT

df8_sd = datfram8_mod[datfram8_mod['geo_value'].str.contains('sd')==True] 
df8_sd.reset_index(drop=True,inplace=True)

df8_nd = datfram8_mod[datfram8_mod['geo_value'].str.contains('nd')==True] 
df8_nd.reset_index(drop=True,inplace=True)

df8_hi = datfram8_mod[datfram8_mod['geo_value'].str.contains('hi')==True] 
df8_hi.reset_index(drop=True,inplace=True)

df8_ut = datfram8_mod[datfram8_mod['geo_value'].str.contains('ut')==True] 
df8_ut.reset_index(drop=True,inplace=True)

fig, ax = plt.subplots()

ax.plot(df8_sd.time_value, df8_sd.value, label = "South Dakota")
ax.plot(df8_nd.time_value, df8_nd.value, label = "North Dakota")
ax.plot(df8_hi.time_value, df8_hi.value, label = "Hawaii")
ax.plot(df8_ut.time_value, df8_ut.value, label = "Utah")

ax.set_ylabel("Proportionate percentage of people who wore masks")
ax.set_title("Specific States")
ax.legend()

dates_8 = pd.date_range(start="2020-09-08",end="2020-11-18")

k = req('usa-facts', 'confirmed_incidence_prop', 'state', '20200406-20210601')
#requests.get('https://api.covidcast.cmu.edu/epidata/api.php?endpoint=covidcast&data_source=usa-facts&signal=confirmed_incidence_prop&time_type=day&geo_type=state&time_values=20200406-20210601&geo_value=*')
js11 = k.json()
datfram11 = pd.DataFrame(js11['epidata'])

# Second interactive plot: time series of new cases prop.

datfram11['time_value'] = pd.to_datetime(datfram11['time_value'], format = '%Y%m%d')

datfram11 = datfram11[['geo_value', 'time_value', 'value']]
datfram11.rename(columns={'geo_value':'State', 'time_value': "Date", 'value': "Prop. New Cases per day"}, inplace = True)

figu = px.line(datfram11, x="Date", y='Prop. New Cases per day', color='State')
figu.show()


l = req('fb-survey', 'smoothed_hh_cmnty_cli', 'state', '20200908-20201118')
#requests.get('https://api.covidcast.cmu.edu/epidata/api.php?endpoint=covidcast&data_source=fb-survey&signal=smoothed_hh_cmnty_cli&time_type=day&geo_type=state&time_values=20200908-20201118&geo_value=*')
js12 = l.json()
datfram12 = pd.DataFrame(js12['epidata'])

datfram12['time_value'] = pd.to_datetime(datfram12['time_value'], format = '%Y%m%d')
datfram12 = datfram12[['geo_value', 'time_value', 'value']]
datfram12.rename(columns={'geo_value':'State', 'time_value': "Date", 'value': "Percentage of people who know someone is sick"}, inplace = True)


datfram8_mod.rename(columns ={'geo_value':"State", "time_value": "Date", "value": "Prop. Percentage wearing mask"}, inplace = True)


datfram_1 = datfram12.merge(datfram8_mod)
datfram_1
dff = datfram_1.iloc[:45]
dff2 = datfram_1.iloc[-29:]

#Interactive map plotting community illness vs mask usage by states

figu3 = px.scatter(dff, x="Prop. Percentage wearing mask", y='Percentage of people who know someone is sick', color = "State", title = "Mask usage vs people sick in community for September 8, 2020")
figu3.show()

figu4 = px.scatter(dff2, x="Prop. Percentage wearing mask", y='Percentage of people who know someone is sick', color = "State", title = "Mask usage vs people sick in community for December 11, 2020")
figu4.show()

#Correlation calculations 

datfram_1.corr(method = "spearman")
dff.corr(method = "spearman")
dff2.corr(method = "spearman")


m = req('fb-survey', 'smoothed_wrestaurant_1d', 'state', '20200908-20201118')
#requests.get('https://api.covidcast.cmu.edu/epidata/api.php?endpoint=covidcast&data_source=fb-survey&signal=smoothed_wrestaurant_1d&time_type=day&geo_type=state&time_values=20200908-20201118&geo_value=*')
js13 = m.json()
datfram13 = pd.DataFrame(js13['epidata'])


n = req('fb-survey', 'smoothed_wlarge_event_1d', 'state', '20200908-20201118')
#requests.get('https://api.covidcast.cmu.edu/epidata/api.php?endpoint=covidcast&data_source=fb-survey&signal=smoothed_wlarge_event_1d&time_type=day&geo_type=state&time_values=20200908-20201118&geo_value=*')
js14 = n.json()
datfram14 = pd.DataFrame(js14['epidata'])


datfram13['time_value'] = pd.to_datetime(datfram13['time_value'], format = '%Y%m%d')
datfram13 = datfram13[['geo_value', 'time_value', 'value']]
datfram13.rename(columns={'geo_value':'State', 'time_value': "Date", 'value': "Percentage of people who went to a restuarant in the last 24 hours"}, inplace = True)

datfram14['time_value'] = pd.to_datetime(datfram14['time_value'], format = '%Y%m%d')
datfram14 = datfram14[['geo_value', 'time_value', 'value']]
datfram14.rename(columns={'geo_value':'State', 'time_value': "Date", 'value': "Percentage of people who went to a large event (10+ people) in last 24 hours"}, inplace = True)


#Comprehensive correlation calculation

datfram_2 = datfram13.merge(datfram14)
dff3 = datfram_2.merge(datfram_1)
dff3.corr(method = "spearman")



