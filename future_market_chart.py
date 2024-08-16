import plotly.graph_objects as go

# Data
labels = ['Electric', 'Gas']
values = [30, 70]

# Specify custom colors
colors = ['#0009FF', '#FF0000',]

# Chart Creating
heading = '2030 Electric Cars vs. Gas Cars Market Share <br><sup> Estimated new cars sold (worldwide) </sup>'
fig = go.Figure(data=[go.Pie(labels=labels, values=values, title=heading, marker=dict(colors=colors))])
def show_future_market_chart():
    fig.show()