import plotly.graph_objects as go

#Data
labels = ['Electric','Gas']
values = [13, 87,]

# Specify custom colors
colors = ['#0009FF', '#FF0000',]

#Chart Creation
heading = '2023 Electric Cars vs. Gas Cars Market Share  <br><sup> Current new cars sold (worldwide) </sup>'
fig = go.Figure(data=[go.Pie(labels=labels, values=values, title = heading, marker=dict(colors=colors))])
def show_current_market_chart():
    fig.show()