#Plotly importing to be able to graph
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

types = ['Home Charger', 'Gas Station', 'Fast Charger']
#The calculation for 8000 goes as follows:
#13.5 gallon tank x 25.4 mpg and rounded down to 400 miles on a full tank 
#it takes about 3 minutes, which is 1/20 of an hour. 400 x 20 = 8000. 
times = [5, 7000, 180]


# Specify custom colors
colors = ['#0009FF', '#FF0000', '#0009FF']

title = 'Electric Cars vs. Gas Cars: Time Efficiency <br><sup>Miles of range refueled in an hour of fueling</sup>'
labels = {'x': 'Type', 'y': 'Refueling MPH'}
fig = px.bar(x=types, y= times, title = title, labels=labels,)
fig.update_traces(marker_color=['blue', 'red', 'blue'])
#Further customize chart.
fig.update_layout(xaxis_dtick=1,)
def show_refuel_time_chart():
    fig.show()