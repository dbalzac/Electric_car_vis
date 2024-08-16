#Plotly importing to be able to graph
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
#Data: types of refueling stations and amount of stations there are
types = ['Generic Charger', 'Gas Station', 'Tesla Supercharger']
amounts = [55000, 170000, 1700]

title = 'Electric Cars vs. Gas Cars: Refueling Stations <br><sup>Number of stations in the USA, not amount of individual outlets</sup>'
labels = {'x': 'Type', 'y': 'Amount'}
fig = px.bar(x=types, y= amounts, title = title, labels=labels)

#Further customize chart.
fig.update_layout(xaxis_dtick=1)
fig.update_traces(marker_color=['blue', 'red', 'blue'])
def show_refueling_locations_chart():
    fig.show()