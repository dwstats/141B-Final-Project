import requests 
import pandas as pd
import matplotlib.pyplot as plt

def req(data_source, signal, geo_type, time_values):
    start = str("https://api.covidcast.cmu.edu/epidata/api.php?endpoint=covidcast&data_source=")
    start += str(data_source)
    start += str("&signal=")
    start += str(signal)
    start += str("&time_type=day&geo_type=")
    start += str(geo_type)
    start += str("&time_values=")
    start += str(time_values)
    start += str("&geo_value=*")
    a = requests.get(start)
    return a


