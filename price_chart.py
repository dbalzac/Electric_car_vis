#Plotly importing to be able to graph
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#$ Per Mile calculations 
#Find out the user's gas price
run = True
while run:
  try:
    gas_price = float(input("What is your local gas price($/g)? Say '0' to use a USA average: "))
    if (gas_price) == 0:
      gas_price = 3.50
  except ValueError:
    #impliment a try-except to prevent invalid vaues
    print("Try again with a valid number!")
    continue
  else:
    pass
    run = False

#gas price divided by average mpg of a vehicle that size

#gas sedan price = (gas_price)/31
#gas suv price = (gas_price)/25
#gas pickup price = (gas_price)/18

#Find the user's electricity price
elec_run = True
while elec_run:
  try:
    elec_price = float(input("How much does your electricity cost($/kwh)? Say '0' to use a USA average: "))
    if (elec_price) == 0:
      elec_price = 0.15
  except ValueError:
    #impliment a try-except to prevent invalid vaues
    print("Try again with a valid number!")
    continue
  else:
    pass
    elec_run = False

#KWH price divided by mpkwh
#Electric price = (elec_price)/mpkwh
#Electric sedan price = (elec_price) /4
#Electric suv price = (elec_price) / 2.8
#Electric pickup price = (elec_price) / 2.4

#Assigning the calculations to headings
df = pd.DataFrame({
  "Size": ["Sedan", "SUV", "Pickup", "Sedan", "SUV", "Pickup"],
  "Fuel": ["Electric", "Electric", "Electric", "Gas", "Gas", "Gas"],
  "$ Per Mile": [round((elec_price)/3.5,2), round((elec_price)/2.8, 2), round((elec_price)/2.4, 2), 
                 round((gas_price)/31, 2), round((gas_price)/25, 2), round((gas_price)/18, 2)],
})

#Adding main headings
fig = px.bar(df, x="Size", y="$ Per Mile", color="Fuel", barmode="group",)
#Creating the chart
fig = go.Figure()
for Fuel, group in df.groupby("Fuel"):
    fig.add_trace(go.Bar(x=group["Size"], y=group["$ Per Mile"], name=Fuel,
      hovertemplate="Fuel=%s<br>Size=%%{x}<br>$ Per Mile=%%{y}<extra></extra>"% Fuel))
fig.update_layout(legend_title_text = "Fuel", title = f"Electric Cars Vs. Gas Cars: Price Efficiency <br><sup>{elec_price} dollars/kwh</sup> <br><sup>{gas_price} dollars/gallon</sup>")
fig.update_xaxes(title_text="Size")
fig.update_yaxes(title_text="$ Per Mile")

def show_price_chart():
  fig.show()